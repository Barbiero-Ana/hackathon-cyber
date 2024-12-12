from rich.theme import Theme
from rich.console import Console
from rich.table import Table

# Tema para estilização
estilo = Theme({
    'titulo': 'bold underline magenta',
    'error': 'bold red'
})

console = Console(theme=estilo)

def registrar_despesas():
    despesas = []
    while True:
        descricao = input('\nDigite a descrição da despesa (ou "sair" para encerrar): ')
        if descricao.lower() == 'sair':
            break
        try:
            valor = float(input('Digite o valor da despesa: '))
            despesas.append({'descricao': descricao, 'valor': valor})
        except ValueError:
            console.print('Valor inválido!', style='error')
    return despesas

def gerar_relatorio(despesas):
    console.print("\n=== Relatório de Despesas ===", style='titulo')
    tabela = Table(show_header=True, header_style="bold magenta")
    tabela.add_column("Descrição")
    tabela.add_column("Valor", justify="right", style="bold red")

    for despesa in despesas:
        tabela.add_row(despesa['descricao'], f"R${despesa['valor']:.2f}")

    console.print(tabela)
