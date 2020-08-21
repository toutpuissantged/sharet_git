def db_check():
	from modules import sqlite3,hashlib
	tnum=0
	tb=1
	conn3=sqlite3.connect("virtual/system/base.db")
	cur3=conn3.cursor()
	cur3.execute("select money from info")
	for l in cur3:
	    liste_d=l
	hmoney=(liste_d[0])
	conn3.commit()
	cur3.close()
	conn3.close()
	while tb==1:
	    tb2=hashlib.sha224((bytes(str(tnum),'utf8'))).hexdigest()
	    if tb2==hmoney:
	        tb=0
	        tmoney=tnum
	    else:
	        tnum+=1
	return tmoney