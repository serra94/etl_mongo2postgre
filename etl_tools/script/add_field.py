import json
import random
import argparse
import os

'''

FINALIDADE:

Esse script tem como finalidade adicionar campos em arquivos json, podendo ser 
útil quando houver a necessidade de se adicionar novos campos massivamente.

'''

def add_field(file, out_file=None, rewrite=False):
    '''
    Informe como primeiro argumento o path do arquivo que deseja adicionar um
    novo campo, posterioremente use a flag "--output_file" seguido do nome do
    arquivo de saída que deseja gerar ao final com a adição do campo e por fim
    adicione a flag "--rewrite" para escrever. Um exemplo final do comando
    seria:

    EX: python3 add_field.py ARQUIVO_BASE --out_file ARQUIVO_SAIDA --rewrite

    EX: python3 add_field.py ../data/ARQUIVO_BASE

    '''
    with open(file, 'r') as file:
        products = json.load(file)

    # GERA E INSERE A CHAVE E OS NÚMEROS ALEÁTORIOS QUE DESEJO CRIAR.
    for product in products:
        product['product_id'] = random.randint(1, 10000000000000)

    # VERIFICA SE O ARQUIVO JÁ EXISTE.
    if out_file:
        if rewrite or not os.path.exists(out_file):
            with open(out_file, 'w') as file:
                json.dump(products, file, indent=4)
            print(f'Os IDs foram adicionados ao arquivo "{out_file}"')
        else:
            print(f'O arquivo "{out_file}" já existe. Use a opção --rewrite para substituí-lo.')
    else:
        # PRINTA SE NENHUM ARQUIVO DE SAÍDA FOR INDICADO.
        print(json.dumps(products, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adicionar IDs aleatórios a um arquivo JSON de produtos.")
    parser.add_argument("file", help="O arquivo JSON de entrada contendo os produtos.")
    parser.add_argument("--output_file", help="O arquivo de saída onde os produtos com IDs serão armazenados.")
    parser.add_argument("--rewrite", action="store_true", help="rewrite o arquivo de saída se ele já existir.")
    
    args = parser.parse_args()
    add_field(args.file, args.output_file, args.rewrite)
