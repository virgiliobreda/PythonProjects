def calculator():
    try:
        while True:
            print('\nEscolha entre: ')
            
            print('\n1 - Adição'
                '\n2 - Subtração'
                '\n3 - Multiplicação'
                '\n4 - Divisão'
                '\n5 - Encerrar')
            
            choice = int(input('\nDigite a opção desejada: '))

            if choice == 5: print('\nPrograma encerrado'); break
            
            if choice != 0 and choice < 6:
                n1 = float(input("\nDigite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))

            if choice == 1:
                print(f'\n{n1}+ {n2} = {n1 + n2}')
            elif choice == 2:
                print(f'\n{n1} - {n2} = {n1 - n2}')
            elif choice == 3:
                print(f'\n{n1} * {n2} = {n1 * n2}')
            elif choice == 4:
                print(f'\n{n1} / {n2} = {n1 / n2}')

            input("\nDigite qualquer tecla para continuar")
    except ZeroDivisionError:
        print(f"{n1} / {n2} = 0")
calculator()
    