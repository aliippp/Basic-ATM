from ATM_Card import ATMCard

class Customer:
    def __init__(self, id, pin=123456, saldo=950):
        self.id = id
        self.pin = pin
        self.saldo = saldo

    def cekId(self):
        return self.id
    def cekPin(self):
        return self.pin
    
    def cekSaldo(self):
        return self.saldo

    def tarikUang(self, nominal):
       self.saldo -= nominal
    
    def setorUang(self, nominal):
        self.saldo += nominal