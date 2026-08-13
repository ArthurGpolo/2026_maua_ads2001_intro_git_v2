import calculadora


def menu():
    while True:
        print("\nMENU:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if not opcao.isdigit():
            print("⚠ Entrada inválida! Digite apenas números.")
            continue

        opcao = int(opcao)

        if opcao == 0:
            print("Saindo...")
            break

        if opcao in (1, 2, 3, 4):
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            except ValueError:
                print("⚠ Digite números válidos.")
                continue

            if opcao == 1:
                resultado = calculadora.somar(a, b)

            print(f"Resultado: {resultado}")

        else:
            print("⚠ Opção inexistente! Tente novamente.")


menu()