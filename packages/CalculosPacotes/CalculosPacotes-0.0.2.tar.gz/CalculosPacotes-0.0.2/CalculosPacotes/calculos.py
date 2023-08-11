class CalculoMat:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def soma(self):
        return self.num1 + self.num2

    def subtrair(self):
        return self.num1 - self.num2
    
    def multiplica(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            raise ValueError("Não é possível dividir por zero.")