
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
    modelCar = int(input('\n Qual o modelo do seu veículo?'))
    anoCar = int(input('\n Qual o ano do seu veículo?'))
    motivo = int(input('\n Quais adversidades você identificou em seu veículo? Descreva detalhadamente.'))
    if(modelCar, anoCar, motivo != ""):
        print('Opção inválida!')
    else:
        return modelCar, anoCar, motivo
    
def medidas_preventivas():
    #elaborar
    
def assistente_virtual():
    #elaborar        

def despesas():
    #elaborar
    
def sobre_nos():
    #elaborar
    
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