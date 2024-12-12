from rich.theme import Theme
from rich.console import Console

# Tema para estilização
estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

console = Console(theme=estilo)

# Dicionário de opções de investimento
investimentos = {
    1: ('Poupança', 0.5),
    2: ('CDB', 0.8),
    3: ('Fundos Imobiliários', 1.2),
    4: ('Tesouro Selic', 0.7),
    5: ('Peer-to-Peer Lending', 1.4),
    6: ('Debêntures', 1.0),
    7: ('Fundo Multimercado', 1.1)
}

def opcoes_investimento():
    console.print('\nOpções de investimento disponíveis:\n', style='titulo')
    for chave, (nome, taxa) in investimentos.items():
        console.print(f'{chave}. {nome} - Rendimento de {taxa}% ao mês', style='entrada')

def rendimento(valor, taxa, meses):
    return valor * (1 + (taxa / 100)) ** meses

def investimento(cliente):
    console.print("\n=== Central de investimentos ===", style='titulo')
    opcoes_investimento()

    try:
        opcao = int(input('\nEscolha onde deseja investir seus fundos (digite o número correspondente): '))
        if opcao not in investimentos:
            console.print('Opção inválida!', style='error')
            return

        valor = float(input('\nDigite o valor que deseja investir: '))
        if valor <= 0 or valor > cliente['saldo']:
            console.print('Valor inválido ou saldo insuficiente!', style='error')
            return

        meses = int(input('\nDigite por quantos meses deseja investir: '))
        if meses <= 0:
            console.print('O tempo deve ser maior que zero!', style='error')
            return

        nome_invest, taxa = investimentos[opcao]
        valor_final = rendimento(valor, taxa, meses)
        cliente['saldo'] -= valor

        console.print(f'\nInvestido em {nome_invest}. R${valor:.2f} renderá R${valor_final:.2f} em {meses} meses.', style='certo')
        console.print(f'Saldo atual: R${cliente["saldo"]:.2f}', style='saida')
    except ValueError:
        console.print('Entrada inválida!', style='error')
