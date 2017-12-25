import re

# O match compara o começo da string

lista = ['1teste', '4qualquer', 'maisuma5', 'teste6']

path1 = r'^\d'
path2 = r'.*\d$'
for element in lista:
	m = re.match(path1, element)
	if m:
		print('START: ', element)

	m = re.match(path2, element)
	if m:
		print('	END: ', element)