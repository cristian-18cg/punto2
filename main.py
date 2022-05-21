print("Por favor digite 20 valores")
lista=[]
x=0
for i in range(20):
 num=int(input(f"Digite el valor[{i+1}]:"))
 lista.append(num)
for i in range(1,len(lista)):
  for j in range(0,len(lista)-i):
    if(lista[j+1] > lista[j]):
      lista[j],lista[j+1]=lista[j+1],lista[j]      
print(lista)