import csv

with open("relatorio_estoque.csv", newline="", encoding="utf-8") as f:
    leitor = csv.DictReader(f, delimiter=";")
    for linha in leitor:
        print(linha)