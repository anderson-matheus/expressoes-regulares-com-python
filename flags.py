import re

text = ("Para entrar em Contato\n"
		  "R. Alagoas, 1049 5º e 6º andares\n"
		  "Savassi - Belo Horizonte MG Brasil\n"
		  "+55 31 3261 8083\n"
		  "contato@ancieladvogados.com.br\n"
		  "11/08/2016")

# pattern = re.compile(r'[a-z].+$', re.M|re.I)
pattern = re.compile(r'^.*$', re.M|re.I|re.DOTALL)
lista = pattern.findall(text)
print(lista)