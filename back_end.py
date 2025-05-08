"""
Funções utilizadas no sistema de concessionária de carros
"""
from front_end import show_conservation_subheader
from front_end import show_success_on_file_write
from front_end import show_cancel_new_car_entry
from front_end import show_high_price_subheader
from front_end import show_list_all_cars_header
from front_end import show_car_search_header
from front_end import show_new_car_summary
from front_end import show_new_car_header
from front_end import show_search_result
from front_end import show_menu_header
from front_end import show_error
from datetime import datetime
from pathlib import Path


#DEFINE O ARQUIVO DE BANCO DE DADOS
arquivo = Path('estoque_carros.txt')

anoMin = 1900   #Define o ano mínimo de fabricação do carro
#Pega o ano e o mês corrente para o teste de ano máximo de fabricação do carro válido
anoMax = datetime.today()       #Pega o datestamp atual
mes = anoMax                    #Pega o datestamp atual
anoMax = int(str(anoMax)[0:4])  #Separa apenas o ano atual e converte para inteiro
mes = int(str(mes)[5:7])        #Separa apenas o mês atual e converte para inteiro

#Se o mês for >= junho, o ano de fabricação pode ser o posterior ao atual
if mes >= 6:
    anoMax += 1

##FUNÇÃO COM RETORNO ADAPTÁVEL
#Realiza a checagem da informação inserida pelo usuário
def checaDados(tipo, informacao):
    if tipo == str:     #Se o tipo for string
        if informacao != '':    #Verifica se foi digitado algo
            return informacao   #Retorna a informação digitada
        else:                   #Se não foi digitado algo mostra mensagem
            show_error(1)
            return ''           #Retorna vazio
    elif tipo == int:   #Se o tipo for inteiro
        if informacao != '':    #Verifica se foi digitado algo
            try:                #Tenta...
                informacao = int(informacao)    #Converter para inteiro
            except ValueError:  #Se não conseguiu converter mostra mensagem
                show_error(2)
                return ''       #Retorna vazio
            else:               #Se conseguiu converter
                return informacao   #Retorna o número inteiro
        else:           #Se não foi digitado algo mostra mensagem
            show_error(1)
            return ''   #Retorna vazio
    elif tipo == float:     #Se o tipo for inteiro
        if informacao != '':    #Verifica se foi digitado algo
            try:                #Tenta...
                informacao = float(informacao)    #Converter para float
            except ValueError:  #Se não conseguiu converter mostra mensagem
                show_error(3)
                return ''       #Retorna vazio
            else:               #Se conseguiu converter
                return informacao   #Retorna o número real
        else:           #Se não foi digitado algo mostra mensagem
            show_error(1)
            return ''           #Retorna vazio


##FUNÇÃO SEM RETORNO - Grava as informações no arquivo
def gravaArquivo(dicCarro):
    if arquivo.exists():        #Verifica se o arquivo existe
        conteudoArquivo = arquivo.read_text()   #Faz a leitura do conteúdo atual do arquivo
        linha = ''              #Cria a variável para receber as informações do novo carro
        for chave, valor in dicCarro.items():   #Varre o dicionário do novo carro
            linha = linha + str(valor) + ','    #Adiciona cada valor na linha
            if chave == 'estado':               #Se a chave for a última
                linha = linha + '\n'            #Adiciona uma quebra de linha
        conteudoArquivo = conteudoArquivo + linha   #Adiciona a nova linha ao conteúdo já existente
        arquivo.write_text(conteudoArquivo)     #Grava no arquivo o conteúdo atualizado
        show_success_on_file_write()
    else:                       #Se o arquivo não existe
        linha = ''              #Cria a variável para receber as informações do novo carro
        for chave, valor in dicCarro.items():   #Varre o dicionário do novo carro
            linha = linha + str(valor) + ','    #Adiciona cada valor na linha
            if chave == 'estado':               #Se a chave for a última
                linha = linha + '\n'            #Adiciona uma quebra de linha
        arquivo.write_text(linha)               #Grava no arquivo o conteúdo da linha
        show_error(4)


