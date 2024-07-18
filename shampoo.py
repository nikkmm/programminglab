

values = []
# Apro e leggo il file, linea per linea
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
 # Faccio lo split di ogni riga sulla virgola
 elements = line.split(',')

if elements[0] != 'Date':
 # Setto la data e il valore
    date = elements[0]
    value = elements[1]
    values.append(value)
print(values)

def sum_csv(my_file):
    for i in 
            sum=sum(values)
            return sum
print(sum)