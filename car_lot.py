"""
Loja de carros

Programa desenvolvido pelo Grupo DEV Carlo Acutis - Bruno Faria

brunofariasilva@gmail.com
08/05/2025

-------

Problemas conhecidos:
1 - Erro caso os argumentos não sejam passados exatamente como se espera. O
    tratamento destes erros ainda não foi implementado.
2 - A leitura do resultado das buscas fica prejudicada, caso a listagem fique extensa.
3 - Falta mostrar o resumo do novo carro adicionado e pedir a confirmação da gravação.
4 - A palavra de busca (no caso de busca por estado de conservação) necessita ser exata
    à que está gravada no banco de dados.
"""

from pathlib import Path
import json
import sys

program_filename = 'car_lot.py'  #Nome do programa para exibição no "help"
db_cars_filepath = 'estoque_carros.json'  #Arquivo de banco de dados

class File():                   #Classe para operações com arquivos
    def __init__(self, path):   #Inicialização da classe
        self.path = Path(path)  #Caminho e nome do arquivo
    
    def _file_exists(self):     #Método que verifica se o arquivo existe
        if self.path.exists():
            return True

    def _initialize_json(self):  #Método que inicializa o arquivo json caso ele não exista
        self.dict = {"cars": []}  #Dicionário vazio
        with open(self.path, 'w', newline='\n') as file_to_save:
            json.dump(self.dict, file_to_save, indent=4)  #Salva o dicionário vazio no arquivo

    def _create_file(self):     #Método para criação do arquivo json, caso não exista
        Path.touch(self.path, mode=0o777, exist_ok=False)  #Cria o arquivo
        self._initialize_json()  #Inicializa o arquivo

    def _read_file(self):       #Método para leitura do arquivo
        if not self._file_exists():  #Se o arquivo não existir
            self._create_file()  #Chama o método de criação do arquivo
        with open(self.path, 'r', newline='\n') as file_to_read:
            file_contents = json.load(file_to_read)  #Abre o arquivo e lê o conteúdo
        return file_contents    #Retorna o conteúdo do arquivo
    
    def _get_content_list(self):  #Método para recuperar o conteúdo do arquivo em lista
        content = self._read_file()  #Lê o conteúdo do arquivo
        return content['cars']  #Retorna apenas o conteúdo em lista

    def _save_file(self, dict_to_save):  #Método para salvar o arquivo
        with open(self.path, 'w', newline='\n') as file_to_save:
            json.dump(dict_to_save, file_to_save, indent=4)  #Salva o dicionário completo no arquivo


class Car:                      #Classe para operações com carros
    def __init__(self, name, year, price, condition):  #Inicialização da classe
        self.name = name        #Nome do carro
        self.year = year        #Ano de fabricação
        self.price = price      #Preço
        self.condition = condition  #Estado de conservação

        self.db_cars_contents = File(db_cars_filepath)  #Inicializa o arquivo de banco de dados
        self.car_stock = self.db_cars_contents._read_file()  #Recupera o conteúdo do arquivo

    def _save_new_car(self):    #Método que grava um novo carro no estoque
        new_car_to_save_dict = {'name': self.name,  #Dicionário com os atributos do carro
                        'year': self.year,
                        'price': self.price,
                        'condition': self.condition}
        self.car_stock['cars'].append(new_car_to_save_dict)  #Adiciona o novo carro no estoque
        self.db_cars_contents._save_file(self.car_stock)  #Salva o arquivo
        print('\nCarro adicionado ao estoque com sucesso!\n')


def __check_inputs(to_new_car_dict):  #Função para validação das inputs de novo carro
    len_args = len(to_new_car_dict)        #Pega a quantidade de argumentos
    if len_args < 4:
        return False
    else:
        return True


def __show_search_result(list_to_show):  #Função que mostra lista de carros
    print(f'\n{len(list_to_show)} carro(s) encontrado(s):')
    for item in list_to_show:   #Para cada item na lista, mostra os detalhes
        print(f'Carro:\t{item['name']}')
        print(f'Ano:\t{item['year']}')
        print(f'Preço:\t{item['price']}')
        print(f'Estado:\t{item['condition']}\n')


