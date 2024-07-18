import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            with open(self.name, 'r') as file:
                reader = csv.reader(file) 
                data = []  

                for row in reader:

                    if len(row) < 2:
                        continue

                    try:

                        epoch = int(row[0])
                        temperature = float(row[1])
                        data.append([epoch, temperature])  
                    except ValueError:

                        continue

                if len(data) < 2:
                    raise ExamException('Errore, pochi dati validi nel file')

                for i in range(1, len(data)):
                    if data[i][0] <= data[i-1][0]:
                        raise ExamException('Errore, timestamp non ordinati o duplicati')

                return data  

        except FileNotFoundError:
            raise ExamException('Errore, file non trovato')
        except Exception as e:
            raise ExamException(f'Errore nella lettura del file: {e}')

def compute_daily_max_difference(time_series):
    if not time_series:
        raise ExamException('Errore, lista valori vuota')

    daily_max_diff = []  
    current_day = time_series[0][0] - (time_series[0][0] % 86400)  
    daily_temps = []  

    for epoch, temperature in time_series:
        day_start_epoch = epoch - (epoch % 86400)

        if day_start_epoch != current_day:
            if len(daily_temps) > 1:
                daily_max_diff.append(max(daily_temps) - min(daily_temps))
            else:
                daily_max_diff.append(None)

            current_day = day_start_epoch
            daily_temps = [temperature]
        else:
            daily_temps.append(temperature)

    if len(daily_temps) > 1:
        daily_max_diff.append(max(daily_temps) - min(daily_temps))
    else:
        daily_max_diff.append(None)

    return daily_max_diff 


