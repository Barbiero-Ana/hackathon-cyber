from rich.theme import Theme
from rich.console import Console
import math

# Tema para estilização
estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

console = Console(theme=estilo)


#Assim fica melhor para codar sem precisar usar o split :D
emprestimos = {
    1: (500.00, 0.03),  # R$500,00, 3% de juros
    2: (1000.00, 0.07),  # R$1.000,00, 7% de juros
    3: (1500.00, 0.10)   # R$1.500,00, 10% de juros
}

def opcoes_emprestimo():
    console.print('\nOpções de empréstimos disponíveis:\n', style='titulo')
    for chave, (valor, taxa) in emprestimos.items():
        console.print(f'{chave}. Empréstimo de R${valor:.2f} - Taxa: {taxa * 100:.2f}%', style='entrada')
        #print com ''titulo'' de cada opção descrita no dicionário direto

def taxas_emprestimo(valor, meses, taxa_juros):
    # total do empréstimo com juros compostos
    valor_final = valor * (1 + taxa_juros) ** meses
    return valor_final

def parcelamento(valor, meses, taxa_juros):
    # valor final do empréstimo com juros compostos
    valor_final = taxas_emprestimo(valor, meses, taxa_juros)
    # valor da parcela mensal
    return valor_final / meses

def emprestimo(cliente):
    console.print("\n=== Central de Empréstimos do Banco Noob Bank ===", style='titulo')
    opcoes_emprestimo()
    try:
        opcao = int(console.input('\n[bold yellow]Escolha qual o tipo de empréstimo que atende suas necessidades (digite o número correspondente): '))
        if opcao not in emprestimos:  
            console.print('Opção inválida... Tente novamente.', style='error')
            return

        meses = int(console.input('\n[bold yellow]Digite em quantos meses gostaria de parcelar o pagamento do empréstimo: '))
        if meses <= 0:
            console.print('O tempo deve ser maior que zero...', style='error')
            return

        valor, taxa_juros = emprestimos[opcao]  
        valor_final = taxas_emprestimo(valor, meses, taxa_juros)
        valor_parcela = parcelamento(valor, meses, taxa_juros)

        
        cliente['saldo'] += valor  

        console.print(f'\nEmpréstimo de R${valor:.2f} concedido com sucesso! O saldo atual do cliente é R${cliente["saldo"]:.2f}.', style='certo')
        console.print(f'O valor total do empréstimo com juros será de R${valor_final:.2f}.', style='saida')
        console.print(f'O parcelamento será de R${valor_parcela:.2f} por mês durante {meses} meses.', style='saida')

        console.print(f'Seu saldo atual após o empréstimo é de R${cliente["saldo"]:.2f}.', style='saida')

    except ValueError:
        console.print('Entrada inválida!', style='error')


