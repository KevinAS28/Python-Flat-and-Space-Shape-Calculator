#!/usr/bin/env python2
# -*- coding: utf-8 -*-


#import module
import os
import math

#membuat program berjalan terus
kalkulator = 'y'
while(kalkulator=='y'):

#menu utama
 print("""

@@@@@@@''''@@''''''@@
@@''''@@''''@@''''@@'
@@''''@@'''''@@''@@''
@@@@@@@@''''''@@@@'''
@@''''@@'''''''@@''''
@@''''@@'''''''@@''''
@@@@@@@''''''''@@''''

'@@''''@@''@@@@@@@@'''@@'''''@@'''@@@@@@@@' @@''''''''@@'''''''''@@@@@@@@'''@@@@@
'@@'''@@'''@@'''''''''@@'''''@@''''''@@'''''@@''''''''@@'''''''''@@''''@@'''@@'''
'@@''@@''''@@'''''''''@@'''''@@''''''@@'''''@@@@''''''@@'''''''''@@''''@@'''@@'''
'@@@@''''''@@@@@@@@''''@@'''@@'''''''@@'''''@@''@@''''@@'''''''''@@@@@@@@'''@@@@@
'@@''@@''''@@''''''''''@@'''@@'''''''@@'''''@@''''@@''@@'''''''''@@''''@@'''''''@
'@@'''@@'''@@'''''''''''@@@@@''''''''@@'''''@@''''''@@@@'''''''''@@''''@@'''''''@
'@@''''@@''@@@@@@@@'''''@@@@@'''''@@@@@@@@''@@''''''''@@'''''''''@@''''@@'''@@@@@

built in python 2.7
ShapeCal English version(translated by google translate)

Welcome to ShapeCal V0.1 


1.start calculate up space

2.start calculate up flat

3.about this program

4.author

insert number and hit enter

""")
 menu1 = input("your choice? ")
 
