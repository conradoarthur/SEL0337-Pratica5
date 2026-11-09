
import os
import signal
import subprocess
import time
from gpiozero import LED

# Configuracao dos LEDs (numeracao BCM)
led_verde = LED(17)
led_vermelho = LED(27)

# Endereco testado e intervalo entre verificacoes
ALVO = os.environ.get("PING_ALVO", "1.1.1.1")
INTERVALO = 2

executando = True


def encerrar(signum, frame):
    """Solicita o encerramento seguro do programa."""
    global executando
    executando = False


def testar_conexao():
    """Retorna True se o endereco responder ao ping."""
    try:
        resultado = subprocess.run(
            ["ping", "-n", "-c", "1", "-W", "1", ALVO],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3,
            check=False
        )
        return resultado.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


signal.signal(signal.SIGTERM, encerrar)
signal.signal(signal.SIGINT, encerrar)

try:
    print("Monitor de conectividade iniciado.", flush=True)

    while executando:
        if testar_conexao():
            led_verde.on()
            led_vermelho.off()
            print("Conectividade OK", flush=True)
        else:
            led_verde.off()
            led_vermelho.on()
            print("Falha de conectividade", flush=True)

        # Espera entre as verificacoes
        time.sleep(INTERVALO)

finally:
    # Apaga os LEDs e libera os pinos
    led_verde.off()
    led_vermelho.off()
    led_verde.close()
    led_vermelho.close()
    print("Monitor encerrado.", flush=True)
