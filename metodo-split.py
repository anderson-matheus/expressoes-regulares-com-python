import re

text = ("para entrar em Contato\n"
		  "r. Alagoas, 1049 5º e 6º andares\n"
		  "Savassi - Belo Horizonte MG Brasil\n"
		  "+55 31 3261 8083\n"
		  "contato@ancieladvogados.com.br\n"
		  "11/08/2016")

lista = re.split(r'\n', text)
print(lista)

string = 'teste, teste, teste.'
lista = re.split(r'\W+', string, 2)
print(lista)