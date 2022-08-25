class circulo:
    def __init__(self, x, y, raio):
        self.centro_x = x
        self.centro_y = y
        self.raio = raio
    def area(self):
        return 3.14 * self.raio * self.raio
    def diametro(self):
        return 2 * self.raio
    def circunferencia(self):
        return 2 * 3.14 * self.raio
    def mudarposicao(self, pos_x, pos_y):
        self.centro_x = pos_x
        self.contro_y = pos_y 

meu_circulo = circulo(0,0,1)
print(meu_circulo.area())
print(meu_circulo.diametro())
print(meu_circulo.circunferencia())
meu_circulo.mudarposicao(2,3)
print(meu_circulo.centro_x)
print(meu_circulo.centro_y)