#menu bangun ruang
 if menu1==1:
  print("""
 
1.cube

2.cuboid

3.prism

4.pyramid

5.tube

6.cone

7.ball

insert number and hit enter

""")
  menu2 = input("your choice? ")
  if menu2==1:
 #menghitung kubus
   print("""

             _______________
            /|             |/
           / |             /
          /  |            /|
         /   |           / |
        /    |          /  |
       /_____|_________/   |
       |     |        |    |
       |     |        |    |
       |     |        |    |
       |     |        |    |
       |     |        |    |
       |     |--------|-----
       |              |   /
       |              |  /
       |              | /
       |______________|/
                       
in geometry, a cube is three-dimensional solid object bounded
by six square faces,facets or sides,with three meeting at each vertex. The cube
is the only regular hexahedron and is one of the five platonic solids
(more detail,visit https://en.m.wikipedia.org/wiki/Cube)

formula to calculate volume of cube is: V=s x s x s
formula to calculate the surface area of the cube is: SA=6 x s^2
explanation:

V = volume
s = side
SA = surface area


1.you want to calculate volume of a cube

2.you want calculate side of a cube

3.you want calculate surface area of a cube

insert number and hit enter

""")
   menukubus = input("your choice? ")
   
   #hitung v kubus
   if menukubus==1:
    carivkubus = input("how long is the ribs of the cube? ")
    vkubus = (float(carivkubus)*float(carivkubus)*float(carivkubus))
    print("the volume of that cube is "+str(vkubus))

   #hitung s kubus
   if menukubus==2:
    cariskubus = input("what is the volume of the cube? ")
    skubus = float(cariskubus)**(1.0/3.0)
    print("one of the broad sides of the cube is "+str(skubus))

   #hitung lp kubus
   if menukubus==3:
    y = 'y'
    n = 'n'
    tanyalpk = input("did you know what is the one of the broad sides of the cube is? Y/N ")
    if tanyalpk.lower() == "n":
     #hitung salah satu luas sisi kubus
     tanyalpk1 = input("how long one of the cube ribs? ")
     lsk = (float(tanyalpk1)*float(tanyalpk1))
     print("the broad sides of the cube is "+str(lsk))
    #hitung lp kubus
    else:
     tanyalpk2 = input("what is one of the broad sides of the cube? ")
     lpks = (float(tanyalpk2)*6)
     print("the surface area of the cube is "+str(lpks))




 #menghitung balok
  if menu2==2:
   print("""
   ________________________________
   /|                              /|
  / |                             / |
 /  |                            /  |
|-------------------------------/   |
|   |                           |   |
|   |                           |   |
|   |                           |   |
|   |---------------------------|--/
|  /                            | /
| /                             |/
|/______________________________/

in geometry,a cuboid is a convex polyhedron
bounded by six quadrilateral faces,whose
polyhedral graph is the same as that of a cube
(more detail,visit https://en.m.wikipedia.org/wiki/Cuboid)

the formula of the volume cuboid is: V  =  L x W x H

explanation:
V = volume
L = long
W = wide
H = height

1.you want to calculate volume of the cuboid

2.you want to calculate surface area of cuboid


insert number and hit enter?
""")

   tanyabalok = input("your choice? ")

   #hitung volume balok
   if tanyabalok==1:
    pbalok = input("Cuboid long? ")
    lbalok = input("cuboid wide? ")
    tbalok = input("cuboid height? ")
    vbalok = (float(pbalok)*float(lbalok)*float(tbalok))
    print("the volume of the cuboid is "+str(vbalok))

   #hitung lp balok
   if tanyabalok==2:
    pbalok = input("Cuboid long? ")
    lbalok = input("Cuboid wide? ")
    tbalok = input("Cuboid height? ")
    lpbalok = (float(pbalok*tbalok*4)+float(lbalok*tbalok*2))
    print("the surface area of the cuboid is "+str(lpbalok))


  #menghitung prisma
  if menu2==3:
   print("""

    Prism
             /|\
            / | \
           /  |  \
          /   |   \
         /    |    \
        /     |     \
       /      |      \
      /       |       \
     |_________________| 
     |        |        |
     |        |        |
     |        |        |
     |        |        |
     |        |        |
     |        |        |
     |        |        |
     |       / \       |
     |      /   \      |
     |     /     \     |
     |    /       \    |
     |   /         \   | 
     |  /           \  | 
     | /             \ | 
     |/               \| 
     |_________________| 
            
            Prism
(more detail,visit https://en.m.wikipedia.org/wiki/Prism)

formula for the volume of prism is: V = ba x H

V = Volume
ba = base area
H = Height

1.you want to calculate
2.anda ingin hitung v prisma
""")

   tanyapr = input("pilihan mu? ")
   if tanyapr==1:
    #hitung lp prisma
    y = 'y'
    n = 'n'
    tanyapr1 = input("apa kamu tahu luas alas prismanya? Y/N ")
    if tanyapr1.lower() == "n":
     print("""anda harus mencari luas alas tersebut
              dengan jalankan ulang program ini
              lalu ke menu bangun datar,lalu cari luas bentuknya
            """)
    if tanyapr1.lower() == "y":
     tanyapr2 = input("berapa luas alas prisma tersebut? ")
     tanyapr3 = input("berapa tinggi prisma tersebut? ")
     tanyapr4 = input("berapa sisi miring alas prisma tersebut? ")
     lppr = ((float(tanyapr2)*2)+(float(tanyapr3*tanyapr4*3)))
     print("luas permukaan prisma tersebut adalah "+str(lppr))


   #hitung v prisma
   if tanyapr==2:
    y = 'y'
    n = 'n'
    tanyapr5 = input("apa kamu tahu luas alas prismanya? Y/N ")
    if tanyapr5.lower() == "n":
     print("""anda harus mencari luas alas tersebut
              dengan jalankan ulang program ini
              lalu ke menu bangun datar,lalu cari luas bentuknya
            """)
    if tanyapr5.lower() == "y":
     tanyapr6 = input("berapa luas alas prisma tersebut? ")
     tanyapr7 = input("berapa tinggi prisma tersebut? ")
     vpr = ((float(tanyapr6))*(float(tanyapr7)))
     print("volume prisma tersebut adalah "+str(vpr))



