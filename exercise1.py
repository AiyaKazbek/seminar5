try:
	fhand = open('mailbox.txt')
except:
	print('File cannot be opened:', fname)
	exit()

lines=fhand.readlines()
a=open('output.txt','w')
for line in lines:
	if line.startswith("Message-ID:"):
		ab=line[13:40]
		print(ab)
		a.write(ab)
fhand.close()
