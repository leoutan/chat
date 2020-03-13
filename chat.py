# import os
# name = 0
# chat = []
# if os.path.isfile('input.txt'):
# 	print('找到檔案')
# 	with open('input.txt', 'r') as f:
# 		for line in f:
# 			line = line.strip()
# 			if 'Allen' == line or 'Tom' == line:
# 				if line != name:
# 					name = line	
# 					continue
# 			chat.append(name + ':' +line + '\n')
# else:	
# 	print('找不到檔案')
# print(chat)

# with open('output.txt', 'w') as f:
# 	for c in chat:
# 		f.write(c)
def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:		
			new.append(person + ':' + line)
	return new
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():	
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
	return lines

lines = main()
print(lines)
