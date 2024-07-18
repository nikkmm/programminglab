import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            with open(self.name, 'r') as file:
                data = []
                previous_date = None

                for line in file:
                    elements = line.strip().split(',')
                    if len(elements) < 2:
                        continue
                    if elements[0] != 'date':
                        try:
                            date = elements[0]
                            passengers = int(elements[1])
                            if passengers < 0:
                                continue

                            if previous_date is not None:
                                if date <= previous_date:
                                    raise ExamException('Date non ordinate o duplicate')

                            previous_date = date

                            data.append([date, passengers])
                        except ValueError:
                            continue

            return data
        except FileNotFoundError:
            raise ExamException('File non trovato')

def detect_similar_monthly_variations(time_series, years):
    if len(years) != 2:
        raise ExamException('La lista degli anni deve contenere esattamente due elementi')

    first_year, second_year = years
    first_year = str(first_year)
    second_year= str(second_year)

    if int(second_year)-int(first_year) != 1:
        raise ExamException('Gli anni devono essere consecutivi e in ordine crescente')

    years_present = [entry[0].split('-')[0] for entry in time_series]
    if first_year not in years_present or second_year not in years_present:
        raise ExamException('Anni non presenti nella serie temporale')

    # Filtra i dati per gli anni specificati
    filtered_data = [entry for entry in time_series if first_year <= entry[0].split('-')[0] <= second_year]

    # Organizza i dati per anno
    monthly_data = {}
    for date, passengers in filtered_data:
        year, month = date.split('-')
        year = int(year)
        month = int(month)
        if year not in monthly_data:
            monthly_data[year] = [None] * 12
        monthly_data[year][month - 1] = passengers

    variations = []
    for i in range(11): # Consideriamo 11 coppie di mesi
        if monthly_data[int(first_year)][i] is not None and monthly_data[int(first_year)][i+1] is not None and \
           monthly_data[int(second_year)][i] is not None and monthly_data[int(second_year)][i+1] is not None:
            diff1 = monthly_data[int(first_year)][i+1] - monthly_data[int(first_year)][i]
            diff2 = monthly_data[int(second_year)][i+1] - monthly_data[int(second_year)][i]
            variations.append(abs(diff1 - diff2) <= 2)
        else:
            variations.append(False)

    return variations

# Example of usage
time_series_file = CSVTimeSeriesFile('data2.csv')
time_series = time_series_file.get_data()
years = [1949, 1951]
result = detect_similar_monthly_variations(time_series, years)
print(result)