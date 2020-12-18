strA = []
strB = []

ind_A = []
ind_B = []

toplamA = 0
toplamB = 0

strA = input()
for i in range(0,10):
   num = int(input())
   ind_A.append(num)

strB = input()
for i in range(0,10):
   num2 = int(input())
   ind_B.append(num2)


liste_strA = list(strA) 
liste_strB = list(strB)

for i in ind_A:
   liste_strB[i] = "-1"
for i in range(0,10):
   liste_strB.remove("-1")

   
for i in ind_B:
   liste_strA[i] = "-1"
for i in range(0,10):
   liste_strA.remove("-1")


for i in range(0,16):
   if(ord(liste_strA[i]) > ord(liste_strB[i])):
      sonuc = ord(liste_strA[i]) - ord(liste_strB[i])
      toplamA += sonuc
   elif(ord(liste_strA[i]) < ord(liste_strB[i])):
      sonuc = ord(liste_strB[i])-ord(liste_strA[i]) 
      toplamB += sonuc
   else:
      pass

son = {"A":toplamA,"B":toplamB}
print(son)
