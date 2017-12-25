import re

# O match compara o começo da string

lista = ['1teste', '4qualquer', 'maisuma5', 'teste6']

pat1 = r'^\d'
pat2 = r'.*\d$'
for element in lista:
	m = re.match(pat1, element)
	if m:
		print('START: ', element)

	m = re.match(pat2, element)
	if m:
		print('	END: ', element)