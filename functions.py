from classes import File, Dao, Car
from classes import program_filename, db_cars_filepath

def __show_search_result(list_to_show):  #Função que mostra lista de carros
    print(f'\n{len(list_to_show)} carro(s) encontrado(s):')
    for item in list_to_show:   #Para cada item na lista, mostra os detalhes
        print(f'Carro:\t{item['name']}')
        print(f'Ano:\t{item['year']}')
        print(f'Preço:\tR$ {float(item['price']):.2f}')
        print(f'Estado:\t{item['condition']}\n')


def search_car(search_info):  #Função para busca de carros
    def _search_by_price(price):  #Subfunção que busca por preço
        dao_conn = Dao()
        car_stock = dao_conn.get_content_list()
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
        dao_conn = Dao()
        car_stock = dao_conn.get_content_list()
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


def list_all_cars():          #Função que lista todos os carros
    dao_conn = Dao()
    car_stock = dao_conn.get_content_list()
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


def build_new_car(args):
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
    