#menghitung limas
  if menu2==4:
   print("""
limas yang akan anda hitung disini adalah limas beraturan dengan alas berbentuk persegi

rumus:

v = (1/3)*la*t

1.anda ingin mencari v limas

2.anda ingin mencari lp limas

""")
   tanyalm = input("pilihan mu ? ")
   #volume limas
   if tanyalm==1:
    y = 'y'
    n = 'n'
    tanyalm1 = input("apakah anda tahu luas alasnya? Y/N ")
    if tanyalm1.lower() == "n":
     print("""
anda harus mencari luas alas limas tersebut
dengan cara jalankan ulang program ini lalu ke menu ruang bangun datar
dan kemudian cari luas bentuknya
      """)
    if tanyalm1.lower() == "y":   
     tanyalm2 = input("berapa luas alas limas? ")
     tanyalm3 = input("berapa tinggi limas? ")
     vlimas = ((float(tanyalm2*tanyalm3/3)))
     print("volume limas tersebut adalah "+(str(vlimas)))


   #lp limas
   if tanyalm==2:
    y = 'y'
    n = 'n'
    tanyalm4 = input("apakah anda tahu luas alasnya? Y/N ")
    if tanyalm4.lower() == "n":
     print("""
anda harus mencari luas alas limas tersebut
dengan cara jalankan ulang program ini lalu ke menu ruang bangun datar
dan kemudian cari luas bentuknya
      """)
    if tanyalm4.lower() == "y":    
     tanyalm5 = input("berapa luas alas limas? ")
     tanyalm7 = input("berapa sisi miring prisma? ")
     sisilm = (math.sqrt(tanyalm5))
     seglm = (float(tanyalm7*sisilm)/2)
     lplimas = (float(tanyalm5+(seglm*4)))
     print("luas permukaan limas tersebut adalah "+str(lplimas))



#menghitung tabung
  if menu2==5:
   print("""

rumus volume tabung adalah

la x t atau (22/7)x(r^2)xt

ket:

la=luas alas
t=tinggi

1.anda ingin hitung v tabung
2.anda ingin hitung luas permukaan

  """)
   tanyatb = input("pilihan mu? ")
   if tanyatb==1:
    #hitung v tabung
    tanyatb = input("apakah anda tahu luas alasnya? Y/N ")    
    if tanyatb.lower() == "y":
     tanyatb1 = input("berapa luas alasnya? ")
     tanyatb2 = input("berapa tinggi tabung? ")
     vtbng = ((float(tanyatb1))*(float(tanyatb2)))
     print("volumenya adalah "+str(vtbng))
    else:
     tanyatb3 = input("berapa jari-jari alasnya? ")
     tanyatb4 = input("berapa tinggi tabung? ")
     latbng = (22*((float(tanyatb3))**2)/7)
     vtbng2 = ((float(latbng))*(float(tanyatb4)))
     print("volumenya adalah "+str(vtbng2))
   #by k3v1n-45
   if tanyatb==2:
    tanyatb = input("apakah anda tahu luas alasnya? Y/N ")    
    if tanyatb.lower() == "y":
     tanyatb1 = input("berapa luas alasnya? ")
     tanyatb2 = input("berapa tinggi tabung? ")
     jrtbng = math.sqrt((float(tanyatb1))*7/22)  #cari jari2 tabung lewat la
     kllatbng1 = (float(jrtbng*2))*22/7 #cari keliling la tabung
     latbng = (float(tanyatb1)*2)+((float(kllatbng1))*(float(tanyatb2)))
     print("luas permukaan tabung tersebut adalah "+str(latbng))
    else:
     tanyatb3 = input("berapa jari-jarinya? ")
     tanyatb4 = input("berapa tingginya? ")
     latbng2 = ((float(tanyatb3))**2)*22/7
     ktbng = (float(tanyatb3))*2*22/7
     lsstbng = (float(tanyatb4))*(float(ktbng))
     lptbng1 = (float(lsstbng))+((float(latbng2))*2)
     print("luas permukaan tabung tersebut adalah "+str(lptbng1))



