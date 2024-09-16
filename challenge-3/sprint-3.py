# Eduarda Tiemi Akamini Machado RM: 554756
# Gustavo de Oliveira Turci Sandrini RM:557505
# Vitor Vinicios Araújo RM: 556241


#Menu inicial
clientes = {}

def menu():
    while True:
        try:
            print("Bem vindo  ao nosso sistema de ajuda!\n"
                "[1] Diagnóstico do veículo\n"
                "[2] Medidas preventivas\n"
                "[3] Assistente  virtual\n"
                "[4] Despesas\n"
                "[5] Sobre nós\n"
                "[6] Dados usuário\n"
                "[7]Sair")
            opcao = int(input('\nDigite a opção desejada: '))
            if(opcao < 1 and opcao > 7):
                print('Opção inválida')
            else: 
                return opcao
        except ValueError:
            print('Valor inválido. Digite uma opção válida') 
        finally:
            print('Fechando menu\n ')   
        
def diagnostico_veiculo():
    try:
        print("\nVocê escolheu a opção diagnóstico")
        contato = input('Informe a forma de contato e contato para retorno?\n ')
        modelCar = input('Qual o modelo do seu veículo?\n ')
        anoCar = int(input('Qual o ano do seu veículo?\n '))
        motivo = input('Quais adversidades você identificou em seu veículo? Descreva detalhadamente.\n ')
        # if(modelCar, anoCar, motivo, contato == ""):
        #     print('Opção inválida!')
    except ValueError as e:
        print(f'Erro: {e}')
    else:
        print('Os dados foram adicionados e encaminhados ao nosso centro de controle. Em breve entraremos em contato.')
    finally:
        print('Finalizando diagnóstico.')

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
    print("Acesse nossa assitente virtual por esse link: \n  https://web-chat.global.assistant.watson.appdomain.cloud/preview.html?region=us-south&integrationID=250f2872-90d1-4b69-a463-e7c03c0581c9&serviceInstanceID=cd14777c-39ac-401b-938f-9849d2bb018f")        

def despesas():
    lista = []
    print("\nVocê escolheu a opção despesas")
    print('Insira o valor por peça usada ou se preferir insira o total do valor das peças, e escolha "não" para encerrar.')
    repetir = input('Você deseja calcular os gastos das peças? (sim ou não) ')
    try:
        while repetir == "sim":
            peca = float(input('Valor da peça: '))
            lista.append(peca)
            repetir = input('Deseja continuar adicionando o valor das peças? (sim ou não) ')
        #pecas = float(input('Digite o valor das peças: '))
        mao_de_obra = float(input('Digite o valor da mão de obra: '))
        despesa = mao_de_obra + sum(lista)
        print(f'Total das despesas: {despesa}')
    except ValueError:
        print('Erro: Por favor, insira valores numéricos válidos.')
    finally:
        print('Finalizando cálculo de despesas.')
    
    
def integrante():
    print("Eduarda, Gustavo, Vitor")
    
def parceiros():
    print("FIAP e Porto Seguro")
def resumo():
    print("O aplicativo PortoCarCare oferece uma solução inovadora para motoristas, com ou sem conhecimento\n"
        "prévio sobre a mecânica de um carro, preocupados com o diagnóstico do problema e a manutenção de seus veículos.\n"
        "O objetivo do aplicativo é usar da tecnologia para proporcionar aos motoristas uma experiência simplificada e\n"
        "confiável ao lidar com problemas mecânicos e de manutenção, sem ter que ir fisicamente a uma oficina mecânica \n" 
        "para saber qual é o problema do seu automóvel, poupando tempo e mão de obra.\n"
        "Nosso serviço oferece uma assistente virtual, programada para auxiliar o cliente, para fazer a análise do caso do cliente\n"
        "e fazer perguntas para chegar a um diagnóstico mais exato possível. Além disso, o aplicativo com uma certa frequência envia\n"
        "notificações aos usuários, buscando fornecer a eles dicas e lembretes úteis sobre a manutenção preventiva, e com isso, ajudar\n"
        "a prolongar a vida útil dos veículos e evitar acidentes ou problemas futuros.")
