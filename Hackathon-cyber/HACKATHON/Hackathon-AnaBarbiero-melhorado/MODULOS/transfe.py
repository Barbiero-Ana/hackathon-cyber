from rich.theme import Theme
from rich.console import Console

# Tema para estilização
# Entradas - [bold yellow]
estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

console = Console(theme=estilo)

def transferencia(origem, destino, valor):
    try:
        if valor <= 0:
            console.print('O valor deve ser maior que zero!', style='error')
            return

        if valor > origem['saldo']:
            console.print('Saldo insuficiente para realizar a transferência!', style='error')
            return

        origem['saldo'] -= valor
        destino['saldo'] += valor

        console.print(f"\nTransferência de R${valor:.2f} realizada com sucesso!", style='certo')
        console.print(f"Saldo atual de {origem['nome']}: R${origem['saldo']:.2f}", style='saida')
        console.print(f"Saldo atual de {destino['nome']}: R${destino['saldo']:.2f}", style='saida')
    except ValueError:
        console.print('Entrada inválida!', style='error')