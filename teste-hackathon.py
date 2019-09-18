print("Considerando os seguintes papéis: ")
print("1 - Desenvolvedor")
print("2 - Negócios")
print("3 - UX/UI")
print("4 - PO")
role = int(input("Digite o papel desejado: "))

level = int(input("Numa escala de 0 a 10, qual o seu nível de conhecimento nesse papel? ")) 

confirma = input("Papel: " + str(role) + " Nível: " + str(level) + ". Podemos confirmar sua inscrição ? (s/n)")

if confirma == "S" or confirma == "s": 
    print("Inscrição confirmada com sucesso!")
else: 
    print("Inscrição cancelada!")

