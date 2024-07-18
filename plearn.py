x= 'nika'
print(f'my name is {x}')

lista= [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,6,7,88,9,]

a=lista[4]
b= lista[1:3]
c=lista[-10]
print(a)
print(b)
print(c)

my_dict1= {'Trieste': 34100, 'Padova': 35100} # diz. di numeri
my_dict = {'Trieste': 'TS', 'Padova': 'PD'} # diz. di stringhe
CAP_ts = my_dict1['Trieste'] 
print(CAP_ts)
for i, item in enumerate(lista):
    print(f'Posizione {i}: {item}')
