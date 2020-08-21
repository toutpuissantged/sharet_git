# pour ecrire et lire les fichiers de configuration
file="virtual/system/config.cfx"

def conf_w(hosta,hostb,temp):

	fd=open(file,'w')
	fd.write(str(hosta)+"\n"+str(hostb)+"\n"+str(temp))
	fd.close()

def conf_r():
	fs=open(file,'r')
	l=fs.readlines()
	fs.close()
	return l[0],l[1],l[2]
if __name__ == '__main__':
	e,f,g=conf_r()
	print("e="+e+"f="+f+"g="+g)