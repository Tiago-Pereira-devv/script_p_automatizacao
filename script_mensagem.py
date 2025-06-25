import pywhatkit
import time

# Lista de contatos (formato +código país DDD número)
contatos = [
    "+5582993234882",
    "+558232025021"
]

# Mensagens que serão enviadas
mensagem_1 = "Opa, tudo bem? Me chamo Tiago, sou do setor de agricultura de precisão e estou entrando em contato referente à sua máquina que veio equipada com o módulo de telemetria. Este módulo trata-se do CM100, ele transfere dados através de sinal de internet via chip telefônico. Dados estes que serão possíveis visualizar pelo nosso aplicativo FieldOps. Como por exemplo: velocidade de deslocamento, localização da máquina, histórico de movimentação da máquina, RPM do motor, etc."
mensagem_2 = "Já lhe foi informado sobre nosso aplicativo do FieldOps para o monitoramento da sua máquina?"

# Envia mensagens para todos os contatos
for contato in contatos:
    try:
        # Primeira mensagem
        pywhatkit.sendwhatmsg_instantly(contato, mensagem_1, wait_time=10, tab_close=True)
        print(f"Mensagem 1 enviada para {contato}")

        # Espera 10 segundos entre as mensagens
        time.sleep(10)

        # Segunda mensagem
        pywhatkit.sendwhatmsg_instantly(contato, mensagem_2, wait_time=10, tab_close=True)
        print(f"Mensagem 2 enviada para {contato}")

        # Espera 20 segundos antes de passar para o próximo contato
        time.sleep(20)

    except Exception as e:
        print(f"Erro ao enviar para {contato}: {e}")

print("Mensagens enviadas para todos os contatos.")
