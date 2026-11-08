"""Primeiro teste de YOLO com webcam/vídeo e métricas de desempenho.

Uso: python scripts/testar_yolo.py --modelo yolo26n.pt --duracao 60
Não treina um modelo de EPIs: utiliza pesos gerais pré-treinados.
"""

import argparse
import csv
from collections import deque
from datetime import datetime
from math import ceil
from pathlib import Path
from statistics import mean, median
from time import perf_counter

import cv2
from ultralytics import YOLO


def argumentos():
    parser = argparse.ArgumentParser(description="Teste inicial de YOLO e FPS")
    parser.add_argument("--modelo", default="yolo26n.pt", help="Ex.: yolo26n.pt, yolo11n.pt, yolov8n.pt")
    parser.add_argument("--fonte", default="0", help="Índice da câmera (0) ou caminho de vídeo")
    parser.add_argument("--duracao", type=float, default=60, help="Segundos de medição após aquecimento")
    parser.add_argument("--aquecimento", type=float, default=5, help="Segundos iniciais sem coleta")
    parser.add_argument("--imgsz", type=int, default=480, help="Resolução de entrada do YOLO")
    parser.add_argument("--conf", type=float, default=0.4, help="Confiança mínima de detecção")
    parser.add_argument("--largura", type=int, default=640, help="Largura solicitada da câmera")
    parser.add_argument("--altura", type=int, default=480, help="Altura solicitada da câmera")
    parser.add_argument("--device", default="cpu", help="Dispositivo, por padrão CPU")
    args = parser.parse_args()
    if args.duracao <= 0 or args.aquecimento < 0:
        parser.error("--duracao deve ser > 0 e --aquecimento deve ser >= 0")
    if not 0 <= args.conf <= 1 or args.imgsz <= 0:
        parser.error("--conf deve estar entre 0 e 1 e --imgsz deve ser > 0")
    return args


def p95(valores):
    """Percentil 95 por posto mais próximo (sem dependências extras)."""
    ordenados = sorted(valores)
    return ordenados[max(0, ceil(0.95 * len(ordenados)) - 1)]


def salvar_csv(registros, args, resolucao):
    pasta = Path("resultados")
    pasta.mkdir(exist_ok=True)
    nome_modelo = Path(args.modelo).stem.replace(" ", "_")
    arquivo = pasta / f"teste_{nome_modelo}_{datetime.now():%Y%m%d_%H%M%S}.csv"
    campos = ["modelo", "device", "fonte", "imgsz", "conf", "resolucao",
              "frame", "tempo_s", "modelo_ms", "loop_ms", "inferencia_interna_ms", "deteccoes"]
    contexto = {
        "modelo": args.modelo,
        "device": args.device,
        "fonte": args.fonte,
        "imgsz": args.imgsz,
        "conf": args.conf,
        "resolucao": f"{resolucao[0]}x{resolucao[1]}",
    }
    with arquivo.open("w", newline="", encoding="utf-8") as saida:
        escritor = csv.DictWriter(saida, fieldnames=campos)
        escritor.writeheader()
        for registro in registros:
            escritor.writerow({**contexto, **registro})
    print(f"Modelo: {args.modelo} | Dispositivo: {args.device} | Fonte: {args.fonte}")
    print(f"Configuração: imgsz={args.imgsz} conf={args.conf} resolução capturada={resolucao}")
    print(f"CSV salvo em: {arquivo}")


def main():
    args = argumentos()
    fonte = int(args.fonte) if args.fonte.isdecimal() else args.fonte
    print(f"Carregando {args.modelo} (pode haver download na primeira execução)...")
    modelo = YOLO(args.modelo)
    camera = cv2.VideoCapture(fonte)
    if not camera.isOpened():
        raise SystemExit(f"Não foi possível abrir a fonte: {args.fonte}")
    if isinstance(fonte, int):
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, args.largura)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, args.altura)

    resolucao = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("Pressione Q para encerrar antecipadamente. Aguarde o fim para ver as métricas.")
    registros = []
    ultimos_loops_ms = deque(maxlen=30)
    inicio = perf_counter()
    contagem_frames = 0
    try:
        while True:
            inicio_loop = perf_counter()
            ok, frame = camera.read()
            if not ok:
                print("Fim do vídeo ou falha na leitura da câmera.")
                break

            inicio_modelo = perf_counter()
            resultado = modelo.predict(
                source=frame,
                imgsz=args.imgsz,
                conf=args.conf,
                device=args.device,
                verbose=False,
            )[0]
            modelo_ms = (perf_counter() - inicio_modelo) * 1000
            imagem = resultado.plot()

            fps_loop = 1000 / mean(ultimos_loops_ms) if ultimos_loops_ms else 0.0
            cv2.putText(imagem, f"FPS total: {fps_loop:.1f}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(imagem, f"Modelo: {modelo_ms:.1f} ms", (15, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.imshow("PIBIC-Jr | Teste inicial YOLO", imagem)
            tecla = cv2.waitKey(1) & 0xFF

            fim_loop = perf_counter()
            loop_ms = (fim_loop - inicio_loop) * 1000
            contagem_frames += 1
            decorrido = fim_loop - inicio
            if decorrido >= args.aquecimento:
                ultimos_loops_ms.append(loop_ms)
                velocidade = resultado.speed or {}
                inferencia_interna = velocidade.get("inference")
                registros.append({
                    "frame": contagem_frames,
                    "tempo_s": round(decorrido, 3),
                    "modelo_ms": round(modelo_ms, 3),
                    "loop_ms": round(loop_ms, 3),
                    "inferencia_interna_ms": round(inferencia_interna, 3) if inferencia_interna is not None else "",
                    "deteccoes": len(resultado.boxes) if resultado.boxes is not None else 0,
                })

            if tecla == ord("q") or decorrido >= args.aquecimento + args.duracao:
                break
    except KeyboardInterrupt:
        print("Teste interrompido pelo teclado.")
    finally:
        camera.release()
        cv2.destroyAllWindows()

    if not registros:
        print("Nenhuma medição após o aquecimento. Tente diminuir --aquecimento.")
        return

    tempos_loop = [linha["loop_ms"] for linha in registros]
    tempos_modelo = [linha["modelo_ms"] for linha in registros]
    print(f"\nFrames medidos: {len(registros)}")
    print(f"FPS total médio (captura + modelo + tela): {1000 / mean(tempos_loop):.2f}")
    print(f"FPS total aproximado mínimo/máximo por frame: {1000 / max(tempos_loop):.2f} / {1000 / min(tempos_loop):.2f}")
    print(f"Tempo médio da chamada ao modelo: {mean(tempos_modelo):.2f} ms")
    print(f"Tempo mediano da chamada ao modelo: {median(tempos_modelo):.2f} ms")
    print(f"P95 da chamada ao modelo: {p95(tempos_modelo):.2f} ms")
    print("Observação: FPS total NÃO é o FPS interno da inferência isolada.")
    salvar_csv(registros, args, resolucao)


if __name__ == "__main__":
    main()
