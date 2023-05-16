a = 80000
b = 200000
ano = 0

while a <= b:
	a=(a*1.03)**ano
	b=(b*1.015)**ano
	ano=ano+1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )
