#Par Qianyun Shen
import turtle
import random
pen = turtle.Turtle()
screen = turtle.Screen()
#prend un  prend un entier n  et retourne un tableau de longueur n 
def iota(n):
	liste= []
	while n > 0:
		liste.append(n-1)
		n -=1
		liste.sort()
	return liste
assert(iota(5))==[0,1,2,3,4]


#prend un tab et un nombre x et retourne un booléen si x est contenu
def contient(tab,x):
	for i in range(len(tab)):
		if tab[i] == x:
			return True
	else:
		return False
assert(contient([9,2,5],7))==False
assert(contient([9,2,5],2))==True


#si x n'a pas dans tab ,ajouter
def ajouter(tab,x):
	if x not in tab:
		tab.append(x)
	else:
		return tab
	return tab
assert(ajouter([9,2,5],2)) == [9,2,5]
assert(ajouter([9,2,5],7))==[9,2,5,7]

#si x dans tab ,retirer
def retirer(tab,x):
	if x in tab:
		tab.remove(x)
	return tab
assert(retirer([9,2,5],2))==[9,5]
assert(retirer([9,2,5],7))==[9,2,5]


#prend la coordonnée(x,y)d'une cellule et la taille d'une grille,retourne
#un tableau contenant le numéro des cellules voisines.
def voisine(x,y,nx,ny):
	#voisin on the top
	c1 = x+(y-1)*nx
	#voisin on the left
	c2 = x+y*nx-1
	#voisin below
	c3 = x+(y+1)*nx
	#voisin on the right
	c4 = x+y*nx+1
	if x == 0 and y == 0:
		return [c3,c4]
	elif x == 0 and y == ny -1:
		return[c1,c4]
	elif x == 0:
		return [c1,c3,c4]
	elif x==nx-1 and y == 0:
		return [c2,c3]
	elif x ==nx-1 and y ==ny-1:
		return [c1,c2]
	elif x == nx-1:
		return [c1,c2,c3]
	elif y == ny-1:
		return [c1,c2,c4]
	elif y == 0:
		return[c2,c3,c4]
	else:
		return[c1,c2,c3,c4]
assert(voisine(7,2,8,4))==[15,22,31]
assert(voisine(3,2,8,4))==[11,18,27,20]

#crée un labyrinthe alétoire
def laby(nx,ny,pas):
	murH = iota(nx*(ny+1)) #l’ensemble de murs horizontaux qui n'ont pas été retirés
	murV = iota((nx+1)*ny) #l’ensemble de murs verticaux qui n'ont pas été retirés
	cave = [0] # l’ensemble des cellules qui ont ´et´e mis dans la cavit´e par l’algorithme
	front = [] #l’ensemble des cellules qui sont voisines des cellules dans la cavité
	length_half = ny*pas/2
	width_half = nx*pas/2
	
	for i in range(0,ny+1):
		pen.pu()
		pen.goto(-width_half,length_half-pas*i)
		pen.pd()
		pen.goto(width_half,length_half-pas*i)
		pen.pu()
	for j in range(0,nx+1):
		pen.goto(width_half-pas*j,-length_half)
		pen.pd()
		pen.goto(width_half-pas*j,length_half)
		pen.pu()
	pen.up()
	pen.goto(-width_half,length_half)
	pen.color("white")
	pen.pd()
	pen.goto(-width_half+pas,length_half)
	pen.up()
	pen.goto(width_half,-length_half)
	pen.pd()
	pen.goto(width_half-pas,-length_half)
	retirer(murH,(nx+1)*ny-1)
	retirer(murH,0)
	x = 0
	y = 0
	for i in voisine(x,y,nx,ny):
		ajouter(front,i)
	while len(front)<nx*ny :
		cellule = random.choice(voisine(x,y,nx,ny))
		if contient(cave,cellule)==False:
		 
			ajouter(cave,cellule)
			retirer(front,cellule)
			for i in voisine(x,y,nx,ny):
				ajouter(front,i)

			pen.color("white")
			# cellule on the right
			if cellule - (x+y*nx)==1:
				pen.up()
				pen.goto(-width_half+pas*(x+1),length_half-pas*y)
				pen.down()
				pen.goto(-width_half+pas*(x+1),length_half-pas*(y+1))
				murV.remove(cellule+y)
			#cellule on the left
			elif cellule -(x+y*nx)==-1:
				pen.up()
				pen.goto(-width_half+pas*(x),length_half-pas*(y))
				pen.down()
				pen.goto(-width_half+pas*(x),length_half-pas*(y+1))
				murV.remove(cellule+y+1)
			# cellule below	
			elif cellule-(x+y*nx)==nx:
				pen.up()
				pen.goto(-width_half+pas*(x),length_half-pas*(y+1))
				pen.down()
				pen.goto(-width_half+pas*(x+1),length_half-pas*(y+1))
				murH.remove(cellule)
			#cellule on the top	
			elif cellule-(x+y*nx)==-nx:
				pen.up()
				pen.goto(-width_half+pas*x,length_half-pas*(y))
				pen.down()
				pen.goto(-width_half+pas*(x+1),length_half-pas*(y))
				murH.remove(cellule+nx)
				
			
		else:
			print('')
		x = cellule%nx
		y = cellule//nx
	return murH,murV
def labySol(nx,ny,pas):
	length_half = ny*pas/2
	width_half = nx*pas/2
	mur = laby(nx,ny,pas)
	murH = mur[0]
	murV = mur[1]
	#Assurer que la tortue est au milieu de la cellule
	rouge_pas = pas/3
	rouge_pas_2 = 2*pas/3
	pen.color("red")
	pen.penup()
	pen.goto(-width_half,length_half)
	pen.forward(rouge_pas)
	pen.rt(90)
	pen.pendown()
	rouge_x = (pen.xcor()+width_half)//pas
	rouge_y = (length_half- pen.ycor())//pas 
	avoir_murH = []
	avoir_murV = []
	for j in range(1,ny+1):
		for i in murH:
			if i == rouge_x +nx*j:
				avoir_murH.append(j)
	
	pen.forward((avoir_murH[0]-1)*pas+rouge_pas_2)
	pen.lt(90)
	for j in range(1,nx+1):
		for i in murV:
			rouge_x = (pen.xcor()+width_half)//pas
			rouge_y = (length_half- pen.ycor())//pas 
			if i == rouge_y+ny*j:
				avoir_murV.append(j)
	pen.forward((avoir_murV[0]-1)*pas+rouge_pas_2)



	
	
pen.hideturtle()
pen.speed(0)
labySol(9,6,50)
screen.exitonclick()
