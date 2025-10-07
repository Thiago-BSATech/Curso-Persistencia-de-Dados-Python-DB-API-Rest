nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

with open("input_data.txt", "w") as f:

    f.write(f"Nome: {nome}\n")
    f.write(f"Idade: {idade}\n")