def sobre_nos():
    while True:
        try:
            print("Sobre nós!\n"
                "[1] Integrantes\n"
                "[2] Parceiros\n"
                "[3] Resumo")
            opcao3 = int(input('\nDigite a opção desejada: '))
            if(opcao3 < 1 and opcao3 > 3):
                print('Opção inválida')
            else: 
                return opcao3
        except ValueError:
            print('Valor inválido. Digite uma opção válida') 
        finally:
            print('Fechando\n ')
    
def controlador_sobre(opcao):
    if opcao == 1:
        integrante()
    elif opcao == 2:
        parceiros()
    elif opcao == 3:
        resumo()
   

    
def menu_usuario():
    while True:
        try:
            print("Bem vindo ao menu do usuário!\n"
                "[1] Cadastrar\n"
                "[2] Verificar dados\n"
                "[3] Alterar dados de cadastro\n"
                "[4] Excluir dados de cadastro\n"
                "[5] Voltar ao menu principal")
            opcao2 = int(input('\nDigite a opção desejada: '))
            if(opcao2 < 1 and opcao2 > 5):
                print('Opção inválida')
            else: 
                return opcao2
        except ValueError:
            print('Valor inválido. Digite uma opção válida') 
        finally:
            print('Fechando menu\n ')  
            
def controlador_usu(opcao2):
    if opcao2 == 1:
        dados = dados_usu()
        adicionar_dados_dicionario(dados)
    elif opcao2 == 2:
        email = usu_email()
        verifica_dados(email)
    elif opcao2 == 3:
        email = usu_email()
        altera_dados(email)
    elif opcao2 == 4:
        email = usu_email()
        excluir_dados(email)
    elif opcao2 == 5:
        menu()


def usu_nome():
    while True:
        nome = input('Digite seu nome: ')
        if nome == '':
            print('Valor inválido')
        else:
            return nome
def usu_email():
    while True:
        email = input('Digite seu e-mail: ')
        if email == '':
            print('Valor inválido')
        else:
            return email
            
def usu_tel():
    while True:
        tel = input('Digite seu telefone: ')
        if tel == '':
            print('Valor inválido')
        else:
            return tel


def dados_usu():   
    email = usu_email()
    dados = {
        email: {
            "email": email,
            "nome": usu_nome(),
            "telefone": usu_tel()
        }
    }
    return dados

def adicionar_dados_dicionario(dados):
    clientes.update(dados)

def verifica_dados(email):
    if email in clientes:
        for chave, valor in clientes[email].items():
            print(f'{chave}: {valor}\n')
    else:
        print('Email não encontrado')
        
def altera_dados(email):
    if email in clientes:
        print('Alterar dados')
        verifica_dados(email)
        while True:
            chave = input('Digite qual dado deseja alterar: ')
            if chave == 'email' or chave == 'nome' or chave == 'telefone':
                while True:
                    valor = input('Digite o novo valor: ')
                    if  valor != '':
                        clientes[email][chave] = valor
                        print('dados alterados')
                        break
                    else:
                        print('Valor inválido')
                break
            else:
                print('Valor inválido')
        

def excluir_dados(email):
    if email in clientes: 
        del clientes[email]
        print('Dados excluídos')
    else:
        print('Email não cadastrado')

            



def controlador(opcao):
    if opcao == 1:
        diagnostico_veiculo()
    elif opcao == 2:
        medidas_preventivas()
    elif opcao == 3:
        assistente_virtual()
    elif opcao == 4:
        despesas()
    elif opcao == 5:
        opcao = sobre_nos()
        controlador_sobre(opcao)
    elif opcao == 6:
        opcao = menu_usuario()
        controlador_usu(opcao)

    else:
        print("Opção inválida")
        
def principal():
    continuar = True
    while continuar:
        opcao = menu()
        controlador(opcao)
        resposta = input("\nDeseja voltar ao menu principal? (s/n): ")
        if resposta.lower() != 's':
            continuar = False
    
#programa principal
principal()
