from problemas import*
from problemas2 import*
import os
while True:

    print("+"+"="*48+"+")
    print("|I"+" "*17+"\"Bem Vindo\""+" "*17+" I|")
    print("+"+"="*48+"+")
    print("Informe o número da operação que você deseja:")
    print("""
|I Verificar Números digite >> 1
|I Calcular Média digite >> 2
|I Verificar ano Bissexto digite >> 3
|I Converter Nota para Letra digite >> 4
|I Verificar se número é divisivel digite >> 5
|I Encontra maior número digite >> 6
|I Verificar quadrado perfeito digite >> 7
|I Classificar números digite >> 8
|I Verificar números multiplos digite >> 9
|I Verificar Palindromo digite >> 10
|I Coverter Temperatura digite >> 11
|I Verificar Divisibilidade digite >> 12
|I Calcular área do triangulo digite >> 13
|I Calcular número de Armstrong digite >> 14
|I Verificar Potencia de 2 digite >> 15
|I Calcular Valor absoluto digite >> 16
|I Verificar triangulo retangulo digite >> 17
|I Determinar raizes digite >> 18
|I Calcular raiz cubica digite >> 19
|I Calcular desconto digite >> 20
|I Classificar numeros digite >> 21
|I Calcular area do circulo digite >> 22
|I Calcular produto escalar digite >> 23
|I Calcular media ponderada digite >> 24
|I Calcular raiz quadrada digite >> 25
|I Sequencia fibonnacci digite >> 26
|I Verificar Triangulo equilatero digite >> 27
|I Feature 30 digite >> 28
|I Feature 31 digite >> 29
|I Feature 32 digite >> 30
|I Feature 33 digite >> 31
|I Feature 34 digite >> 32
|I Feature 35 digite >> 33
|I Feature 36 digite >> 34
|I Feature 37 digite >> 35
|I Feature 38 digite >> 36
|I Feature 39 digite >> 37
|I Feature 40 digite >> 38
|I Feature 41 digite >> 39
|I Feature 42 digite >> 40
|I Feature 43 digite >> 41
|I Feature 44 digite >> 42
|I Feature 45 digite >> 43
|I Feature 46 digite >> 44
|I Feature 47 digite >> 45
|I Feature 48 digite >> 46
|I Feature 49 digite >> 47
|I Feature 50 digite >> 48
|I Feature 51 digite >> 49
|I Feature 52 digite >> 50
|I Feature 53 digite >> 51
|I Feature 54 digite >> 52
|I Feature 55 digite >> 53
|I Tabuada digite >> 54
    """)
    print(">------Digite o número da função------<")
    funcao = int(input(">> "))
    if funcao == 1:
        verificar_numero()
    elif funcao == 2:
        calcular_media()
    elif funcao == 3:
        verificar_ano_bissexto()
    elif funcao == 4:
        converter_nota_letra()
    elif funcao == 5:
        verificar_divisivel()
    elif funcao == 6:
        encontrar_maior()
    elif funcao == 7:
        verificar_quadrado_perfeito()
    elif funcao == 8:
        classificar_numeros()
    elif funcao == 9:
        verificar_multiplo()
    elif funcao == 10:
        verificar_palindromo()
    elif funcao == 11:
        converter_temperatura()
    elif funcao == 12:
        verificar_divisibilidade()
    elif funcao == 13:
        calcular_area_triangulo()
    elif funcao == 14:
        verificar_numero_armstrong()
    elif funcao == 15:
        verificar_potencia_de_2()
    elif funcao == 16:
        calcular_valor_absoluto()
    elif funcao == 17:
        verificar_triangulo_retangulo()
    elif funcao == 18:
        determinar_raizes()
    elif funcao == 19:
        calcular_raiz_cubica()
    elif funcao == 20:
        calcular_desconto()
    elif funcao == 21:
        classificar_numeros()
    elif funcao == 22:
        calcular_area_circulo()
    elif funcao == 23:
        calcular_produto_escalar()
    elif funcao == 24:
        calcular_media_ponderada()
    elif funcao == 25:
        calcular_raiz_quadrada()
    elif funcao == 26:
        sequencia_fibonnacci()
    elif funcao == 27:
        verificar_triangulo_equilatero()
    elif funcao == 28:
        feature30()
    elif funcao == 29:
        feature31()
    elif funcao == 30:
        feature32()
    elif funcao == 31:
        feature33()
    elif funcao == 32:
        feature34()
    elif funcao == 33:
        feature35()
    elif funcao == 34:
        feature36()
    elif funcao == 35:
        feature37()
    elif funcao == 36:
        feature38()
    elif funcao == 37:
        feature39()
    elif funcao == 38:
        feature40()
    elif funcao == 39:
        feature41()
    elif funcao == 40:
        feature42()
    elif funcao == 41:
        feature43()
    elif funcao == 42:
        feature44()
    elif funcao == 43:
        feature45()
    elif funcao == 44:
        feature46()
    elif funcao == 45:
        feature47()
    elif funcao == 46:
        feature48()
    elif funcao == 47:
        feature49()
    elif funcao == 48:
        feature50()
    elif funcao == 49:
        feature51()
    elif funcao == 50:
        feature52()
    elif funcao == 51:
        feature53()
    elif funcao == 52:
        feature54()
    elif funcao == 53:
        feature55()
    elif funcao == 54:
        tabuada()
    os.system("pause")
    os.system("cls")