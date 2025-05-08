"""
Sistema de controle de loja de carros

Desenvolvido por Bruno Faria - Grupo DEV Carlo Acutis

Python 3.12 - IDE VSCode

Em 08/05/2025.
"""
#Importa as funções a serem utilizadas
from front_end import limpaTela, cabecalho, mostraMenu
from front_end import show_error, show_end_program
from front_end import show_main_header
from back_end import cadastrar_carro, procurar_carro

#Itens do Menu Principal
itensMenu = ['Cadastrar carro', 'Buscar carro', 'Listar todos os carros', 'Finalizar sistema']

show_main_header()
opMenu = mostraMenu(itensMenu)  #Chama o Menu principal e armazena o retorno
while opMenu != (itensMenu.index('Finalizar sistema') + 1):  #Repete Enquanto o retorno do
                        #Menu Principal for diferente do índice de 'Finalizar sistema' + 1
    if opMenu == (itensMenu.index('Cadastrar carro') + 1):
        show_main_header()
        cadastrar_carro()       #Chama a função que cadastra um novo carro
    elif opMenu == (itensMenu.index('Buscar carro') + 1):
        show_main_header()
        procurar_carro()        #Chama a função de busca
    elif opMenu == (itensMenu.index('Listar todos os carros') + 1):
        show_main_header()
        procurar_carro('todos')  # Chama a função de busca para listagem de todos os carros
    elif opMenu == (itensMenu.index('Finalizar sistema') + 1):
        pass                    #Se o usuário escolheu finalizar o sistema, não entrará novamente no while
    else:                       #Se o usuário digitou opção inválida (letra ou outro número que não existe no menu)
        show_error(10)

    show_main_header()
    opMenu = mostraMenu(itensMenu)  #Mostra novamente o Menu Principal e aguarda a opção do usuário

show_end_program()
exit(0)
