# optimisation par  compression 

def compress_a(data,lon4,unit3):

    from modules import zlib

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

if __name__ == '__main__':
    pass
