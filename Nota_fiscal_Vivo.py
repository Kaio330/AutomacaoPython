import re
from POO_Automacao import NotaFiscal

class NotaFiscalVivo(NotaFiscal):
    def __init__(self,conta, data_emissao, data_vencimento, nota, valor_total, cnpj, tipo_conta):
        super().__init__(conta, data_emissao, data_vencimento, nota, valor_total, cnpj, tipo_conta)


    @classmethod
    def adicionarValores(cls, pdf_texto):

        regex_conta = r'(?:CÓDIGO DO CLIENTE|Número da Conta|Conta)[:]?\s*(\d{10,15})'
        regex_emissao = r'(?:DATA DE EMISSÃO:\s*|\BAIRRO\s*[:]?\s*\w+\s*\w+?|BAIRRO\s*\w+[:]\w+[.]?\s*\w+\s*\w+\?s*\w+?)\s*(\d{2}/\d{2}/\d{4})'
        regex_vencimento = r'(?i)Vencimento\s*(\d{2}/\d{2}/\d{4}|\d:\d\s*/\d{2}/\d{4})|(\d{2}/\d{2}/\d{4})\s+\d{1,3}(?:\.\d{3})*,\d{2}'
        regex_fatura = r'Nº NFCOM (\d+)'
        regex_valor = r'(?:TOTAL A PAGAR|\d+[-]\d+) (\d+[\.,]?\d+[\.,]\d{1,2}|0,00)'
        regex_cnpj = r'(?i)CNPJ Matriz\s*:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
        regex_TipoConta = r'SERVICO GESTAO (\w+\s*\w+)'


        match_conta = re.search(regex_conta, pdf_texto)
        match_emissao = re.search(regex_emissao, pdf_texto)
        match_vencimento = re.search(regex_vencimento, pdf_texto)
        match_fatura = re.search(regex_fatura, pdf_texto)
        match_valor = re.search(regex_valor, pdf_texto)
        match_cnpj = re.search(regex_cnpj, pdf_texto)
        match_TipoConta = re.search(regex_TipoConta, pdf_texto)


        conta = match_conta.group(1) if match_conta else None
        data_emissao = match_emissao.group(1) if match_emissao else None
        data_vencimento = match_vencimento.group(1) if match_vencimento else None
        nota = match_fatura.group(1) if match_fatura else None
        valor_total = match_valor.group(1) if match_valor else None
        cnpj = match_cnpj.group(1) if match_cnpj else None
        TipoConta = match_TipoConta.group(1) if match_TipoConta else None


        return cls(conta, data_emissao, data_vencimento, nota, valor_total, cnpj, TipoConta)