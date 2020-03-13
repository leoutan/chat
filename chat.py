import os
name = 0
chat = []
if os.path.isfile('input.txt'):
	print('找到檔案')
	with open('input.txt', 'r') as f:
		for line in f:
			line = line.strip()
			if 'Allen' == line or 'Tom' == line:
				if line != name:
					name = line	
					continue
			chat.append(name + ':' +line + '\n')
else:	
	print('找不到檔案')
print(chat)

with open('output.txt', 'w') as f:
	for c in chat:
		f.write(c)