##FUNÇÃO SEM RETORNO
#Solicita as informações do novo carro e as salva no arquivo
def cadastrar_carro():
    #Declara o dicionário do carro
    novoCarro = {'nome': str,
                 'preco': float,
                 'ano': int,
                 'estado': str}

    show_new_car_header()
    #Solicita as informações ao usuário e chama a função de checagem do tipo de dados.
    #Essa função verificará também se o campo ficou vazio. Se ficou vazio, a informação
    #será solicitada novamente até que o usuário insira a informação correta
    dadoInserido = checaDados(str, input('Nome do carro: '))
    while dadoInserido == '':
        dadoInserido = checaDados(str, input('Nome do carro: '))

    novoCarro['nome'] = dadoInserido

    dadoInserido = checaDados(float, input('Preço do carro: R$ '))
    while dadoInserido == '':
        dadoInserido = checaDados(float, input('Preço do carro: R$ '))

    novoCarro['preco'] = dadoInserido

    dadoInserido = checaDados(int, input('Ano do carro: '))
    #Verifica se o campo ficou vazio e se o ano informado é válido
    while (dadoInserido == '') or (dadoInserido < anoMin) or (dadoInserido > anoMax):
        if dadoInserido == '':  #Se o campo ficou vazio, não faz nada, pois já exibiu msg de erro
            pass
        elif dadoInserido < anoMin:   #Se o ano é inferior ao ano mínimo
            show_error(5)
        elif dadoInserido > anoMax:   #Se o ano é superior ao ano máximo
            show_error(6)
        dadoInserido = checaDados(int, input('Ano do carro: '))

    novoCarro['ano'] = dadoInserido

    dadoInserido = checaDados(str, input('Estado de conservação: '))
    while dadoInserido == '':
        dadoInserido = checaDados(str, input('Estado de conservação: '))

    novoCarro['estado'] = dadoInserido

    show_new_car_summary(novoCarro)
    #Solicita confirmação para gravar no arquivo
    if input('Gravar no arquivo (S/N)? ').upper() == 'S':
        gravaArquivo(novoCarro)  #Chama a função de gravação passando o dicionário do novo carro
    else:
        show_cancel_new_car_entry()


