def intro():

	from modules import welcome,dire,base,conf_w

	#global hosta,hostb,version,temp

	dire.dir.dir_maker()

	welcome.w1.welcome()

	base.base_check()

	defo=input('use your recent settings  ?(Y/n) : ')
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
		hosta,hostb,temp=base.ip_rd()
		temp=int(temp)

	base.ip_base(hosta,hostb,temp)

	return hosta,hostb,temp

if __name__ == '__main__':
    pass
