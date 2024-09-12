
#Menu inicial
def menu():
    opcao = -1
    while opcao >= 1 or opcao <= 6:
        print("Bem vindo  ao nosso sistema de ajuda!\n"
    "[1] Diagnóstico do veículo\n"
    "[2] Medidas preventivas\n"
    "[3] Assistente  virtual\n"
    "[4] Despesas\n"
    "[5] Sobre nós\n"
    "[6] Soluções para seu veículo\n"
    "[7] Cadastro\n"
    "[8] Login")
        opcao = int(input('\nDigite a opção desejada: '))
        if(opcao < 1 or opcao > 8):
            print('Opção inválida')
        else: 
            return opcao
        
def diagnostico_veiculo():
    print("\nVocê escolheu a opção diagnóstico")
    contato = int(input('\n Informe a forma de contato para retorno?'))
    modelCar = int(input('\n Qual o modelo do seu veículo?'))
    anoCar = int(input('\n Qual o ano do seu veículo?'))
    motivo = int(input('\n Quais adversidades você identificou em seu veículo? Descreva detalhadamente.'))
    if(modelCar, anoCar, motivo, contato != ""):
        print('Opção inválida!')
    else:
        return ('Os dados foram adicionados e foram encaminhados ao nosso centro de controle e em breve entraremos em contato')
    
def medidas_preventivas():
    print("\nVocê escolheu a opção medidas preventivas")
    print("\n1-Verifique os pneus regularmente: Veja se os pneus têm pressão suficiente e se não estão gastos ou danificados.\n"
        "2-Freios em bom estado: Verifique regularmente o sistema de freios, incluindo pastilhas, discos e fluido de freio. Substitua os componentes desgastados.\n"
        "3-Mantenha as luzes do carro em bom estado: Verifique regularmente se todas as luzes do carro estão funcionando corretamente.\n"
        "4-Mantenha os pneus alinhados: Um alinhamento adequado dos pneus ajuda a garantir um desgaste uniforme e uma condução suave.\n"
        "5-Mude o óleo regularmente: Siga as recomendações do fabricante para troca de óleo e filtro.\n"
        "6-Bateria: Verifique regularmente a bateria, garantindo que os terminais estejam limpos e bem conectados. Substitua a bateria conforme necessário, especialmente se estiver mostrando sinais de falha.\n"
        "7-Use o freio de estacionamento: Isso ajuda a evitar danos à transmissão.\n"
        "8-Evite sobrecarregar o carro: Não carregue mais peso do que o recomendado.\n"
        "9-Faça revisões regulares: Leve o carro a um mecânico regularmente para verificar se está tudo bem.")
    
def assistente_virtual():
    print("\nVocê escolheu a opção assistente virtual")
    print("Acesse nossa assitente virtual por esse link: https://web-chat.global.assistant.watson.appdomain.cloud/preview.html?region=us-south&integrationID=250f2872-90d1-4b69-a463-e7c03c0581c9&serviceInstanceID=cd14777c-39ac-401b-938f-9849d2bb018f")        

def despesas():
    lista = []
    print("\nVocê escolheu a opção despesas")
    print('Insira o valor por peça usada ou se preferir insira o total do valor das peças, e escolha "não" para encerrar.')
    repetir = input('Você deseja calcular os gastos das peças? (sim ou não) ')
    while repetir == "sim":
        peca = float(input('Valor da peça: '))
        lista.append(peca)
        repetir = input('Deseja continuar adicionando o valor das peças? (sim ou não) ')
    sum1 = sum(lista)
    #pecas = float(input('Digite o valor das peças: '))
    mao_de_obra = float(input('Digite o valor da mão de obra: '))
    despesa = mao_de_obra + sum1
    print(f'Total das despesas: {despesa}')
    
def sobre_nos():
    escolha = -1
    integrantes = ["Eduarda", "Gustavo", "Vitor"]
    parceiros = ["FIAP", "Porto Seguro"]
    resumo = ("O aplicativo PortoCarCare oferece uma solução inovadora para motoristas, com ou sem conhecimento\n"
        "prévio sobre a mecânica de um carro, preocupados com o diagnóstico do problema e a manutenção de seus veículos.\n"
        "O objetivo do aplicativo é usar da tecnologia para proporcionar aos motoristas uma experiência simplificada e\n"
        "confiável ao lidar com problemas mecânicos e de manutenção, sem ter que ir fisicamente a uma oficina mecânica \n" 
        "para saber qual é o problema do seu automóvel, poupando tempo e mão de obra.\n"
        "Nosso serviço oferece uma assistente virtual, programada para auxiliar o cliente, para fazer a análise do caso do cliente\n"
        "e fazer perguntas para chegar a um diagnóstico mais exato possível. Além disso, o aplicativo com uma certa frequência envia\n"
        "notificações aos usuários, buscando fornecer a eles dicas e lembretes úteis sobre a manutenção preventiva, e com isso, ajudar\n"
        "a prolongar a vida útil dos veículos e evitar acidentes ou problemas futuros.")
    
    while opcao >= 1 or opcao <= 6: #VER QUE NEGÓCIOS É ESSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("Bem vindo ao conteúdo de nossa empresa!\n"
        "[1] Integrantes\n"
        "[2] Sobre nós\n"
        "[3] Parceirias\n")
        opcao = int(input('\nDigite a opção desejada: '))
        if(opcao < 1 or opcao > 3):
            print('Opção inválida')
        else: 
            return opcao
    
    
    
def solucoes_veiculos():
    #elaborar
    
def login():
    #elaborar
    
def cadastro():
    #elaborar


#Controla as opções do usuário     
def controlador(opcao):
    if opcao == 1:
        result = diagnostico_veiculo()
    elif opcao == 2:
        result = medidas_preventivas()
    elif opcao == 3:
        result = assistente_virtual()
    elif opcao == 4:
        result = despesas()
    elif opcao == 5:
        result = sobre_nos()
    elif opcao == 6:
        result = solucoes_veiculo()
    elif opcao == 8:
        result = login(usuarios)
    elif opcao == 7:
        result = cadastro(usuarios)
    else:
        print("Opção inválida")
    return result