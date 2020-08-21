class calc():
		
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

if __name__ == '__main__':
    pass
