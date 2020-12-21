n = int(input())
liste = []
liste2 = []
str = input()
liste = str.split(" ")

yeni_liste = list(map(int,liste))
yeni_liste.sort()
for i in range(0,n):
   if(int(yeni_liste[i]) / 10 == 0):
      liste2.append(0)
   else:
      liste2.append(int(int(yeni_liste[i]) / 10))
yeni_liste_stemp = list(liste2)

liste2 = []
for i in range(0,n):
   if(int(yeni_liste[i]) / 10 == 0):
      liste2.append(0)
   else:
      liste2.append(int(int(yeni_liste[i]) % 10))
yeni_liste_leaf = list(liste2)

print("'",end="")
counter=0
lenstemp=len(yeni_liste_stemp)
for i in range(0,lenstemp):
    if(i==lenstemp-1):
        if(yeni_liste_stemp[i]!=yeni_liste_stemp[i-1]):
            print("' '",end="")
            print(yeni_liste_stemp[i],"|",yeni_liste_leaf[i],end="")
            print("'",end="")
        else:
            print(yeni_liste_leaf[i])
            print(",",end="")
    else:
        if(i==0):
            print(yeni_liste_stemp[i],"|",yeni_liste_leaf[i],end="")
        elif(yeni_liste_stemp[i]==yeni_liste_stemp[i-1]):
            print(" ",end="")
            print(yeni_liste_leaf[i],end="")
        else:
            print("' '",end="")
            print(yeni_liste_stemp[i],"|", yeni_liste_leaf[i], end="")
