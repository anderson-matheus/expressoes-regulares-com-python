import re

text = ("Hoje acordei as 06:00hrs e tomei meu café da manhã as 06:30hrs "
		  "Logo depois fui correr, corri 10km em 40 minutos, ouvindo CPM22 "
		  "voltei para casa e tomei um banho e fui sai para trabalhar as 8:30hrs "
		  "voltei para casa as 18:00hrs e jantei as 19:00hrs")

# pattern = re.compile(r'\w+')
# pattern = re.compile(r'(?i)\b[a-z]')
pattern = re.compile(r'(\d\d):(\d\d)')
m = pattern.findall(text)

if m:
	print(m)