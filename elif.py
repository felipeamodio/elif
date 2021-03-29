pontuacao = int(input("Digite sua pontuação: "))

if pontuacao >= 1000:
    print("Você ganhou um bônus de 3 gb na sua franquia de internet")
elif pontuacao >= 500:
    print("Você ganhou um bônus de 1.5 gb na sua franquia de internet")
elif pontuacao >=200:
    print("Você ganhou um bônus de 500 mb na sua franquia de internet")
else:
    print("Você não tem pontos suficientes para ganhar o bônus")
