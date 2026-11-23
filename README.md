
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

A aplicação foi testada em laboratório utilizando uma Raspberry Pi, dois LEDs e o serviço personalizado monitor_rede.service, gerenciado pelo systemd.

Durante os testes, foi possível observar o comportamento do sistema em duas condições de conectividade:

Conectividade disponível: o programa identificou respostas ao comando ping, mantendo o LED verde aceso e o vermelho apagado.

Falha de conectividade: quando o endereço de teste deixou de responder, o programa apagou o LED verde e acendeu o vermelho.

Após o restabelecimento da conectividade, o LED verde voltou a acender automaticamente, sem necessidade de reiniciar o programa.

O comando systemctl status monitor_rede.service confirmou que o serviço estava em execução (active (running)) e habilitado para inicialização automática (enabled). As mensagens registradas no terminal também permitiram acompanhar as mudanças de estado da conexão.

Evidências fotográficas

Figura 1 — Falha de conectividade



Montagem experimental com o LED vermelho aceso e registros de falha de conectividade no terminal da Raspberry Pi.

Figura 2 — Conectividade disponível



Montagem experimental com o LED verde aceso e registros de conectividade bem-sucedida, incluindo a recuperação após falhas.

Esses resultados demonstram que o monitor conseguiu identificar alterações na conectividade e atualizar os LEDs automaticamente, enquanto o programa permanecia em execução como serviço do Linux.

## 9. Versionamento com Git

O projeto utiliza Git para registrar as alterações realizadas durante seu desenvolvimento e GitHub para armazenar os arquivos e a documentação.

O histórico de commits será disponibilizado no arquivo `historico_git.txt`, gerado pelo comando:

```bash
git log > historico_git.txt
```

## 10. Conclusão


A Prática 5 permitiu compreender o funcionamento do systemd no gerenciamento de aplicações em sistemas embarcados Linux. Por meio de um serviço personalizado, foi possível executar um programa Python de monitoramento de conectividade na Raspberry Pi, utilizando os LEDs como indicadores visuais.

Os testes demonstraram o funcionamento da aplicação em condições de conectividade disponível e indisponível, incluindo a atualização automática dos indicadores após mudanças na rede.

Além disso, a utilização do arquivo .service permitiu configurar o gerenciamento e a inicialização automática da aplicação, enquanto o script de parada implementou uma rotina de encerramento controlado.

A atividade mostrou como o systemd pode ser utilizado para manter aplicações embarcadas em funcionamento sem a necessidade de executá-las manualmente pelo terminal, além de reforçar a importância dos registros do sistema para acompanhar e verificar seu comportamento.
