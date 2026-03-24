import os

class NotaFiscal:
    def __init__(self, conta, data_emissao, data_vencimento, nota, valor_total, cnpj,
                 tipo_conta):
        self.conta = conta
        self.data_emissao = data_emissao
        self.data_vencimento = data_vencimento
        self.nota = nota
        self.cnpj = cnpj
        self.valor_total = valor_total
        self.tipoConta = tipo_conta

    def adicionarValores(self, pdf_texto):
        pass
        return

    def adicionarExcel(self, wb):

        directory = 'Pdfs'
        files = os.listdir(directory)
        files_quantity = len(files)

        if files_quantity == 0:
            raise Exception('Nenhum PDF foi encontrado')
        wb = wb
        ws = wb.active
        ws.title = "Planilha preenchida"

        ws['A1'] = 'Conta'
        ws['B1'] = 'Valor Total'
        ws['C1'] = 'Data de Emissão'
        ws['D1'] = 'Data de Vencimento'
        ws['E1'] = 'Fatura'
        ws['F1'] = 'Cnpj'
        ws['G1'] = 'Tipo Conta'
        ws['H1'] = 'RPS'

        last_empty_line = 1
        while ws['A' + str(last_empty_line)].value is not None:
            last_empty_line += 1


        if self.conta:
            conta = self.conta
            ws['A{}'.format(last_empty_line)] = conta
        else:
            ws['A{}'.format(last_empty_line)] = 'Nenhuma Conta'

        if self.valor_total:
            valor = self.valor_total
            ws['B{}'.format(last_empty_line)] = valor
        else:
            ws['B{}'.format(last_empty_line)] = "Nenhum Valor Total"

        if self.data_emissao:
            dataEmissao = self.data_emissao
            ws['C{}'.format(last_empty_line)] = dataEmissao
        else:
            ws['C{}'.format(last_empty_line)] = None

        if self.data_vencimento:
            dataVencimento = self.data_vencimento
            ws['D{}'.format(last_empty_line)] = dataVencimento
        else:
            ws['D{}'.format(last_empty_line)] = None

        if self.nota:
            notaFiscal = self.nota
            ws['E{}'.format(last_empty_line)] = notaFiscal
        else:
            ws['E{}'.format(last_empty_line)] = None

        if self.cnpj:
            Cnpj = self.cnpj
            ws['F{}'.format(last_empty_line)] = Cnpj
        else :
            ws['F{}'.format(last_empty_line)] = None

        if self.tipoConta:
            TipoConta = self.tipoConta
            ws['G{}'.format(last_empty_line)] = TipoConta
        else :
            ws['G{}'.format(last_empty_line)] = None


        if hasattr(self, 'rps'):
            if self.rps:
                rps = self.rps
                ws['H{}'.format(last_empty_line)] = rps
            else:
                ws['H{}'.format(last_empty_line)] = None

class Estrategia:
    def __init__(self, pdf_texto, estrategia: NotaFiscal):
        self.pdf_texto = pdf_texto
        self.estrategia = estrategia

    def definirNota(self, estrategia):
        self.estrategia = estrategia

    def adicionarValores(self, pdf_texto):
        self.pdf_texto = pdf_texto
        return self.estrategia.adicionarValores(pdf_texto)