
# SEL0337 — Prática 5: Monitor de Conectividade de Rede

Alunos: 
Arthur Conrado Nunes Santos - 14668168
Ulisses Lombardi Campos - 14781443

## 1. Objetivo

Desenvolver uma aplicação em Python para monitorar a conectividade de rede de uma Raspberry Pi 3B+, utilizando LEDs para indicar o resultado das verificações.

A aplicação será configurada como um serviço do Linux por meio do `systemd`, permitindo sua inicialização automática durante o boot e seu gerenciamento pelos comandos `systemctl`.

## 2. Funcionamento

O programa realiza periodicamente um teste de conectividade utilizando o comando `ping`.

- **LED verde:** acende quando o endereço configurado responde ao teste.
- **LED vermelho:** acende quando o teste de conectividade falha.
- **Intervalo de verificação:** 5 segundos, além do tempo necessário para executar o teste.

O endereço padrão utilizado é `1.1.1.1`, podendo ser alterado pela variável de ambiente `PING_ALVO`.

## 3. Materiais

- Raspberry Pi 3B+
- Protoboard
- 1 LED verde
- 1 LED vermelho
- 2 resistores de 220 Ω ou 330 Ω
- Jumpers
- Fonte de alimentação
- Conexão à rede

## 4. Conexões

| Componente | GPIO (BCM) | Pino físico |
|---|---|---|
| LED verde | GPIO17 | 11 |
| LED vermelho | GPIO27 | 13 |
| GND | — | 6 |

Cada LED deve ser conectado em série com seu respectivo resistor.

## 5. Arquivos do projeto

- `monitor_rede.py`: programa responsável pelo monitoramento da conectividade e controle dos LEDs.
- `monitor-rede.service`: arquivo de configuração do serviço `systemd`.
- `parar_monitor.sh`: script executado durante a parada do serviço, responsável por solicitar o encerramento do programa Python.

## 6. Instalação e execução

Os comandos abaixo consideram o usuário `sel` e o diretório `/home/sel/pratica5`. Esses caminhos devem ser ajustados conforme a configuração da Raspberry utilizada.

### Preparação

```bash
chmod +x /home/sel/pratica5/parar_monitor.sh
python3 /home/sel/pratica5/monitor_rede.py
```

Após confirmar o funcionamento manual, interromper o programa com `Ctrl+C`.

### Configuração do serviço

```bash
sudo cp /home/sel/pratica5/monitor-rede.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start monitor-rede.service
sudo systemctl status monitor-rede.service
```

### Inicialização automática

```bash
sudo systemctl enable monitor-rede.service
sudo reboot
```

### Parada e consulta dos registros

```bash
sudo systemctl stop monitor-rede.service
journalctl -u monitor-rede.service
```

## 7. Procedimento de teste

Os seguintes testes estão previstos para a execução em laboratório:

1. Verificar o funcionamento do LED verde com a Raspberry conectada à internet.
2. Desconectar o Wi-Fi e observar a indicação de falha pelo LED vermelho.
3. Reconectar o Wi-Fi e verificar o restabelecimento da indicação verde.
4. Parar o serviço pelo `systemctl` e verificar se os LEDs são desligados.
5. Habilitar a inicialização automática, reiniciar a Raspberry e confirmar o funcionamento do serviço após o boot.

## 8. Resultados e evidências

*Seção a ser preenchida após a execução da prática.*

Serão registrados os resultados observados, as fotografias da montagem e as capturas do terminal demonstrando a execução e o gerenciamento do serviço.

## 9. Versionamento com Git

O projeto utiliza Git para registrar as alterações realizadas durante seu desenvolvimento e GitHub para armazenar os arquivos e a documentação.

O histórico de commits será disponibilizado no arquivo `historico_git.txt`, gerado pelo comando:

```bash
git log > historico_git.txt
```

## 10. Conclusão

*Seção a ser preenchida após a validação do funcionamento da aplicação e da inicialização automática pelo systemd.*
