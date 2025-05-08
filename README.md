Projeto “Concessionária”
A fim de praticar os conhecimentos recebidos até o momento, desenvolva um software para uma concessionária de veículos que atenda aos seguintes requisitos:

• Cadastro de novos carros: o usuário pode registrar novos veículos no sistema, detalhando as informações do carro;
• Busca no estoque: o usuário informa um critério de pesquisa (preço máximo ou estado de conservação), e o sistema verifica a disponibilidade de carros e exibe os resultados encontrados.
Em relação ao desenvolvimento, você deve:
Implementar um menu interativo que permita ao usuário escolher entre cadastrar um novo carro ou pesquisar pelos carros já cadastrados. O menu deve continuar sendo exibido infinitamente até que o usuário digite uma tecla específica para sair (por exemplo, "0" ou “q”). O menu deve oferecer as seguintes opções:
• Cadastrar um novo carro: O usuário será solicitado a fornecer os dados do carro (nome, preço, ano, estado) e o carro será cadastrado em um arquivo chamado estoque_carros.txt;
• Pesquisar carros: O usuário poderá pesquisar carros no arquivo estoque_carros.txt com base no preço ou no estado do carro. O usuário deverá digitar o valor para pesquisa (preço ou estado), e todos os carros que atenderem ao critério deverão ser exibidos;
• Sair: O menu será interrompido e o programa será finalizado quando o usuário teclar "0" ou “q”.

Implementar uma função chamada cadastrar_carro(), que permita ao usuário cadastrar um novo carro no arquivo estoque_carros.txt. A função deve:
• Solicitar ao usuário as seguintes informações: Nome, Preço (número decimal), Ano de fabricação, Estado (ex.: novo, seminovo, etc.);
• Adicionar essas informações ao final do arquivo estoque_carros.txt, no formato: nome_carro,preco,ano,estado.

Implementar uma função chamada procurar_carro(), que deve retornar uma lista contendo os carros encontrados, na qual cada carro é um dicionário com as informações nome_carro, preco, ano e estado. A função deve ser capaz de verificar se o usuário informou um valor numérico (float) e portanto deseja buscar por preço máximo ou se informou uma palavra (string) e deseja buscar pelo estado do carro (por exemplo, "novo", "seminovo", "conservado", "mal estado"):
• Caso o usuário informe um valor numérico, o sistema entenderá que ele está pesquisando por preço máximo;
• Caso o usuário informe uma palavra, o sistema interpretará como uma pesquisa por estado do carro;
• Se a pesquisa for por preço: verifique se o preço do carro é menor ou igual ao valor informado;
• Se a pesquisa for por estado: verifique se o estado do carro corresponde ao valor informado;
• Para cada carro que atenda ao critério, exiba as informações do carro (nome, preço, ano e estado) na tela;
• Caso nenhum carro atenda ao critério, exiba a mensagem: "Carro não encontrado!
