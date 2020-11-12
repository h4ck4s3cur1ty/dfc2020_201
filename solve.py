import string
import re
from datetime import datetime

f = open('mem.raw', 'rb')

string_a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()\!*#$%&-./:<=>?@_{}~ '
def is_printable(s):
	return filter(lambda x: x in string_a, s)

def is_number(value):
	try:
		return float(value)
	except ValueError:
		return False

offset = []
for i in re.finditer('#158676', f.read()):
	offset.append(i.start())

#offset = [1026978096, 1026978144, 1026978224, 1026978448, 1026978512, 1026978576, 1026978832, 1026979056, 1026979120, 1026979280, 1026979344, 1026979472, 1026980064, 1026980160, 1026980272, 1026980416, 1026980480, 1026980544, 1026980624, 1026980688, 1026980752, 1026980816, 1569726480, 1569726560, 1569726592, 1569726624, 1569726832, 1651620016, 1651620448, 1805290952, 1805291204, 2389983400L, 2389985440L, 2389985644L, 2930739404L, 2930739536L, 5011452464L]

last_offset = []
for i in range(len(offset)):
	try:
		if offset[i+1]-offset[i] > 10000000:
			last_offset.append(offset[i])
	except:
		pass

len1 = last_offset[0] - offset[0]
len2 = last_offset[1] - offset[offset.index(last_offset[0])+1]
len3 = last_offset[2] - offset[offset.index(last_offset[1])+1]
len4 = last_offset[3] - offset[offset.index(last_offset[2])+1]
len5 = last_offset[4] - offset[offset.index(last_offset[3])+1]
len6 = last_offset[5] - offset[offset.index(last_offset[4])+1]

data = ''
f.seek(offset[0])
data += f.read(len1)

f.seek(offset[offset.index(last_offset[0])+1])
data += f.read(len2)

f.seek(offset[offset.index(last_offset[1])+1])
data += f.read(len3)

f.seek(offset[offset.index(last_offset[2])+1])
data += f.read(len4)

f.seek(offset[offset.index(last_offset[3])+1])
data += f.read(len5)

f.seek(offset[offset.index(last_offset[4])+1])
data += f.read(len6)

hist = is_printable(data).split('#')

for i in range(len(hist)):
	data = hist[i].split('P')
	if data[0] != '':
		data2 = '\n'.join(data)
		time = datetime.utcfromtimestamp(is_number(data2[:10])).strftime('%Y-%m-%d %H:%M:%S')
		hist_data = data2[10:] + '\n'
		print time
		print hist_data
