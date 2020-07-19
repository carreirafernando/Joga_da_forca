palavra_secreta = input('Digite uma palavra para começar o jogo: ').strip().lower()
acertos = []
chances = 3
while True:
    if chances == 0:
        print('\nVocê perdeu....')
        break
    else:
        print(f'VOCÊ PODE ERRAR {chances}X')
        entrada = input('Digite uma letra: ').strip().lower()
        if not entrada.isalpha():
            print('\033[31mApenas letras...\033[m')
            continue
        elif len(entrada) > 1:
            print('\033[31mPor favor, Digite apenas UMA letra!\033[m')
            continue
        if entrada in acertos:
            print('Você já digitou esse letra!')
            continue
        else:
            if entrada in palavra_secreta:
                acertos.append(entrada)
                print(f'\033[92mA letra "{entrada.upper()}" tem na palavra.\033[m')
            else:
                print(f'A letra {entrada.upper()} não tem...')
                chances -= 1
        palavra = ''
        for letra in palavra_secreta:
            if letra in acertos:
                palavra += letra
                print(f'{letra}', end=' ')
            else:
                print('_', end=' ')
        if palavra_secreta == palavra:
            print('\nVocê acertou!!!')
            break
print('Até logo...')
