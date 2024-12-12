from rich.theme import Theme
from rich.console import Console
from MODULOS.invest import investimentos
from MODULOS.cambio import cambio_trade
from MODULOS.relatorio import registrar_despesas, gerar_relatorio
from MODULOS.transfe import transferencia
from MODULOS.linguas import textos




# Tema para estilização
estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

console = Console(theme=estilo)

# valores de teste
cliente1 = {
    'nome': 'João Silva',
    'saldo': 1000.0,
    'moeda': 'BRL',
    'taxa_moeda': 1.0
}

cliente2 = {
    'nome': 'Maria Oliveira',
    'saldo': 500.0,
    'moeda': 'BRL',
    'taxa_moeda': 1.0
}



def selecionar_idioma():
    console.print("\nSelecione o idioma / Choose the language:", style='titulo')
    console.print("[1] Português (pt)", style='entrada')
    console.print("[2] English (en)", style='entrada')
    console.print("[3] Español (es)", style='entrada')
    console.print("[4] Français (fr)", style='entrada')
    console.print("[5] Deutsch (de)", style='entrada')
    console.print("[6] Русский (ru)", style='entrada')
    console.print("[7] 日本語 (jp)", style='entrada')
    console.print("[8] 한국어 (ko)", style='entrada')
    
    while True:
        opcao = input("\nDigite o número da opção / Enter the option number: ")
        linguas = {'1': 'pt', '2': 'en', '3': 'es', '4': 'fr', '5': 'de', '6': 'ru', '7': 'ja', '8': 'ko'}
        if opcao in linguas:
            return linguas[opcao]
        else:
            console.print("Opção inválida! / Invalid option!", style='error')




def menu(idioma):
    t = textos[idioma]
    
    while True:
        console.print("\n=== Menu de Opções ===",style='titulo')
        
        while True:
            console.print(t["menu_opcoes"], style='titulo')
            
            console.print(t["investir"], style='entrada')
            console.print(t["cambio"], style='entrada')
            console.print(t["registrar_despesas"], style='entrada')
            console.print(t["transferir"], style='entrada')
            console.print(t["sair"], style='entrada')

            opcao = input(t["escolha"])


            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                investimentos(cliente1)
            elif opcao == '2':
                cambio_trade(cliente1)
            elif opcao == '3':
                despesas = registrar_despesas()
                gerar_relatorio(despesas)
            elif opcao == '4':
                console.print(t["\n=== Transferência entre Usuários ==="], style='titulo')
                try:
                    while True:
                        valor = float(input(f"\nDigite o valor para transferir de {cliente1['nome']} para {cliente2['nome']}: "))
                        if valor > cliente1['saldo']:
                            console.print("Saldo insuficiente! Tente novamente com um valor menor.", style='error')
                        else:
                            transferencia(cliente1, cliente2, valor)
                            break
                except ValueError:
                    console.print(t["Valor inválido!"], style='error')
            
            elif opcao == '5':
                console.print(t["\nSaindo do sistema. Até logo!"], style='certo')
                break
            
            else:
                console.print(t["\nOpção inválida. Tente novamente."], style='error')

if __name__ == "__main__":
    idioma_selecionado = selecionar_idioma()
    menu(idioma_selecionado)
