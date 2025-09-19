import sqlite3
import csv
from pathlib import Path


# Caminho do banco SQLite
ROOT_PATH = Path(__file__).parent
def conectar():
    return sqlite3.connect(ROOT_PATH /"powerstack.sqlite")

# Caminho do CSV bruto
CSV_PATH = ROOT_PATH / "relatorio_estoque.csv"

def criar_tabela_raw():
    with conectar() as conexao:
        cursor = conexao.cursor()   
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque_raw (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Produto TEXT,
        Referencia TEXT,
        Saldo REAL
    
    )
    """)
    conexao.commit()
    #conexao.close()

def importar_csv():
    #conexao = sqlite3.connect(DB_PATH)
    with conectar() as conexao:
        cursor = conexao.cursor()

    with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=";")  # ajuste delimitador se precisar

        for linha in leitor:

            produto = linha["Produto"]
            referencia = linha["Refer?ncia"]
            saldo_str = linha["Saldo"]

            if saldo_str:
                saldo = float(saldo_str.replace(",","."))
            else:
                saldo = 0.0

            cursor.execute("""
                INSERT INTO estoque_raw (Produto, Referencia, Saldo)
                VALUES (?, ?, ?)
            """, (produto, referencia, saldo)
            )

    conexao.commit()
    print("✅ CSV importado com sucesso para estoque_raw")

if __name__ == "__main__":
    criar_tabela_raw()
    importar_csv()
