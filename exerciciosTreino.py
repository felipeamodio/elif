rm = input("Insira seu rm: ")
idade = input("Insira sua idade: ")

if int(idade) >= 18:
    print("Sua participação no curso foi autorizada, aluno de RM {}".format(rm))
else:
    autorizado = input("Você possui autorização dos seus pais? Responda com S ou N")
    if autorizado == 'S':
        print("Sua participação no curso foi autorizada, aluno de RM {}".format(rm))
    else:
        print("Sua participação no curso não foi autorizada por seus pais não terem dado a autorização pois você é menor de idade")

#   OR e AND
#
# o OR retorna verdadeiro se pelo menos 1 dos testes for verdadeiro
#
# o AND só torna verdadeiro se todos forem verdadeiro
#
#
#
#
#
#
#
#
#