##FUNÇÃO COM RETORNO LISTA DE DICIONÁRIOS
#Realiza a busca conforme a informação inserida pelo usuário
def procurar_carro(tipoBusca=None):  #Se não houver parâmetro passado, o tipoBusca será = None
    if tipoBusca is None:   #Se tipoBusca = None (busca normal), mostra subtítulo
        show_car_search_header()
    #Bloco de verificação do arquivo. Se o arquivo não existir, mostra mensagem. Se o arquivo existir
    #faz a leitura e organiza os dados em lista de dicionários.
    if arquivo.exists() is False:   #Se o arquivo de BD NÃO existe
        show_error(7, arquivo)
        return                  #Retorna ao Menu Principal
    else:                       #Se o arquivo de BD existe
        #Declara a estrutura de dicionário para armazenar os carros
        dicCarro = {'nome': str,
                    'preco': float,
                    'ano': int,
                    'estado': str}
        conteudoArquivo = arquivo.read_text()   #Faz a leitura do conteúdo atual do arquivo
        conteudoArquivo = conteudoArquivo.replace(u'\n', '')    #Remove os \n
        item = ''               #Variável para armazenar cada item da lista
        qtdVirgula = 0          #Contador de vírgulas
        listaCarros = []        #Lista completa dos carros do arquivo
        for char in conteudoArquivo:    #Para cada caractere no conteúdo do arquivo
            if char != ',':             #Se o caractere NÃO for 'vírgula'
                item = item + char      #Adiciona o caractere no item
            else:                       #Se o caractere for 'vírgula'
                if qtdVirgula == 0:     #Se a qtd de vírgulas = 0, o item é o nome do carro
                    dicCarro['nome'] = item     #Adiciona o nome no dicionario
                    qtdVirgula += 1     #Incrementa a qtd de vírgulas
                    item = ''           #Zera o item
                elif qtdVirgula == 1:   #Se a qtd de vírgulas = 1, o item é o preço
                    dicCarro['preco'] = float(item)  #Adiciona o preço no dicionário (convertido para float)
                    qtdVirgula += 1     #Incrementa a qtd de vírgulas
                    item = ''           #Zera o item
                elif qtdVirgula == 2:   #Se a qtd de vírgulas = 2, o item é o ano
                    dicCarro['ano'] = int(item)     #Adiciona o ano no dicionario (convertido para inteiro)
                    qtdVirgula += 1     #Incrementa a qtd de vírgulas
                    item = ''           #Zera o item
                elif qtdVirgula == 3:   #Se a qtd de vírgulas = 3, o item é o estado de conservação
                    dicCarro['estado'] = item     #Adiciona o estado no dicionario
                    qtdVirgula = 0      #Zera a qtd de vírgulas
                    item = ''           #Zera o item
                    listaCarros.append(dicCarro.copy())  #Adiciona uma cópia do dicionário na lista de carros
                    dicCarro.clear()    #Zera o dicionário

    if tipoBusca == 'todos':    #Se tipoBusca = 'todos', significa listar todos os carros
        chaveBusca = 999999999999999.99     #Atribui um valor float imenso à chaveBusca
    else:                       #Se o tipoBusca = None (busca normal) pede a informação ao usuário
        chaveBusca = input('Informe o PREÇO MÁXIMO ou o ESTADO DE CONSERVAÇÃO para a busca: ')
        #Bloco que trata a input. Não pode ser vazio ou zero. Se tiver conteúdo numérico diferente de zero será
        #tratado como float (preço máximo). Se tiver conteúdo e não puder ser convertido para float, será tratado
        #como string (estado de conservação)
        if chaveBusca != '':        #Se a chave de busca NÃO é vazia
            try:                    #Tenta...
                chaveBusca = float(chaveBusca)  #Converter para float
            except ValueError:      #Se houver exceção
                pass                #Não faz nada
            else:                   #Se converteu...
                if chaveBusca == 0:  #Verifica se o valor é zero e mostra mensagem
                    show_error(8)
                    return          #Retorna ao Menu Principal
        else:                       #Se a chave de busca é vazia, mostra mensagem
            show_error(9)
            return                  #Retorna ao Menu Principal

    if type(chaveBusca) is float:   #Se a chave de busca for float
        if tipoBusca == 'todos':    #Se o tipoBusca = 'todos', mostra o subtítulo de listar todos os carros
            show_list_all_cars_header()
        else:                   #Se o tipoBusca = None, busca normal, subtítulo de busca por preço máximo
            show_high_price_subheader()
        listaExibir = []        #Lista do resultado da busca dos carros
        for item in listaCarros:    #Varre a lista completa de carros
            if item['preco'] <= chaveBusca:  #Verifica se o preço é <= ao preço do carro atual
                listaExibir.append(item)    #Adiciona o carro atual na lista de resultado da busca

        return show_search_result(listaExibir)  #Mostra o resultado da busca e retorna a lista de carros da busca
    else:   #Se a chave de busca for string
        show_conservation_subheader()
        listaExibir = []        #Lista do resultado da busca dos carros
        for item in listaCarros:    #Varre a lista completa de carros
            if item['estado'].lower() == chaveBusca.lower():  #Verifica se o estado é igual ao do carro atual
                listaExibir.append(item)    #Adiciona o carro atual na lista de resultado da busca

        return show_search_result(listaExibir)  #Mostra o resultado da busca e retorna a lista de carros da busca
