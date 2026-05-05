import re
from Nota_fiscal_Embratel import NotaFiscalEmbratel
from Nota_fiscal_Vivo import NotaFiscalVivo
from POO_Automacao import Estrategia, NotaFiscal
from Nota_fiscal_Algar import NotaFiscalAlgar
import pdfplumber as pdftool

def CriaObjetos(pdf_texto):
    try:
        regex_cnpj = r'(?:CNPJ Matriz\s*:\s*|C\d?NPJ:\s*|CNPJ\s*)(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
        match_cnpj = re.search(regex_cnpj, pdf_texto)
    
        cnpjOperadora = match_cnpj.group(1)

        if cnpjOperadora.__contains__('02.558.157/0001-62'):
            fatura = Estrategia(pdf_texto, NotaFiscal)
            fatura.definirNota(NotaFiscalVivo)
            return fatura.adicionarValores(pdf_texto)
        
        elif cnpjOperadora.__contains__('05.872.814/0001-30') or cnpjOperadora.__contains__('05.872.814/0007-25'):
            fatura = Estrategia(pdf_texto, NotaFiscal)
            fatura.definirNota(NotaFiscalAlgar)
            return fatura.adicionarValores(pdf_texto)

        elif cnpjOperadora.__contains__('40.432.544/0001-47') or cnpjOperadora.__contains__('02.667.694/0001-40'):
            fatura = Estrategia(pdf_texto, NotaFiscal)
            fatura.definirNota(NotaFiscalEmbratel)
            return fatura.adicionarValores(pdf_texto)
        

    except Exception as e:
        print(f"erro no processamento: {e}")
    return NotaFiscalEmbratel('', '', '', '', '', '', '','')

def extrair_texto(filepath):
    try:  
        texto_completo = []  
        with pdftool.open(filepath) as tool:
            for num_pag, pagina in enumerate(tool.pages, 0):

                if num_pag >= 10:
                    break

                data = pagina.extract_text()
                texto_completo.append(data)

                print(data)
                print("________________________________________")
    except Exception as e:
        print(e)
    return '\n'.join(texto_completo)
