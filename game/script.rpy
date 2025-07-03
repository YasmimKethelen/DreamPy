define professor_frank = Character("Professor Frank", color="#3477eb")
define android_giba = Character("GIBA",  color="#34d8eb")
define usuario = Character("[nomeusuario]", color="#9f34eb")

label start:

    $ nomeusuario = renpy.input("Insira seu nome:")


    scene bg classroom
    with fade

    show professor frank at Transform(xalign=0.5, yalign=-2.5, zoom=0.75)
    professor_frank "Muito bem, turma. Atenção, por favor."
    professor_frank "Como vocês sabem, a prova final está se aproximando."

    show professor frank at Transform(xalign=0.5, yalign=-2.5, zoom=0.75)
    professor_frank "O conteúdo será lógica de programação e estruturas condicionais."

    hide professor frank with dissolve


    usuario "Lógica de programação... estruturas condicionais..."
    usuario "Ainda tenho muito o que revisar..."

    play sound "school_bell.ogg"

    usuario "Preciso me preparar. Não posso falhar dessa vez."

    scene bg biblioteca
    with fade

    play music "study_ambience.ogg" loop

    usuario "Preciso revisar mais... Só mais um pouco..."

    play sound "page_flip.ogg"
    pause 0.1
    play sound "glitch.ogg"

    scene black with pixellate
    play sound "glitch_explosion.ogg"

    usuario "O que... está... acontecendo?"

    pause 0.1

    scene bg cyber_city_dark
    with fade

    play music "cyber_ambience.ogg" loop

    usuario "Que lugar é esse?"

    show android giba at Transform(xalign=0.5, yalign=0.98, zoom=0.75)
    android_giba "Bem-vindo, %(nomeusuario)s."
    android_giba "Estava esperando por você."
    usuario "O quê? Quem é você?"
    android_giba "Eu sou GIBA — Guardião Integrado de Bases Avançadas."
    android_giba "O código pode ter me criado, mas sou eu quem o comanda."
    android_giba "Antes de revelar mais, preciso ter certeza de que você está preparado."
    android_giba "O teste começa agora."


    jump basic_quiz


label basic_quiz:

    $ score = 0
    show screen score_display
    show android giba at Transform(xalign=0.9, yalign=0.98, zoom=0.75)

    menu:
        "Qual dessas estruturas é usada para repetir um bloco de código várias vezes em Python?"
        "a) if":
            pass
        "b) while":
            $ score += 1
        "c) def":
            pass
        "d) try":
            pass

    menu:
        "Qual função embutida converte uma string para um número inteiro em Python?"
        "a) int()":
            $ score += 1
        "b) str()":
            pass
        "c) float()":
            pass
        "d) bool()":
            pass

    menu:
        "O que este código imprime?\nx = [1, 2, 3]\nprint(x[1])"
        "a) 1":
            pass
        "b) 2":
            $ score += 1
        "c) 3":
            pass
        "d) Erro":
            pass

    menu:
        "Qual das alternativas cria uma função em Python?"
        "a) def minha_funcao():":
            $ score += 1
        "b) func minha_funcao():":
            pass
        "c) create function minha_funcao():":
            pass
        "d) function minha_funcao():":
            pass

    menu:
        "O que significa o operador == em Python?"
        "a) Atribuição de valor":
            pass
        "b) Comparação de identidade":
            pass
        "c) Comparação de igualdade":
            $ score += 1
        "d) Nenhuma das anteriores":
            pass

    if score == 5:
        jump perfect_basic
    else:
        jump fail_basic


label perfect_basic:

    play sound "city_pulse.ogg"


    show android giba at center
    android_giba "Você passou."
    android_giba "Mas há mais... Está pronto para um desafio mais avançado, %(nomeusuario)s?"
    hide screen score_display

    menu:
        "Sim. Quero continuar.":
            jump advanced_quiz
        "Não. Preciso voltar.":
            jump wakeup_good


label fail_basic:

    play sound "city_corrupt.ogg"


    show android giba at center
    android_giba "Você ainda não está pronto. Mas o código espera..."
    hide screen score_display

    scene black with pixellate
    play sound "static_breathing.ogg"

    scene bg biblioteca with pixellate
    play sound "heartbeat.ogg"

    usuario "Nossa! Que sonho estranho... preciso voltar a estudar."

    return


label advanced_quiz:

    $ score_adv = 0
    show screen score_display2
    show android giba at Transform(xalign=0.9, yalign=0.98, zoom=0.75)


    menu:
        "O que este código imprime?\ndef funcao(a, b=2):\n    return a * b\nprint(funcao(3))"
        "a) 3":
            pass
        "b) 6":
            $ score_adv += 1
        "c) 5":
            pass
        "d) Erro":
            pass

    menu:
        "Qual dessas estruturas é imutável em Python?"
        "a) list":
            pass
        "b) set":
            pass
        "c) tuple":
            $ score_adv += 1
        "d) dict":
            pass

    menu:
        "O que significa o erro IndentationError em Python?"
        "a) Nome de variável inválido":
            pass
        "b) Espaçamento incorreto no código":
            $ score_adv += 1
        "c) Parênteses não fechados":
            pass
        "d) Função não definida":
            pass

    menu:
        "O que o operador 'in' faz em Python?"
        "a) Cria um loop":
            pass
        "b) Compara igualdade":
            pass
        "c) Verifica se um valor está presente em uma sequência":
            $ score_adv += 1
        "d) Define uma variável":
            pass

    menu:
        "Qual é o resultado de len(\"Python\")?"
        "a) 5":
            pass
        "b) 6":
            $ score_adv += 1
        "c) 7":
            pass
        "d) Erro":
            pass

    if score_adv == 5:
        jump perfect_advanced
    else:
        jump fail_advanced


label perfect_advanced:
    show android giba at center
    play sound "final_glitch.ogg"
    android_giba "Você domina os fundamentos! Mas agora não poderemos prosseguir."
    hide screen score_display2
    android_giba "E não se preocupe, %(nomeusuario)s. Irá se sair bem na sua prova!"
    hide android giba
    show happy_giba at Transform(xalign=0.5, yalign=0.98, zoom=0.62)
    usuario "Prova? Como você sa-"
    scene black with pixellate
    scene bg biblioteca with pixellate
    play sound "mysterious_echo.ogg"
    usuario "-be sobre a minha prova?"
    usuario "Caramba! Isso foi só um sonho?!"
    usuario "De qualquer forma... Me sinto muito mais confiante do que antes!"

    return

label fail_advanced:
    show android giba at center
    play sound "final_glitch.ogg"
    android_giba "Você está quase lá! Não desanime agora."
    hide screen score_display2
    android_giba "Irei aguardar o seu retorno."
    hide android giba
    show happy_giba at Transform(xalign=0.5, yalign=0.98, zoom=0.62)
    usuario "Retorno?"
    scene black with pixellate
    scene bg biblioteca with pixellate
    play sound "mysterious_echo.ogg"
    usuario "Caramba! Isso foi um sonho?!"
    usuario "De qualquer forma... Me sinto  mais confiante do que antes!"

    return

label wakeup_good:
    scene black with pixellate
    scene bg biblioteca with pixellate
    play sound "mysterious_echo.ogg"

    usuario "Caramba isso foi um sonho?!"
    usuario "De qualquer forma... Me sinto um pouco mais confiante que antes!"

    return
