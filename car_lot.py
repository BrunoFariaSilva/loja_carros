"""
Loja de carros

Programa desenvolvido pelo Grupo DEV Carlo Acutis - Bruno Faria

brunofariasilva@gmail.com
08/05/2025

-------

Problemas conhecidos:
1 - A leitura do resultado das buscas fica prejudicada, caso a listagem fique extensa.
2 - Separar módulos
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
        self.empty_dict = {"cars": []}  #Dicionário vazio
        with open(self.path, 'w', newline='\n') as file_to_save:
            json.dump(self.empty_dict, file_to_save, indent=4)  #Salva o dicionário vazio no arquivo

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


class Dao:                      #Classe para interação com arquivos
    def __init__(self):         #Inicialização da classe
        self.db_cars_contents = File(db_cars_filepath)  #Inicializa o arquivo de banco de dados
        self._init_cars_db()    #Chama o método de inicialização do banco de dados
    
    def _init_cars_db(self):    #Método para inicialização do banco de dados
        self.car_stock = self.db_cars_contents._read_file()  #Recupera o conteúdo do arquivo
    
    def save_new_car_to_db(self, car_dict):  #Método para salvar o novo carro no banco de dados
        self.car_stock['cars'].append(car_dict)   #Adiciona o novo carro no estoque
        self.db_cars_contents._save_file(self.car_stock)  #Salva o arquivo
   

class Car:                      #Classe para operações com carros
    def __init__(self, initial_args):  #Inicialização da classe
        if self._validate_args_atributes(initial_args):  #Validação dos argumentos
            self.dao_conn = Dao()  #Inicialização do banco de dados

    def _validate_args_atributes(self, args):  #Método para validação dos argumentos
        if len(args) >= 4:      #Verifica se existem pelo menos 4 argumentos
            name, year, price, condition = args[0], args[1], args[2], ' '.join(args[3:])  #Atribui às
                                                                    #variáveis os argumentos passados
            if check_is_a_float(year) and check_is_a_float(price):  #Verifica números
                self._set_atributes(name, year, price, condition)  #Chama o método que
                                    #atribui os argumentos aos atributos da instância
                self._is_newcar_valid(True)  #Marca a instância como carro válido
                return True
            else:               #Se houve input inválida
                    self._is_newcar_valid(False)  #Marca a instância como carro não válido
                    return False
        else:                   #Se não existe pelo menos 4 argumentos
            self._is_newcar_valid(False)  #Marca a instância como carro não válido
            return False

    def _is_newcar_valid(self, valid):  #Método que marca o carro como válido ou não
        self.is_valid = valid   #Atributo de carro válido

    def _set_atributes(self, name, year, price, condition):
        self.name = name        #Nome do carro
        self.year = year        #Ano de fabricação
        self.price = price      #Preço
        self.condition = condition  #Estado de conservação

    def _save_new_car(self):    #Método que grava um novo carro no estoque
        new_car_to_save_dict = {'name': self.name,  #Dicionário com os atributos do carro
                        'year': self.year,
                        'price': self.price,
                        'condition': self.condition}
        
        self.dao_conn.save_new_car_to_db(new_car_to_save_dict)
        print('\nCarro adicionado ao estoque com sucesso!\n')


def __show_search_result(list_to_show):  #Função que mostra lista de carros
    print(f'\n{len(list_to_show)} carro(s) encontrado(s):')
    for item in list_to_show:   #Para cada item na lista, mostra os detalhes
        print(f'Carro:\t{item['name']}')
        print(f'Ano:\t{item['year']}')
        print(f'Preço:\tR$ {float(item['price']):.2f}')
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
                if condition.casefold() in car['condition'].casefold():  #Compara o estado de conservação
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


def show_usage_info_and_errors(message = None):  #Função "help" caso o programa não seja chamado corretamente
    if message:
        print(f'\n{message}')
        print(f"\nType '{program_filename} help' to obtain usage examples.\n")
    else:
        print(f'\nUsage: {program_filename} <operation> <options>')
        print('\nOperations:\tnewcar\t\tInsert new car to stock')
        print('\t\tsearch\t\tSearch for a car by price or condition')
        print('\t\tlistall\t\tList all cars in stock')
        print('\t\thelp\t\tShow this help screen\n\n')
        print('To insert a new car to stock, enter the arguments as below:')
        print(f'\t{program_filename} newcar <car_name> <fabrication_year> <price> <condition>')
        print(f'\tArguments <fabrication_year> and <price> needs to be a number')
        print(f'\tExemple: {program_filename} Corolla 2010 35000 Seminovo\n')
        print('For a search, use the PRICE or CONDITION as a key, one at once')
        print(f'\tExemple: {program_filename} search <price> or <condition>\n')
        print('To list all cars in stock, use <listall> argument')
        print(f'\tExemple: {program_filename} listall\n\n')    


def check_is_a_float(num):
    try:
        num = float(num)
    except ValueError:
        return False
    else:
        return num


def __build_new_car(args):
    args.pop(0)         #Descarta o argumento 'newcar'
    new_car = Car(args)  #Cria uma instância de carro (Car) passando os argumentos
    if new_car.is_valid:  #Verifica se o carro informado é válido (mínimo de 4 argumentos)
        if __ask_to_save_new_car(new_car):
            new_car._save_new_car()  #Salva o novo carro no banco de dados
        else:
            show_usage_info_and_errors('-------> Informações descartadas <-------')
    else:               #Se as inputs estão incorretas ou faltantes
        show_usage_info_and_errors('-------> Please check inputs and try again! <-------')  #Mostra a forma correta de uso do programa    


def __check_input(text, options):
    #Validate user input with options provided
    user_input = input(text)
    if user_input in str(options):
        return user_input
    else:
        print('\nInvalid input! Run it again.')
        return


def __show_car_summary(car):
    print('Detalhes do carro\n')
    print(f'Carro:\t{car.name}')
    print(f'Ano:\t{car.year}')
    print(f'Preço:\tR$ {float(car.price):.2f}')
    print(f'Estado:\t{car.condition}\n')


def __ask_to_save_new_car(car):
    __show_car_summary(car)
    if __check_input(f'Deseja salvar o carro no estoque (S/n)? ', ['S', 'n']) == 'S':
        return True


def __main():                   #Função principal
    valid_args = ['newcar', 'search', 'listall', 'help']  #Lista dos argumentos válidos
    args = sys.argv             #Variável recebe todos os argumentos
    args.pop(0)                 #Descarta o nome do programa
    if (not args) or (args[0] not in valid_args):  #Se não existir argumentos ou
                    #o que existir não estiver na lista de argumentos válidos
        show_usage_info_and_errors()     #Mostra a forma correta de uso do programa
    else:                       #Se existe argumento válido
        if args[0] == 'newcar':  #Se o argumento é para novo carro
            __build_new_car(args)

        elif args[0] == 'search':  #Se o argumento é para busca
            __search_car(args[1])  #Chama a função de busca passando a input

        elif args[0] == 'listall':  #Se o argumento é para listagem completa
            __list_all_cars()   #Chama a função que mostra todos os carros
        
        elif args[0] == 'help':
            show_usage_info_and_errors()  #Mostra a forma correta de uso do programa


if __name__ == "__main__":
    __main()
    