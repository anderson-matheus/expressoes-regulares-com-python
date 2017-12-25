import re

text = ("para entrar em Contato "
		  "r. Alagoas, 1049 5º e 6º andares "
		  "Savassi - Belo Horizonte MG Brasil "
		  "+55 31 3261 8083 "
		  "contato@ancieladvogados.com.br "
		  "11/08/2016")

# pat = r'\b(\d\d)\/(\d\d)\/(\d{4})'
pat = r'(\w+)@(\w+)([.com.br]+)'
m = re.search(pat, text)

if m:
	print(m.group(0))
	print(m.group(1))
	print(m.group(2))
	print(m.group(3))
	print(m.span())
	print(m.start())
	print(m.end())