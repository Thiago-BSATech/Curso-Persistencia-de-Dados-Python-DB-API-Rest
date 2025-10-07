list = ["homem aranha: sem volta pra casa", "Interestelar", "Os vingadores"]

tuple = '03/12/2021', "20/10/2021", "03/06/2018" 

dictionary = {list[0]: tuple[0], list[1]: tuple[1], list[2]: tuple[2]}

# A partir do dicionário que você criou, faça um loop no dicionário e imprima na tela suas chaves e os valores

# Se quiser saber mais sobre como realizar essa atividade, clique na opinião da pessoa instrutora.

for il, it in dictionary.items():
    print(f'{il}: foi visto no dia {it}')