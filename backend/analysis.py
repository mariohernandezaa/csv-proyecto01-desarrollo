import csv

import pandas as pd

def analizar_csv(archivo):
    muestra = archivo.read(65536)
    archivo.seek(0)
    texto_muestra = muestra.decode("utf-8-sig", errors="replace")

    try:
        separador = csv.Sniffer().sniff(texto_muestra, delimiters=",;\t|").delimiter
    except csv.Error:
        separador = ","

    try:
        datos = pd.read_csv(archivo, sep=separador, encoding="utf-8-sig")
    except UnicodeDecodeError:
        archivo.seek(0)
        datos = pd.read_csv(archivo, sep=separador, encoding="latin-1")
        
    return {
        "filas": len(datos),
        "columnas": len(datos.columns),
        "tipos": datos.dtypes.astype(str).to_dict(),
        "ausentes_por_columna": datos.isna().sum().to_dict(),
        "ausentes_por_fila": datos.isna().sum(axis=1).tolist(),
    }