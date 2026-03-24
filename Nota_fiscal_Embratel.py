import re
from POO_Automacao import NotaFiscal

class NotaFiscalEmbratel(NotaFiscal):

    def __init__(self, conta, data_emissao, data_vencimento, nota, valor_total, cnpj, tipo_conta, rps):
        super().__init__(conta, data_emissao, data_vencimento, nota, valor_total, cnpj, tipo_conta)
        self.rps = rps


    @classmethod
    def adicionarValores(cls, pdf_texto):

        regex_conta = r'(\d{11}-\d{4}) [\d{2}/\d{2}/\d{4}]?'
        regex_emissao = r'(?:DATA EMISSÃO|Data de Emissão)\s*:\s*(\d{2}/\d{2}/\d{4})'
        regex_vencimento = r'(\d{2}/\d{2}/\d{4})'
        regex_fatura = r'Nº da Fatura\s*:\s*\d{2}/\d{2}/((\d{8})[-](\d{1}))'
        regex_valor = r'(\d+[\.,]?\d+[\.,]\d{1,2})'
        regex_cnpj = r'(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
        regex_TipoConta = r'(\w{3,5}) -\w+\s*\w+\s*\w+\s*\w+\s*[\w+\s*\]?d+[\.,]?\d+[\.,]\d{1,2}'
        regex_rps = r'NÚMERO\s*:\s*(\d{6})'

        match_conta = re.search(regex_conta, pdf_texto)
        match_emissao = re.search(regex_emissao, pdf_texto)
        match_vencimento = re.search(regex_vencimento, pdf_texto)
        match_fatura = re.search(regex_fatura, pdf_texto)
        match_valor = re.search(regex_valor, pdf_texto)
        match_cnpj = re.search(regex_cnpj, pdf_texto)
        match_TipoConta = re.search(regex_TipoConta, pdf_texto)
        match_rps = re.findall(regex_rps, pdf_texto)


        conta = match_conta.group(1) if match_conta else None
        data_emissao = match_emissao.group(1) if match_emissao else None
        data_vencimento = match_vencimento.group(1) if match_vencimento else None
        nota = match_fatura.group(1) if match_fatura else None
        valor_total = match_valor.group(1) if match_valor else None
        cnpj = match_cnpj.group(1) if match_cnpj else None
        TipoConta = match_TipoConta.group(1) if match_TipoConta else None


        if len(match_rps) == 2:
            rps = match_rps[0] +'_'+ match_rps[1]

        elif len(match_rps) == 3:
            rps = match_rps[0] + '_' + match_rps[1] + '_' + match_rps[2]

        elif len(match_rps) == 1:
            rps = match_rps[0]

        else:
            rps = None

        contaJunta = conta + TipoConta


        return cls(contaJunta.replace('-',''), data_emissao, data_vencimento, nota.replace('-',''), valor_total, cnpj, TipoConta, rps)