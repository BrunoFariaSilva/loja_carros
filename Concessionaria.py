"""
Sistema de controle de loja de carros

Desenvolvido por Bruno Faria - Grupo DEV Carlo Acutis

Python 3.12 - IDE PyCharm

Em 12/12/2024.
"""
#Importa as funções a serem utilizadas
from funcoes import limpaTela, cabecalho, mostraMenu
from funcoes import cadastrar_carro, procurar_carro

#DEFINIÇÃO DAS VARIÁVEIS DE AMBIENTE
linhasCLS = 30
tituloPrograma = 'Concessionária Santo Jovem'
#Itens do Menu Principal
itensMenu = ['Cadastrar carro', 'Buscar carro', 'Listar todos os carros', 'Finalizar sistema']

limpaTela(linhasCLS)            #Chama a função que limpa a tela
cabecalho(tituloPrograma)       #Chama a função que mostra o título
opMenu = mostraMenu(itensMenu)  #Chama o Menu principal e armazena o retorno
while opMenu != (itensMenu.index('Finalizar sistema') + 1):  #Repete Enquanto o retorno do
                        #Menu Principal for diferente do índice de 'Finalizar sistema' + 1
    if opMenu == (itensMenu.index('Cadastrar carro') + 1):
        limpaTela(linhasCLS)
        cabecalho(tituloPrograma)
        cadastrar_carro()       #Chama a função que cadastra um novo carro
    elif opMenu == (itensMenu.index('Buscar carro') + 1):
        limpaTela(linhasCLS)
        cabecalho(tituloPrograma)
        procurar_carro()        #Chama a função de busca
    elif opMenu == (itensMenu.index('Listar todos os carros') + 1):
        limpaTela(linhasCLS)
        cabecalho(tituloPrograma)
        procurar_carro('todos')  # Chama a função de busca para listagem de todos os carros
    elif opMenu == (itensMenu.index('Finalizar sistema') + 1):
        pass                    #Se o usuário escolheu finalizar o sistema, não entrará novamente no while
    else:                       #Se o usuário digitou opção inválida (letra ou outro número que não existe no menu)
        print('Opção inválida!')
        input('Pressione ENTER para tentar novamente...')

    limpaTela(linhasCLS)
    cabecalho(tituloPrograma)
    opMenu = mostraMenu(itensMenu)  #Mostra novamente o Menu Principal e aguarda a opção do usuário

limpaTela(linhasCLS)
cabecalho(tituloPrograma)
print('Sistema finalizado! Obrigado.')
exit(0)
