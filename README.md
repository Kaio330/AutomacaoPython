# Extrator de Dados de Notas Fiscais (PDF para Excel)

Este projeto automatiza a extração de dados de notas fiscais de telecomunicações (faturas em PDF de operadoras como Vivo, Algar, e Embratel) e gera uma planilha Excel com as informações organizadas. Ele funciona como um serviço de monitoramento, observando uma pasta específica para novos arquivos PDF e processando-os automaticamente.

## 🚀 Funcionalidades

- **Monitoramento Automático de Diretório:** Observa a pasta `Pdfs/` à procura de novos arquivos PDF e os processa assim que são adicionados.
- **Extração Inteligente de Dados:** Lê o texto dos PDFs utilizando a biblioteca `pdfplumber`.
- **Identificação da Operadora:** Utiliza Regex para identificar a operadora pelo CNPJ presente no documento (suporta Vivo, Algar e Embratel/Claro).
- **Design Pattern Strategy:** Emprega o padrão de projeto Strategy para lidar com os diferentes formatos de fatura de cada operadora de forma escalável e organizada.
- **Geração de Planilha (Excel):** Exporta os dados extraídos (Conta, Valor Total, Data de Emissão, Data de Vencimento, Fatura, CNPJ, Tipo Conta, RPS) para uma planilha Excel salva na pasta `Planilhas Preechidas/`.

## 📁 Estrutura de Arquivos

- `Main.py`: Script principal. Inicia o monitoramento da pasta `Pdfs/` utilizando `watchdog` e gerencia a criação da planilha e salvamento na pasta `Planilhas Preechidas/`.
- `CriaObjetos.py`: Responsável por abrir o PDF, extrair o texto, identificar a operadora (via CNPJ) e invocar a classe correspondente para extrair os valores.
- `POO_Automacao.py`: Contém a estrutura base Orientada a Objetos, definindo as classes `NotaFiscal` (com lógica de exportação para Excel) e `Estrategia` (padrão de projeto).
- `Nota_fiscal_Vivo.py`, `Nota_fiscal_Algar.py`, `Nota_fiscal_Embratel.py`: Classes específicas que estendem as regras de negócio para encontrar e extrair os dados particulares das faturas de cada empresa.
- `Pdfs/`: Diretório onde você deve colocar os arquivos `.pdf` para processamento.

## 🛠️ Requisitos

Certifique-se de ter o Python 3 instalado e as seguintes bibliotecas do Python:

```bash
pip install openpyxl watchdog pdfplumber
```

## ⚙️ Como Usar

1. **Clone o repositório** e acesse a pasta do projeto.
2. Certifique-se de que a pasta `Pdfs/` existe no mesmo diretório do arquivo `Main.py` (ela será criada ou deve ser criada se não existir).
3. **Execute o script principal**:

   ```bash
   python Main.py
   ```
4. O console exibirá: `Monitorando a pasta: .../Pdfs`. O script ficará em execução aguardando novos arquivos.
5. **Adicione arquivos PDF** de faturas (Vivo, Algar, Embratel) na pasta `Pdfs/`.
6. Após detectar e processar os arquivos, o sistema criará (se não existir) uma pasta chamada `Planilhas Preechidas/` na raiz do projeto e salvará nela um arquivo Excel (.xlsx) contendo os dados extraídos, com a data e hora atual no nome.

## 🛑 Parando o Monitoramento

Para parar o script, pressione `Ctrl+C` no terminal onde o `Main.py` está sendo executado.

## 💻 Arquitetura

O sistema é um ótimo exemplo de uso de Padrões de Projeto (Design Patterns) em Python:
- **Strategy Pattern (`Estrategia` em `POO_Automacao.py`):** Permite selecionar dinamicamente (em tempo de execução, baseado no CNPJ) qual algoritmo (classe da operadora) deve ser utilizado para parsear o PDF, facilitando a adição de novas operadoras no futuro sem modificar a estrutura principal.
- **Observer Pattern (`watchdog` em `Main.py`):** Observa alterações em arquivos e reage a elas através de eventos assíncronos.
