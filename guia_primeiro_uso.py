import pywhatkit
import time

# Adicionar contato com Código do país mais DDD
contato = "+557996505818"

# Anexar endereço da imagem
imagens = [
    "C:/Users/Tiago/Desktop/imagens_script/acesso_1.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/acesso_2.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/acesso_3.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/acesso_4.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/acesso_5.jpeg",
    "C:/Users/Tiago/Desktop/imagens_script/acesso_6.jpeg"
]

# texto da legenda
legendas = [
    "Ao entrar no aplicativo é possível acessar o perfil das suas máquinas clicando neste botão indicado",
    "Já direcionado na aba equipamentos, para ver os detalhes especificos de uma máquina, acesse o botão indicado pela seta",
    "Ao entrar no status específicos da máquina teremos de cara esses dois botões, o botão indicado pela seta azul ao ser selecionado irá entregar o histórico de movimentação da máquina das ultimas 24h. Já o botão indicado pela seta verde irá lhe direcionar para a localização da máquina via Google ",
    "Este exemplo detalha como que é entregue o histórico de movimentação das ultimas 24h.",
    "Para visualizar todos os parâmetros da sua máquina, role a tela para baixo e clique neste botão 'ver todos os parâmetros'.",
    "Você será direcionado para esta tela e poderá ver detalhadamente todos os parâmetros disponíveis para sua máquina."
    
]

# Regra FOR para envio do ciclo de mensagens
for i in range(len(imagens)):
    fechar_aba = False if i == len(imagens) - 1 else True
    pywhatkit.sendwhats_image(
        contato,
        imagens[i], 
        
        caption=legendas[i],
        wait_time=10,
        tab_close=fechar_aba
    )
    print(f"Imagem {i+1} enviada")
    time.sleep(10)  # pausa maior para garantir o envio

print("Envios concluídos.") # Status de Conclusão
