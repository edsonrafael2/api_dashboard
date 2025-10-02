import pdfplumber
import re

def extrair_total_vendas(caminho_pdf: str) -> float:
    """
    Lê um PDF e retorna o valor total de vendas encontrado.
    Retorna 0.0 se não encontrar.
    """
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"

    # Regex para localizar valores monetários (ex: R$ 12.345,67)
    padrao_valor = re.compile(r"R\$\s?([\d\.\,]+)")

    # Procurar palavras-chave antes de valores
    if "Total de Vendas" in texto or "Total" in texto:
        valores = padrao_valor.findall(texto)
        if valores:
            ultimo_valor = valores[-1]  # geralmente o último é o total
            return float(ultimo_valor.replace(".", "").replace(",", "."))
    
    return 0.0





caminho_pdf = "relatorios/vendas_setembro.pdf"
print(f" O Valor total da Vendas: {extrair_total_vendas(caminho_pdf)}")

