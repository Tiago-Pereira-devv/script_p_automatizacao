import pywhatkit
import time

# Adicionar contato com Código do país mais DDD
contato = "+5582993234882"

# Anexar endereço da imagem
imagens = [
    "C:/Users/Tiago/Desktop/imagens_script/field_ops_app.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/tela_login.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/EULA.jpeg"
]

# texto da legenda
legendas = [
    "Nosso aplicativo Mobile: FielOps. Encontra-se disponível para Donwload gratuito pelo Google Play ou Apple Store",
    "Assim que finalizar instalar o aplicativo efetue seu login inserindo email e senha",
    "Quando tranferirmos sua máquina para o portal, irá aparecer essa solicitação de termos de condições, onde a transmissão de dados será ativada após o aceitamento destes termos. Assim como todo aplicativo que, para utilizá-lo, precisamos aceitar os termos de condições. Caso tenha mais dúvidas os termos podem ser lidos através do link disponível na própria solicitação."
]

# Regra FOR para envio do ciclo de mensagens
for i in range(len(imagens)):
    fechar_aba = False if i == len(imagens) - 1 else True
    pywhatkit.sendwhats_image(
        contato,
        imagens[i],
        caption=legendas[i],
        wait_time=20,
        tab_close=fechar_aba
    )
    print(f"Imagem {i+1} enviada")
    time.sleep(10)  # pausa maior para garantir o envio

print("Envios concluídos.") # Status de Conclusão