#menghitung kerucut
  if menu2==6:
   print("""

rumus volume kerucut adalah:

v = (1/3)*la*t

1.anda ingin mencari v kerucut

2.anda ingin mencari lp kerucut

""")
   tanyalm10 = input("pilihan mu ? ")
   #volume limas
   if tanyalm10==1:
    y = 'y'
    n = 'n'
    tanyalm1 = input("apakah anda tahu luas alasnya? Y/N ")
    if tanyalm1.lower() == "n":
     print("""
anda harus mencari luas alas kerucut tersebut
dengan cara jalankan ulang program ini lalu ke menu ruang bangun datar
dan kemudian cari luas bentuknya
      """)
    else:   
     tanyakc2 = input("berapa luas alas kerucut? ")
     tanyakc3 = input("berapa tinggi kerucut? ")
     vkc = ((float(tanyakc2*tanyakc3/3)))
     print("volume kerucut tersebut adalah "+(str(kc)))


   #lp kerucut
   if tanyalm10==2:
    y = 'y'
    n = 'n'
    tanyalm4 = input("apakah anda tahu luas alasnya? Y/N ")
    if tanyalm4.lower() == "n":
     print("""
anda harus mencari luas alas kerucut tersebut
dengan cara jalankan ulang program ini lalu ke menu ruang bangun datar
dan kemudian cari luas bentuknya
      """)
    else:    
     y = 'y'
     n = 'n'
     tanyakc = input("apakah anda tahu berapa panjang sisi miring kerucutnya? Y/N ")
     if tanyakc.lower() == "y":
      tanyalm5 = input("berapa luas alas kerucut? ")
      tanyalm7 = input("berapa sisi miring kerucut? ")
      jrlakc = math.sqrt((float(tanyalm5))*7/22) #jari-jari
      lpkc = (22*(float(jrlakc))*((float(jrlakc))+(float(tanalm7)))/7)    #rumus pi r(r+s)
      print("luas permukaan kerucut adalah "+str(lpkc))
     else:
      tanyakcr = input("berapa jari-jarinya? ")
      tanyakcr1 = input("berapa tinggi kerucutnya? ")
      skrc = math.sqrt(((float(tanyakcr))**2)+((float(tanyakcr1))**2))
      print("sisi miringnya adalah "+str(skrc))





  #hitung bola
  if menu2==7:
   print("""
bola itu agak unik

rumus v bola: (4 : 3) X (22 / 7) X (r^3)

1.anda ingin mencari v bola

2.anda ingin mencari r jari-jari

  """)
   tanyabo = input("pilihan mu? ")
   if tanyabo==1:
    tanyabo1 = input("berapa jari-jarinya? ")
    vbo = (4*22*(float(tanyabo1**3))/7/3)
    print("volume bolanya adalah "+str(vbo))
   else:
    tanyabo2 = input("berapa volume bola tersebut? ")
    rbo = ((float(tanyabo2))*7*3/22/4)
    rbo1 = (float(rbo))**(1.0/3.0)
    print("jari-jari bola tersebut adalah "+str(rbo1))
    




#menghitung bangun datar
 if menu1==2:
  print("""

bangun datar apa yang ingin anda hitung?

1.persegi
2.persegi panjang
3.trapesium
4.lingkaran
5.segitiga
6.layang-layang
7.jajargenjang
8.belah ketupat

ketik nomor lalu enter

""")

  tanyadatar = input("yang mana pilihan mu? ")
  if tanyadatar==1:
   #menghitung persegi
   print("""
persegi

rumus luas persegi adalah S x S atau S^2
sedangkan rumus keliling persegi adalah S x 4

1.anda ingin menghitung luas persegi
2.anda ingin menghitung keliling persegi
3.anda ingin mencari sisi persegi
  
pilih nomor, lalu enter

 """)

   tanyaps = input("pilihan mu? ")
#   if tanyaps

 
 if menu1==3: #about this program
  print("""

ShapeCalc v0.1 (english version)
by Kevin Agusto
this is my first program that i made it with serious
take 2 weeks to made it(2 hours/day)

this program is open-source
which mean,you can edit this program
and share to your friends.

Source:

WikiPedia (https://www.wikipedia.org)
Google Translate (https://translate.google.com)
Learn Python (https://sololearn.com)



thanks to:

God (help and let me create this program)
you (using it)
Guido van Rossum (python creator)
people from SoloLearn (help me to solve this program trouble)
wikipedia (definition and other information)
and else

""")


#author
 if menu1==4:
  print("""

Kevin Agusto
email: kevinagusto28@gmail.com
from:indonesia

im new in programming and having
dream to mastering 8 diffrent programming languages.

if you like it, i dont ask any money.just pray for me
so i can reach my dream ;v

found any bugs?
im so glad if u can tell me to my email

""")
  
 y = 'y'
 n = 'n'
 kalkulator = input("want to restart this program Y/N? ")
 
