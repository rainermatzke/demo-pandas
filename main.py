import os
import gzip
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    # Bestimme Pfad zur CSV Datei und lade diese
    path = os.getcwd()
    f = gzip.open(str(f'{path}/names.csv.gz'), 'r') # Hilfsfunktion um CSV Datei im Memory zu entpacken
    df = pd.read_csv(f)
    print(df.info())

    # Filter die CSV nach dem Jahr 1910 und zeige die ersten Zeilen an
    df_1910 = df[df.Year == 1910]
    print(df_1910.head())

    # Zeige statistische Infos zu den Daten von 1910
    print(df_1910.describe())

    dfnames = df.groupby('Name')['Count'].agg(['sum']).sort_values('sum').reset_index()
    print(dfnames.head())
    print(dfnames.tail())

    for name in ['Felix', 'Linus', 'Brigitte', 'Rainer', 'Reiner', 'Gitti']:
        res = dfnames[(dfnames['Name'] == name)].reset_index()
        if len(res) > 0:
            print(f"Anzahl {name} über alle Jahre: {str(res.at[0, 'sum'])}")
        else:
            print(f"Kein Treffer für {name}")
