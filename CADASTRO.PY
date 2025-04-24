lista = []
opcao = 0
while(opcao != 1):
 print("\n CADASTRO \n 1.Sair \n 2.Cadastrar \n 3.Lista")
 opcao = int(input("Digite sua opção: "))
 if (opcao == 2):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))
  IMC = peso/(altura*altura)
  lista.append([nome,idade,peso,altura,IMC])
  print("Seu IMC é:" , round(IMC,1))
  if IMC < 18.5:
    print("Abaixo do peso")
  elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso normal")
  elif IMC > 24.9:
    print("Excesso de peso")
  print("Seu nome é:", nome), print("Sua idade é:", idade,"anos")

 elif (opcao == 3):
  senha = int(input("Digite a senha "))
  if senha == 1234:
    print(lista)
    if lista == []:
      print("Nenhuma pessoa cadastrada")
  else:
    print("SENHA INCORRETA")

 elif (opcao == 1):
  print("\n VOLTE SEMPRE")
 else:
  print("OPÇÃO INVÁLIDA")
