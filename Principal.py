from agua import Agua
from energia import Energia

opcao = 100
contaEnergia = Energia(0, 0, 0, 0, 0, 0, 0, 0, 0)
contaAgua = Agua(0, 0, 0, 0, 0)

while opcao != 0:
    opcao = int(input("Digite 1 para realizar o cálculo da sua conta de agua\nDigite 2 para realizar o cálculo da sua conta de energia\nDigite 0 para sair do programa\n"))
    if opcao == 1:

        contaAgua.entradaAgua()
        contaAgua.calculaM3()
        contaAgua.saidaAgua()

    elif opcao == 2:

        contaEnergia.entrada()
        contaEnergia.calculaKW()
        contaEnergia.saida()

print("Até logo!!!")
