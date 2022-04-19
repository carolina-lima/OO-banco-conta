from conta import Conta

#referência do meu objeto >> conta
conta = Conta(1234,"Carolina",0.0,1000.0)

conta2 = Conta(4321,"Rodrigo",300.0,1000.0)

conta2.transfere(10.0,conta)
conta.extrato()
conta2.extrato()

print(conta.limite)
conta.limite = 200.0
print(conta.limite)

conta.saca(1000.00)


