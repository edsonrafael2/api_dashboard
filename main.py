
from extrator_pdf import extrair_total_vendas
from atualizador_dre import atualizar_receita_bruta

def main():
    # Caminhos
    caminho_pdf = "relatorios/vendas_setembro.pdf"
    caminho_planilha = "DRE_Mensal_Com_Formulas.xlsx"
    saida_planilha = "DRE_Atualizada.xlsx"

    # Define o mês manualmente (pode ser capturado por input futuramente)
    mes = "SET"

    # 1. Extrair valor do PDF
    total_vendas = extrair_total_vendas(caminho_pdf)
    print(f"📊 Total de Vendas extraído: R$ {total_vendas:,.2f}")

    # 2. Atualizar planilha
    atualizar_receita_bruta(caminho_planilha, mes, total_vendas, saida_planilha)

if __name__ == "__main__":
    main()
