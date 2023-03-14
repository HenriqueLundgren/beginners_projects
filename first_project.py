import random  #importando o módulo

def computer_guess(x): #declarando a função que recebe o paramentro x
    low = 1
    high = x  #variavel que vai receber o parametro passado pelo programador
    feedback = '' #declarando a variavel feedback e já passando ela como string para receber o input do usuario
    while feedback != 'c':  #enquanto a entrada do usuario não for 'c' de correct, a interação continua
        if low != high:
            guess = random.randint(low, high)   #continua gerando numeros aleatorios entre 1 e parametro passado que nesse caso é x
        else:
            guess = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()  #recebe a resposta do usuario acerca do numero obtido pelo \
                                                                                             # computador
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'NICEEE! The computer guessed your number, {guess}, correctly!')

computer_guess(35)
