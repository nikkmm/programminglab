import csv


# Definizione di una specifica classe di eccezioni per il programma
class ExamException(Exception):
    pass


# Classe che gestisce la lettura di file CSV contenenti serie temporali
class CSVTimeSeriesFile:

    def __init__(self, name):
        # Inizializzazione con il nome del file
        self.name = name

    def get_data(self):
        try:
            # Apertura del file in modalità lettura
            with open(self.name, 'r') as file:
                reader = csv.reader(file)  # Creazione del lettore CSV
                data = []  # Lista per memorizzare i dati validi

                for row in reader:
                    # Controllo se la riga ha almeno due colonne
                    if len(row) < 2:
                        continue

                    try:
                        # Conversione di epoch a intero e temperatura a float
                        epoch = int(row[0])
                        temperature = float(row[1])
                        data.append([epoch, temperature
                                     ])  # Aggiunta dei dati validi alla lista
                    except ValueError:
                        # Ignora le righe con valori non convertibili
                        continue

                # Controllo se ci sono abbastanza dati validi nel file
                if len(data) < 2:
                    raise ExamException('Errore, pochi dati validi nel file')

                # Controllo se i dati sono ordinati per timestamp e senza duplicati
                for i in range(1, len(data)):
                    if data[i][0] <= data[i - 1][0]:
                        raise ExamException(
                            'Errore, timestamp non ordinati o duplicati')

                return data  # Ritorno dei dati validi

        except FileNotFoundError:
            # Gestione dell'errore se il file non è trovato
            raise ExamException('Errore, file non trovato')
        except Exception as e:
            # Gestione di altri tipi di errori nella lettura del file
            raise ExamException(f'Errore nella lettura del file: {e}')


# Funzione per calcolare la differenza massima giornaliera di temperatura
def compute_daily_max_difference(time_series):
    if not time_series:
        # Solleva un'eccezione se la lista di time series è vuota
        raise ExamException('Errore, lista valori vuota')

    daily_max_diff = [
    ]  # Lista per memorizzare le differenze massime giornaliere
    current_day = time_series[0][0] - (
        time_series[0][0] % 86400)  # Calcolo dell'inizio del giorno corrente
    daily_temps = [
    ]  # Lista per memorizzare le temperature di un singolo giorno

    for epoch, temperature in time_series:
        # Calcolo dell'inizio del giorno per il timestamp corrente
        day_start_epoch = epoch - (epoch % 86400)

        if day_start_epoch != current_day:
            # Se cambiamo giorno, calcoliamo la differenza massima del giorno precedente
            if len(daily_temps) > 1:
                daily_max_diff.append(max(daily_temps) - min(daily_temps))
            else:
                daily_max_diff.append(None)

            # Reset delle variabili per il nuovo giorno
            current_day = day_start_epoch
            daily_temps = [temperature]
        else:
            # Aggiunta della temperatura alla lista delle temperature del giorno corrente
            daily_temps.append(temperature)

    # Calcolo della differenza massima per l'ultimo giorno
    if len(daily_temps) > 1:
        daily_max_diff.append(max(daily_temps) - min(daily_temps))
    else:
        daily_max_diff.append(None)

    return daily_max_diff  # Ritorno della lista delle differenze massime giornaliere
# Esecuzione del test dell'implementazione con un file di dati campione 'data.csv'
if __name__ == "__main__":
    # Creazione dell'oggetto CSVTimeSeriesFile con il nome del file
    time_series_file = CSVTimeSeriesFile(name='data.csv')
    # Recupero dei dati dal file
    time_series = time_series_file.get_data()
    # Calcolo e stampa delle differenze massime giornaliere
    print(compute_daily_max_difference(time_series))