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


funcionario = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salário do funcionário: "))

if salario < 0: #os dois pontos servem pra indicar que o que vier abaixo só vai acontecer se o teste for verdadeiro
   salario = salario * -1

   print("O salário do funcionário {} é {}".format(funcionario, salario))