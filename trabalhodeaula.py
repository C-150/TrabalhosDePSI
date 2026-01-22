from operator import truediv

Notas=[]

while True:
    int(input("Diga uma nota:"))

opcao = int( input(Notas))


if opcao == "1":
    Notas = input("Diga sua nota:")
    Notas.append(0)
    print(int("Nota adicionada."))

else:
    print("Notas")
    for i in range(len(Notas)):
     print("Notas", i + 1, "-",Notas[i])

     if Notas ==[]
         print("Não há alunos.")
     else:
         print("Alunos:")
         for i in range(len(alunos)):
             print(i + 1, "-", alunos[i])

       Notas= int(input("Notas o aluno: ")) - 1

         if Notas >= 0 and Notas < len(Notas):
             Notas = float(input("Introduza a nota do aluno (0 a 20): "))

             if nota >= 0 and nota <= 20:
                 Notas[escolha] = nota
                 print("Nota inserida com sucesso!")
             else:
                 print("Erro: a nota deve estar entre 0 e 20.")
         else:
             print("Notas inválidas.")

     if contador == 0:
         print("Não existem notas.")
     else:
         media = soma / contador
         print("Média:", media)

         if media < 10:
             print("Classificação: Insuficiente")
         elif media < 14:
             print("Classificação: Suficiente")
         elif media < 18:
             print("Classificação: Bom")
         else:
             print("Classificação: Muito Bom")



