ano = 1997
nome = "Felipe Alves Amodio"
saldo = 415.83

print("O tipo da variável ano é {}".format(type(ano)))
print("O tipo da variável nome é {}".format(type(nome)))
print("O tipo da variável saldo é {}".format(type(saldo)))

# convertendo variável

variave_float = 5.2
variavel_int = int(variave_float)
print(variavel_int) #ele ignora as casas decimais e só mostra as partes inteiras

#rm = input("Insira seu RM: ")
#idade = input("Insira sua idade: ")
#if int(idade) >= 18:
 #   print("Sua autorização foi autorizada, aluno de RM {}!".format(rm))
#else:
 #   print("Sua participação não foi autorizada por causa da sua idade")

#funcionario = input("Digite o nome do funcionario: ")
#salario = float(input("Digite o salário do funcionário: "))

#if salario < 0: #os dois pontos servem pra indicar que o que vier abaixo só vai acontecer se o teste for verdadeiro
 #  salario = salario * -1

  # print("O salário do funcionário {} é {}".format(funcionario, salario))


idadeAluno = int(input("Digite sua idade: "))
nameAluno = str(input("Digite o seu nome: "))

if idadeAluno >= 18:
     print("Parabéns pela aquisição do curso, {}. Faça bom proveito :)".format(nameAluno))
else:
     print("Parabéns pela aquisição do curso, {}. Ficaremos no aguardo do envio da aprovação dos seus pais para realizar as aulas". format(nameAluno))