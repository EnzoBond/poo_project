from exercise6 import ContaBancaria

conta1 = ContaBancaria("Enzo", 10000.00)

print(f"O titular é {conta1.get_titular()} e o saldo é R${conta1.get_saldo():.2f}")

conta1.set_titular("Enzo Gabriel")
conta1.set_saldo(2000.00)
print(f"O titular é {conta1.get_titular()} e o saldo é R${conta1.get_saldo():.2f}")

conta1.set_titular("")
conta1.set_saldo(-500)