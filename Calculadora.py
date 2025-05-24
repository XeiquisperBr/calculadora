import sys
opcao = ""
while opcao not in ["1", "2", "3", "4","5"]:
    print("-----Menu Calculadora-----\n")
    print("[1].Soma")
    print("[2].Subtração")
    print("[3].Multiplicação")
    print("[4].Divisão")
    print("[5].Sair\n")
    opcao = input("Selecione uma das opções pelo seu número: ")

    if opcao == "5":
        print("Você selecionou sair, até logo!")
        sys.exit()
    elif opcao not in ["1", "2", "3", "4","5"]:
            print("\nDigite uma opção válida.")

print("\nInsira abaixo os números para realizar a operação.\n")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Você deve digitar apenas números.")

while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Você deve digitar apenas números.")

if opcao == "1":
    print("\nVocê selecionou soma.\n")
    resultado = num1 + num2
    print(f"O Resultado da soma é: {resultado}\n")
elif opcao == "2":
    print("\nVocê selecionou subtração.\n")
    resultado = num1 - num2
    print(f"O Resultado da subtração é: {resultado}\n")
elif opcao == "3":
    print("\nVocê selecionou multiplicação.\n")
    resultado = num1 * num2
    print(f"O Resultado da multiplicação é: {resultado}\n")
elif opcao == "4":
    print("\nVocê selecionou divisão.\n")
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = num1 / num2
        print(f"O Resultado da divisão é: {resultado}\n")
else:
    print("Selecione uma opção válida.")