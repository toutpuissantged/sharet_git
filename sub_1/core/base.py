# gestion de la base de donnee
class base():

    def base_check():
        from modules import sqlite3,hashlib,random
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

    def ip_base(hosta,hostb,temp):
        from modules import sqlite3
        donn=(hosta,hostb,str(temp))
        try:
            conn=sqlite3.connect("virtual/system/ip.db")
            cur=conn.cursor()
            cur.execute("create table ip (self_ip,other_ip, time ) ")
            cur.execute("insert into ip (self_ip,other_ip, time ) values(?,?,?)" ,donn)
            conn.commit()
            cur.close()
            conn.close()
        except sqlite3.OperationalError:
            conn=sqlite3.connect("virtual/system/ip.db")
            cur=conn.cursor()
            cur.execute("insert into ip (self_ip,other_ip, time ) values(?,?,?)" ,donn)
            conn.commit()
            cur.close()
            conn.close()
        #print("base de donne ecrit avec succes")

    def ip_rd():

        from modules import sqlite3
        
        conn2=sqlite3.connect("virtual/system/ip.db")
        cur=conn2.cursor()
        cur.execute("select self_ip from ip")
        for l in cur:
            d=l
        cur.execute("select other_ip from ip")
        for l in cur:
            s=l
        cur.execute("select time from ip")
        for l in cur:
            n=l
        
        return d[0],s[0],n[0]


if __name__ == '__main__':
    pass