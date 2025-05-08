#DEFINIÇÃO DAS VARIÁVEIS DE AMBIENTE
linhasCLS = 30
tituloPrograma = 'Concessionária Santo Jovem'


##FUNÇÃO SEM RETORNO - Limpa a tela
def limpaTela(linhas):
    print('\n' * linhas)

##FUNÇÃO SEM RETORNO - Cabeçalho
def cabecalho(titulo):
    tamTitulo = len(titulo)
    print('=' * tamTitulo)
    print(titulo)
    print('=' * tamTitulo)
    print()

def show_main_header():
    limpaTela(linhasCLS)            #Chama a função que limpa a tela
    cabecalho(tituloPrograma)       #Chama a função que mostra o título    

def show_menu_header():
    print('MENU PRINCIPAL')
    print('--------------')

##FUNÇÃO COM RETORNO INTEIRO
#Mostra o Menu Principal e aguarda a opção do usuário
def mostraMenu(listaMenu):
    show_menu_header
    for item in listaMenu:      #Varre a lista de itens do Menu Principal
        print(f'{listaMenu.index(item) + 1} --> {item}')    #Mostra o índice e o item

    print()
    opMenu = input('Escolha uma opção: ')   #Aguarda a opção do usuário
    try:                        #Tenta...
        opMenu = int(opMenu)    #Converter para inteiro
    except ValueError:          #Se não conseguiu
        return -1               #Retorna -1
    else:                       #Se conseguiu converter
        return opMenu           #Retorna a opção do usuário

def show_end_program():
    limpaTela(linhasCLS)
    cabecalho(tituloPrograma)
    print('Sistema finalizado! Obrigado.\n\n')

def show_error(cod, file=None):
    if cod == 1:
        print('Esse campo não pode ficar em branco! Por favor, informe novamente.')
    elif cod == 2:
        print('Esse campo só aceita número inteiro! Por favor, informe novamente.')
    elif cod == 3:
        print('Esse campo só aceita número real! Por favor, informe novamente.')
    elif cod == 4:
        print()
        print('O arquivo de BD não existia e foi criado com sucesso!')
        input('Pressione ENTER para voltar ao Menu Principal...')
    elif cod == 5:
        print('O ano informado é anterior à existência de carros! Tente novamente.')
    elif cod == 6:
        print('O ano informado é superior ao ano atual. Tente novamente.')
    elif cod == 7:
        print(f'O arquivo de BD "{file}" não existe. Por favor, insira um novo carro.')
        print()
        input('Pressione ENTER para voltar...')
    elif cod == 8:
        print('O valor não pode ser ZERO! Por favor, tente novamente.')
        input('Pressione ENTER para voltar...')
    elif cod == 9:
        print('O campo de busca não pode ser vazio! Por favor, tente novamente.')
        input('Pressione ENTER para voltar...')
    elif cod == 10:
        print('Opção inválida!')
        input('Pressione ENTER para tentar novamente...')        


def show_success_on_file_write():
    print()
    print('Arquivo gravado com sucesso!')
    input('Pressione ENTER para voltar ao Menu Principal...')

def show_new_car_header():
    print('Cadastrar novo carro')
    print('--------------------')
    print()
    print('Por favor, insira todas as informações:')
    print()

def show_new_car_summary(info_new_car):
    print()
    print('As informações inseridas para o novo carro foram:')
    #Mostra o resumo das informações inseridas
    for chave, valor in info_new_car.items():
        print(f'{chave.capitalize()} - {str(valor).upper()}')
    print()

def show_cancel_new_car_entry():
    print()
    print('Informações descartadas!')
    print()
    input('Pressione ENTER para voltar ao Menu Principal...')    

def show_car_search_header():
    print('Buscar carro no estoque')
    print('-----------------------')
    print()

def show_list_all_cars_header():
    print('LISTANDO TODOS OS CARROS DO ESTOQUE:')
    print('------------------------------------')

def show_high_price_subheader():
    print()
    print('Busca por PREÇO MÁXIMO:')
    print('-----------------------')    

def show_conservation_subheader():
    print()
    print('Busca por ESTADO DE CONSERVAÇÃO:')
    print('--------------------------------')    


def show_search_result(result_list):
    tamListaExibir = len(result_list)   #Pega o tamanho da lista de resultado de busca
    if tamListaExibir > 0:  #Se a lista de resultado da busca tiver algum resultado
        #Bloco de configuração para exibição em modo tabela
        tamColunas = [25, 14, 16, 30]   #Define o tamanho das colunas
        col0 = 'NOME DO CARRO'  #Título da coluna 1
        col1 = 'PREÇO'          #Título da coluna 2
        col2 = 'ANO FABRICAÇÃO'  #Título da coluna 3
        col3 = 'ESTADO DE CONSERVAÇÃO'  #Título da coluna 4
        #Concatena todas as informações do título da tabela centralizado de acordo com o tam das colunas
        tituloTabela = (col0.center(tamColunas[0]) +
                       col1.center(tamColunas[1]) +
                       col2.center(tamColunas[2]) +
                       col3.center(tamColunas[3]))
        print(tituloTabela)     #Mostra o título da tabela
        print('-' * sum(tamColunas))    #Mostra o sublinhado do título da tabela de acordo com o tam do título
        for item in result_list:    #Para cada carro na lista de resultado
            #Concatena em uma linha todas as informações do carro
            linha = (item['nome'].center(tamColunas[0]) +
                     str(item['preco']).center(tamColunas[1]) +
                     str(item['ano']).center(tamColunas[2]) +
                     item['estado'].center(tamColunas[3]))
            print(linha)    #Mostra a linha com todas as informações do carro
        print()
        input('Pressione ENTER para voltar...')
    else:   #Se nenhum resultado foi encontrado, mostra mensagem...
        print()
        print('Carro não encontrado!')
        print()
        input('Pressione ENTER para voltar...')
        return  #Retorna ao Menu Principal
    return result_list  #Retorna a lista de carros da busca










