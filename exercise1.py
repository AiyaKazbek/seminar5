try:
	file1=open('mailbox.txt')
except:
	print('File cannot be opened')
	exit()

lines=file1.readlines()

file2=open('output.txt','w')
for line in lines:
	if line.startswith("Message-ID:"):
		word=line[13:40]
		print(word)
		file2.write(word)
file1.close()
