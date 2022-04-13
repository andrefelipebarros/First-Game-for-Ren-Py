# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

 #images de fundo

image fundo = "images/backgrounds/quarto.jpg"



#personagem sem nome

define n = Character("Narrador")

#personagens principais

define a = Character("André",image="/images/André")

define j = Character("Nadruz")


#image narrador

image Narrador = "images/Narrador.png"

#imagens efeitos

image Ideia = "images/lampada.png"


#images André

image Andre sorrindo = "images/André/Andre sorrindo.png"

image André sorrindo olho fechado = "images/André/André sorrindo olho fechado.png"

image André sorrindo imaginando um abraço = "images/André/André sorrindo imaginando um abraço.png"

image André olhando para cima sorrindo = "images/André/abraçado olhando para cima sorrindo.png"

image André Dúvida = "images/André/André Dúvida.png"

image André Nervoso = "images/André/André Nervoso.png"

image André Nervoso 2 = "images/André/André Nervoso 2.png"

image André Ansioso = "images/André/André Ansioso.png"

image André pensou em comer = "images/André/André pensou em comer.png"




#imagens Nadruz





# The game starts here.

label start:

    a "O Começo de tudo foi muito Louco."
    
    n "em 2020..."

    with dissolve
    scene fundo
    
    show Andre sorrindo at center:

    

    a "Ta chegando meu aniversário XD"
    hide Andre sorrindo
    show André sorrindo olho fechado at center:

    a "como faço aniversário no dia 2 de fevereiro"
    a "irei postar no meu status, que quem me mandar mensagem"

    show André sorrindo imaginando um abraço at center

    a "as 20:20 darei um mega abraço na pessoa (queria se sentir importante)"
   
    hide André sorrindo imaginando um abraço
    with dissolve

    n "André está animado para as mensagens que irá receber..."
    
    n "Horas depois..."
   
    show André Dúvida at center:

    a "poxa ta chegando a hora... será que receberei alguma mensagem?"

    show André Nervoso at center:

    a "..."
    
    show André Nervoso 2 at center:

    a "....."

    show André Ansioso at center:

    a "HAAAAAAAAAAA EU TO ANSIOSOOOOOOOOO..."
    show Ideia at center:
        zoom -0.04
        yalign 0.07


    show André pensou em comer at center:

    a "Vou aproveitar e comer alguma coisa, já que falta 20 minutos"
    hide Ideia
    hide André pensou em comer
    with dissolve

    #show dele dormindo
    
    n "André acabou dormindo..."

    n "Assim que acordou"

    #show

    a "ME RESPONDERAMM HHAAAAAA"

    a "Pera... foi somente o meu Pai querendo abraço..."

    a "Que coisa chata, ninguém quer um abraço meu."

    a "Vou voltar a dormir"



    # This ends the game.

    return
