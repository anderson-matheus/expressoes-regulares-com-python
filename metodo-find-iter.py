
import re

with open('arquivo.html', 'r') as f:
	text = f.read()

pat = re.compile(r'(http?s://)(\w+)\.(\w+\.?\w+?)\/(\w+)')

for m in pat.finditer(text):
	http = m.group(1)
	domain = m.group(2)
	region = m.group(3)
	path = m.group(4)
	print(m.group())
	string = 'http: {0}, doman: {1}, region: {2}, path: {3}'.format(http, domain, region, path)
	print(string)