def __search_car(search_info):  #Função para busca de carros
    def _search_by_price(price):  #Subfunção que busca por preço
        car_stock_content = File(db_cars_filepath)  #Leitura do arquivo
        car_stock = car_stock_content._get_content_list()  #Recupera o conteúdo em lista
        if car_stock:           #Se existir carro no estoque
            search_result = []  #Nova lista para resultado da busca
            for car in car_stock:  #Para cada carro no estoque
                if float(car['price']) <= price:  #Compara os preços
                    search_result.append(car)  #Adiciona o carro na lista de resultados
            return search_result  #Retorna a lista de resultados
        else:                   #Se não existir carro no estoque
            print('\nNenhum carro encontrado no estoque!\n')
            return 0            #Retorna zero
                

    def _search_by_condition(condition):  #Subfunção que busca por estado de conservação
        car_stock_content = File(db_cars_filepath)  #Leitura do arquivo
        car_stock = car_stock_content._get_content_list()  #Recupera o conteúdo em lista
        if car_stock:           #Se existir carro no estoque
            search_result = []  #Nova lista para resultado da busca
            for car in car_stock:  #Para cada carro no estoque
                if car['condition'] == condition:  #Compara o estado de conservação
                    search_result.append(car)  #Adiciona o carro na lista de resultados
            return search_result  #Retorna a lista de resultados
        else:                   #Se não existir carro no estoque
            print('\nNenhum carro encontrado no estoque!\n')
            return 0            #Retorna zero

    try:                        #Tenta...
        price = float(search_info)  #Converter para float
    except ValueError:          #Caso haja exceção, a busca é por estado de conservação
        search_result = _search_by_condition(search_info)  #Chama a função de busca
        if search_result:       #Se existir resultado na busca
            __show_search_result(search_result)  #Mostra o resultado
        else:                   #Se não existir resultado na busca
            print('\nNenhum carro encontrado para a busca realizada! Tente novamente.\n')
    else:                       #Se conseguiu converter, a busca é por preço
        search_result = _search_by_price(price)  #Chama a função de busca
        if search_result:       #Se existir resultado na busca
            __show_search_result(search_result)  #Mostra o resultado
        else:                   #Se não existir resultado na busca
            print('\nNenhum carro encontrado para a busca realizada! Tente novamente.\n')


def __list_all_cars():          #Função que lista todos os carros
    car_stock_content = File(db_cars_filepath)  #Leitura do arquivo
    car_stock = car_stock_content._get_content_list()  #Recupera o conteúdo em lista
    if car_stock:               #Se existir carro no estoque
        all_cars = []           #Nova lista para salvar todos os carros
        for car in car_stock:   #Para cada carro no estoque
            all_cars.append(car)  #Adiciona o carro na lista
        
        __show_search_result(all_cars)  #Mostra a lista de carros
    else:                       #Se não existir carro no estoque
        print('\nNenhum carro encontrado no estoque!\n')


def __show_usage_info():        #Função "help" caso o programa não seja chamado corretamente
    print(f'\nUsage: {program_filename} <operation> <options>')
    print('\nOperations:\tnewcar\t\tInsert new car to stock')
    print('\t\tsearch\t\tSearch for a car by price or condition')
    print('\t\tlistall\t\tList all cars in stock\n\n')
    print('To insert a new car, enter the argument below:')
    print(f'{program_filename} newcar <car_name> <fabrication_year> <price> <condition>')
    print(f'Exemple: {program_filename} Corolla 2010 35000 Seminovo\n')
    print('For a search, use the PRICE or CONDITION as a key, one at once')
    print(f'Exemple: {program_filename} search <price> or <condition>\n')
    print('To list all cars in stock, use <listall> argument')
    print(f'Exemple: {program_filename} listall\n\n')    


def __main():                   #Função principal
    valid_args = ['newcar', 'search', 'listall', 'help']  #Lista dos argumentos válidos
    args = sys.argv             #Variável recebe todos os argumentos
    args.pop(0)                 #Descarta o nome do programa
    if (not args) or (args[0] not in valid_args):  #Se não existir argumentos ou
                    #o que existir não estiver na lista de argumentos válidos
        __show_usage_info()     #Mostra a forma correta de uso do programa
    else:                       #Se existe argumento válido
        if args[0] == 'newcar':  #Se o argumento é para novo carro
            if __check_inputs(args[1:]):  #Verifica as inputs para o novo carro (não implementado)
                new_car = Car(name=args[1], year=args[2], price=args[3], condition=args[4])  #Cria
                    #uma instância de carro (Car) passando os argumentos
                new_car._save_new_car()  #Salva o novo carro no banco de dados
            else:               #Se as inputs estão incorretas ou faltantes
                print('\nPlease check inputs and try again!\n')
                __show_usage_info()  #Mostra a forma correta de uso do programa


        elif args[0] == 'search':  #Se o argumento é para busca
            __search_car(args[1])  #Chama a função de busca passando a input

        elif args[0] == 'listall':  #Se o argumento é para listagem completa
            __list_all_cars()   #Chama a função que mostra todos os carros
        
        elif args[0] == 'help':
            __show_usage_info()  #Mostra a forma correta de uso do programa


if __name__ == "__main__":
    __main()
