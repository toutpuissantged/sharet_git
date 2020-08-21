  
class w1():        
# calculer de la validite du code

    def welcome():
        """     """
        from modules import version
        from modules import time
        from modules import mode
        print(mode)
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

if __name__ == '__main__':
    pass