from pathlib import Path
import json

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

    def read_file(self):       #Método para leitura do arquivo
        if not self._file_exists():  #Se o arquivo não existir
            self._create_file()  #Chama o método de criação do arquivo
        with open(self.path, 'r', newline='\n') as file_to_read:
            file_contents = json.load(file_to_read)  #Abre o arquivo e lê o conteúdo
        return file_contents    #Retorna o conteúdo do arquivo
    
    def save_file(self, dict_to_save):  #Método para salvar o arquivo
        with open(self.path, 'w', newline='\n') as file_to_save:
            json.dump(dict_to_save, file_to_save, indent=4)  #Salva o dicionário completo no arquivo


class Dao:                      #Classe para interação com arquivos
    def __init__(self):         #Inicialização da classe
        self.db_cars_contents = File(db_cars_filepath)  #Inicializa o arquivo de banco de dados
        self._init_cars_db()    #Chama o método de inicialização do banco de dados
    
    def _init_cars_db(self):    #Método para inicialização do banco de dados
        self.car_stock = self.db_cars_contents.read_file()  #Recupera o conteúdo do arquivo
    
    def save_new_car_to_db(self, car_dict):  #Método para salvar o novo carro no banco de dados
        self.car_stock['cars'].append(car_dict)   #Adiciona o novo carro no estoque
        self.db_cars_contents.save_file(self.car_stock)  #Salva o arquivo

    def get_content_list(self):  #Método para recuperar o conteúdo do arquivo em lista
        content = self.db_cars_contents.read_file()  #Lê o conteúdo do arquivo
        return content['cars']  #Retorna apenas o conteúdo em lista
   

class Car:                      #Classe para operações com carros
    def __init__(self, initial_args):  #Inicialização da classe
        if self._validate_args_atributes(initial_args):  #Validação dos argumentos
            self.dao_conn = Dao()  #Inicialização do banco de dados

    def _validate_args_atributes(self, args):  #Método para validação dos argumentos
        if len(args) >= 4:      #Verifica se existem pelo menos 4 argumentos
            name, year, price, condition = args[0], args[1], args[2], ' '.join(args[3:])  #Atribui às
                                                                    #variáveis os argumentos passados
            from functions import check_is_a_float
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

    def save_new_car(self):    #Método que grava um novo carro no estoque
        new_car_to_save_dict = {'name': self.name,  #Dicionário com os atributos do carro
                        'year': self.year,
                        'price': self.price,
                        'condition': self.condition}
        
        self.dao_conn.save_new_car_to_db(new_car_to_save_dict)
        print('\nCarro adicionado ao estoque com sucesso!\n')
