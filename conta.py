class Conta:
    #função contrutora da minha classe
    def __init__(self, numero:int, titular:str, saldo:float, limite:float):
        #atributos da minha classe (dois underscore para torna-los privados)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    #métodos da minha classe
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property #getter
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter #setter
    def limite(self, limite):
        self.__limite = limite
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    
    