"""
Loja de carros

Programa desenvolvido pelo Grupo DEV Carlo Acutis - Bruno Faria

brunofariasilva@gmail.com
08/05/2025 - 12/05/2025

-------

Problemas conhecidos:
1 - A leitura do resultado das buscas fica prejudicada, caso a listagem fique extensa.
"""

from functions import list_all_cars, show_usage_info_and_errors
from functions import build_new_car, search_car
import sys


def __main():                   #Função principal
    valid_args = ['newcar', 'search', 'listall', 'help']  #Lista dos argumentos válidos
    args = sys.argv             #Variável recebe todos os argumentos
    args.pop(0)                 #Descarta o nome do programa
    if (not args) or (args[0] not in valid_args):  #Se não existir argumentos ou
                    #o que existir não estiver na lista de argumentos válidos
        show_usage_info_and_errors()     #Mostra a forma correta de uso do programa
    else:                       #Se existe argumento válido
        if args[0] == 'newcar':  #Se o argumento é para novo carro
            build_new_car(args)  #Chama a função construtora do novo carro

        elif args[0] == 'search':  #Se o argumento é para busca
            search_car(args[1])  #Chama a função de busca passando a input

        elif args[0] == 'listall':  #Se o argumento é para listagem completa
            list_all_cars()   #Chama a função que mostra todos os carros
        
        elif args[0] == 'help':  #Se o argumento é para ajuda
            show_usage_info_and_errors()  #Mostra a forma correta de uso do programa


if __name__ == "__main__":
    __main()
    