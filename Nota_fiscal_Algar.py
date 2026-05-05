import re
from POO_Automacao import NotaFiscal

class NotaFiscalAlgar(NotaFiscal):
    def __init__(self,conta, data_emissao, data_vencimento, nota, valor_total, cnpj, rps):
        super().__init__(conta, data_emissao, data_vencimento, nota, valor_total, cnpj)
        self.rps = rps
    

    @classmethod
    def adicionarValores(cls, pdf_texto):

        regex_conta = r'Nº DO CLIENTE[:]?\s*(\d{10,15})'
        regex_emissao = r'EMISSÃO DESTA CONTA:\s* (\d{2}/\d{2}/\d{4})'
        regex_vencimento = r'(?:MENSAGENS IMPORTANTES|você|ALGAR TELECOM S/A)\s*(\d{2}/\d{2}/\d{4})'
        regex_fatura = r'N°\s*(\d+)'
        regex_valor = r'(?:SUB-TOTAL FATURA R[^:]|TOTAL R[^:])\s*(\d+[\.,]\d+?[\.,]\d{1,2}|\d+[\.,]\d+?[\.,]?\d{1,2}|0,00)'
        regex_cnpj = r'(?i)CNPJ\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
        regex_rps =r'RPS:\s*(\d+).'


        match_conta = re.search(regex_conta, pdf_texto)
        match_emissao = re.search(regex_emissao, pdf_texto)
        match_vencimento = re.search(regex_vencimento, pdf_texto)
        match_fatura = re.search(regex_fatura, pdf_texto)
        match_valor = re.search(regex_valor, pdf_texto)
        match_cnpj = re.search(regex_cnpj, pdf_texto)
        match_rps = re.search(regex_rps, pdf_texto)


        conta = match_conta.group(1) if match_conta else None
        data_emissao = match_emissao.group(1) if match_emissao else None
        data_vencimento = match_vencimento.group(1) if match_vencimento else None
        nota = match_fatura.group(1) if match_fatura else None
        valor_total = match_valor.group(1) if match_valor else None
        cnpj = match_cnpj.group(1) if match_cnpj else None
        rps = match_rps.group(1) if match_rps else None

        
        return cls(conta, data_emissao, data_vencimento, nota, valor_total, cnpj,rps)
