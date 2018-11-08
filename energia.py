import calculo


class Energia(calculo.Calculo):
    def __init__(self, leituraAnterior, leituraAtual, consumo, pis, cofins, icms, total, kw, totalImpostos):
        self.pis = pis
        self.cofins = cofins
        self.icms = icms
        self.total = total
        self.kw = kw
        self.totalImpostos = totalImpostos
        super().__init__(leituraAnterior, leituraAtual, consumo)

    def entrada(self):
        print("CONTA DE ENERGIA")
        self.leituraAnterior = int(input("Digite o valor da leitura Anterior:"))
        self.leituraAtual = int(input("Digite o valor da leitura Atual:"))
        print()

        if self.leituraAtual <= self.leituraAnterior:
            print("Os valores inseridos estão incorretos, selecione novamente a opção desejada no menu.")
            print()
        else:
            print("Os valores inseridos estão corretos")
            print()
            self.consumo = self.leituraAtual - self.leituraAnterior

    def calculaKW(self,):
        # Calcula valor bruto
        self.kw = self.consumo * 0.36

        # Calcula PIS
        self.pis = (self.kw/100)*1.36

        # Calcula COFINS
        self.cofins = (self.kw/100)*6.25

        # Calcula ICMS
        self.icms = (self.kw/100)*36.5

        # Calcula o total de impostos
        self.totalImpostos = self.pis + self.cofins + self.icms

        # Calcula Total da Conta
        self.total = self.kw + self.totalImpostos

    def saida(self):
        print()
        print("o valor da conta sem os impostos é de: %.2f " % self.kw)
        print("o valor do PIS cobrado de sua conta é de: %.2f " % self.pis)
        print("o valor do COFINS cobrado de sua conta é de: %.2f " % self.cofins)
        print("o valor do ICMS cobrado de sua conta é de: %.2f " % self.icms)
        print("o valor total de impostos cobrados de sua conta é de: %.2f " % self.totalImpostos)
        print("o valor valor total de sua conta é de: %.2f" % self.total)
        print()








