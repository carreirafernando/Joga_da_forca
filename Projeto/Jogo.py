import time
cor_vermelho_terminal = '\033[31m'
cor_vermelho_final = '\033[m'
acertos = []


def verificacao_inicial(entrada):
    if entrada in acertos:
        print(cor_vermelho_terminal, 'Você já digitou essa letra\n', cor_vermelho_final)
    elif not entrada.isalpha():
        print(cor_vermelho_terminal, 'Digite somente letras.\n', cor_vermelho_final)
    elif len(entrada) > 1:
        print(cor_vermelho_terminal, 'Digite apenas uma letra.\n', cor_vermelho_final)
    elif entrada == '':
        print(cor_vermelho_terminal, 'Precisa digitar algo.\n', cor_vermelho_final)
    else:
        return entrada


def verificacao_2(entrada_2):
    if entrada_2 in palavra_secreta:
        acertos.append(entrada_2)


def laco():
    palavra = ''
    for l in palavra_secreta:
        if l in acertos:
            time.sleep(0.2)
            print(f'{l.upper()}', end='')
            palavra += l
        else:
            time.sleep(0.2)
            print(' _ ', end='')
    return palavra


palavra_secreta = input('Vamos iniciar.... \nDigite a palavra secreta: ').strip().lower()
while True:
    letra = verificacao_inicial(input('\nDigite uma letra: '))
    if letra:
        verificacao_2(letra)
        if laco() == palavra_secreta:
            print('\nVocê venceu!!!\n')
            break
    else:
        continue
