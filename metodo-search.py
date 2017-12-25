import re

text = ("para entrar em Contato "
		  "r. Alagoas, 1049 5º e 6º andares "
		  "Savassi - Belo Horizonte MG Brasil "
		  "+55 31 3261 8083 "
		  "contato@ancieladvogados.com.br "
		  "11/08/2016")

# pattern = r'[A-Z]\w+'
# pattern = r'[0-9]\w+'
pattern = r'\+\d{2} \d{2} \d{4} \d{4}'
match = re.search(pattern, text)

if match:
	print(match.group())