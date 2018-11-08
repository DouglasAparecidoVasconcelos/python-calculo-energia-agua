import calculo


class Agua(calculo.Calculo):
    def __init__(self, leituraAnterior, leituraAtual, consumo, litros, total):
        self.litros = litros
        self.total = total
        super().__init__(leituraAnterior, leituraAtual, consumo)

    def entradaAgua(self):
        print("CONTA DE AGUA")
        self.leituraAnterior = int(input("Digite o valor da leitura Anterior:"))
        self.leituraAtual = int(input("Digite o valor da leitura Atual:"))

        if self.leituraAtual <= self.leituraAnterior:
            print("Os valores inseridos estão incorretos, selecione novamente a opção desejada no menu.")
            print()
        else:
            print("Os valores inseridos estão corretos")
            self.consumo = self.leituraAtual - self.leituraAnterior
            self.litros = self.consumo*1000

    def calculaM3(self):
        # Calcula conta de agua segundo a regra passada no arquivo.

        if self.consumo <= 10.99:
            self.total = 14.19

        elif self.consumo > 10.99 and self.consumo <= 20.99:
            self.total = 14.19 * 1.98

        elif self.consumo > 21 and self.consumo <= 50:
            self.total = 14.19 * 3.04

        else:
            self.total = 14.19 * 3.63

    def saidaAgua(self):
        print()
        print("Voce usou %.0f de Água" % self.litros)
        print("O valor de sua conta de Água é de: %.2f" % self.total)
        print()


