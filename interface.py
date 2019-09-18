from participant import Participant
from participantsService import ParticipantsService

participantsService = ParticipantsService()
participantsList = []
registerAnother = 's'
confirm = 'n'

def getUserData():
    global name
    global role
    global level
    name = input("Digite o seu nome: ")
    print("Considerando os seguintes papéis: ")
    print("1 - Desenvolvedor")
    print("2 - Negócios")
    print("3 - UX/UI")
    print("4 - PO")
    role = int(input("Digite o papel desejado: "))
    level = int(input("Numa escala de 0 a 10, qual o seu nível de conhecimento nesse papel? ")) 
   
def registerUser():
    global confirm
    global registerAnother
    confirm = input("Papel: " + str(role) + " Nível: " + str(level) + ". Podemos confirmar sua inscrição ? (s/n) ")
    if confirm == "S" or confirm == "s": 
        participantsList.append(Participant(name, role, level))
        print("Inscrição confirmada com sucesso!")
        print(participantsList)
        registerAnother = input("Deseja registrar outro usuário? (s/n)")
    else: 
        print("Inscrição cancelada!")    
        registerAnother = input("Deseja registrar outro usuário? (s/n)")
       
def run():
    participantsService.getMockedUsers(participantsList)
    while registerAnother == 's' or registerAnother == 'S':
        getUserData()
        registerUser()

run()