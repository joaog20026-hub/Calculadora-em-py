print("CALCULADORA EM PYTHON")
print("---------------------")

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma operação: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = numero1 + numero2
    print("\nResultado:", numero1, "+", numero2, "=", resultado)

elif opcao == "2":
    resultado = numero1 - numero2
    print("\nResultado:", numero1, "-", numero2, "=", resultado)

elif opcao == "3":
    resultado = numero1 * numero2
    print("\nResultado:", numero1, "*", numero2, "=", resultado)

elif opcao == "4":
    if numero2 == 0:
        print("\nErro: divisão por zero não é permitida.")
    else:
        resultado = numero1 / numero2
        print("\nResultado:", numero1, "/", numero2, "=", resultado)

else:
    print("\nOpção inválida.")
