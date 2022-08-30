#Lucas Bonfim
#29/08/2022
#API para consultar dados do CEP.

import requests


#Input para o cliente preencher utilizando um CEP.
cep = str(input("Digite um CEP: "))
cep = cep.replace("-", "").replace(".", "").replace(" ", "")



if len(cep) == 8:
    #link de onde sera extraido a API.
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisição = requests.get(link)
    dicionario = requisição.json()


    #Informações principais que serão extraidas e apresentadas ao cliente.
    uf = dicionario['uf']   
    cidade = dicionario['localidade']
    bairro = dicionario['bairro']
    logradouro = dicionario['logradouro']
    #Saida das informações.
    print("{}\n{}\n{}\n{}\n". format(logradouro, bairro, cidade, uf))


    #else caso o CEP do cliente seja invalido.
else:
    print('CEP invalido tente novamente!')