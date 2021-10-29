filename=input("File atyn engiz:")
try:
	file1=open(filename)
except:
	print('File cannot be opened')
	exit()

lines=file1.readlines()

file2=open('output.txt','w')
for line in lines:
	if line.startswith("Message-ID:"):
		word=line[13:40]
		file2.write(word)
		file2.write('\n')
file1.close()
