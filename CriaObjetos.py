import re
from Nota_fiscal_Embratel import NotaFiscalEmbratel
from Nota_fiscal_Vivo import NotaFiscalVivo
from POO_Automacao import Estrategia, NotaFiscal
import pdfplumber as pdftool

def CriaObjetos(pdf_texto):
    regex_cnpj = r'(?:CNPJ Matriz\s*:\s*|C\d?NPJ:\s*)(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
    match_cnpj = re.search(regex_cnpj, pdf_texto)

    cnpjOperadora = match_cnpj.group(1)

    if cnpjOperadora == '02.558.157/0001-62':
        fatura = Estrategia(pdf_texto, NotaFiscal)
        fatura.definirNota(NotaFiscalVivo)
        return fatura.adicionarValores(pdf_texto)

    if cnpjOperadora == '40.432.544/0001-47' or '02.667.694/0001-40':
        fatura = Estrategia(pdf_texto, NotaFiscal)
        fatura.definirNota(NotaFiscalEmbratel)
        return fatura.adicionarValores(pdf_texto)

    return NotaFiscalEmbratel('', '', '', '', '', '', '','')

def extrair_texto(filepath):
    texto_completo = []
    with pdftool.open(filepath) as tool:
        for num_pag, pagina in enumerate(tool.pages, 0):

            if num_pag >= 10:
                break

            data = pagina.extract_text()
            texto_completo.append(data)

            print(data)
            print("________________________________________")
    return '\n'.join(texto_completo)