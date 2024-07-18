def stampa(list):
    print('contenuto della list :', list)

def statistiche(list):
    if(all(type(x)==int for x in list)):
        somma=sum(list)
        media= somma/len(list) if list else 0
        minimo= min(list)
        massimo=max(list)
        print(f'la somma :{somma},media: {media}, minimo={minimo},massimo={massimo}')
               
        
def somma_vettoriale(list,list1):
    if (all(type(x)==int) for x in list) and (all(type(x)==int for x in list1)):
        if(len(list)==len(list1)):
            somma=[x+y for x,y in zip(list,list1)]
            return somma
        else :
            return []
    else : 
        return []
        
lista1=[1,2,3,4,5]
lista2=[0,2,4,6,8]
lv=[]

print('test de la fonction statistiche: ')
statistiche(lista1)
statistiche(lista2)


somma_vettoriale(lista1,lista2)
print('test de la fonction statistiche: ')
