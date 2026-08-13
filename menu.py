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

        else:
            print("⚠ Opção inexistente! Tente novamente.")


menu()