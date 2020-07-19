palavra_secreta = input('Digite uma palavra para começar o jogo: ').strip().lower()
acertos = []
while True:
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
