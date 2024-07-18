class Testo(str):
    pass

mytxt = Testo('je passse ces exams')

print(mytxt)

shfile= open('shampoo_sales.csv','r')
print(shfile.readline())
print(shfile.readline())
print(shfile.readline())

mia_stringa = 'Ciao, come va?'
lista_elementi = mia_stringa.split(',')
print(lista_elementi)
