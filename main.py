import sys
sys.path.append('..')
import pandas as pd
import requests
import schedule
import time
from datetime import datetime, timedelta
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s",
)

from config import PATH_OUTPUT_DATA

# funcion para extraer datos por rango de fechas
def extraer_datos(end_point, fecha_ini, fecha_fin):
    url = "http://10.1.0.103:9080/Utea/" + end_point
    params = {
        "pStrFecIni": fecha_ini,
        "pStrFecFin": fecha_fin,
    }
    response = requests.get(url, params=params)
    data = None
    if response.status_code == 200:
        data = response.json()
        now = datetime.now()
        logging.info(f"Se extrajo datos correctamente de: {end_point}")
    else:
        logging.info(f"Error el obtener datos de: {end_point}: {response.status_code}")
    return data

#get fechas

def ejecutar_tareas():
    ayer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    logging.info(f"Obteniendo datos de fecha: {ayer}")
    #extraer datos de API
    ReportePlaya = extraer_datos("ReportePlaya", ayer, ayer)
    TrafCamBalanza = extraer_datos("TrafCamBalanza", ayer, ayer)
    Molienda = extraer_datos("Molienda", ayer, ayer)
    
    df_ReportePlaya = pd.DataFrame(ReportePlaya)
    df_TrafCamBalanza = pd.DataFrame(TrafCamBalanza)
    df_Molienda = pd.DataFrame(Molienda)

    df_ReportePlaya.to_excel(PATH_OUTPUT_DATA + 'ReportePlaya.xlsx', index=False)
    df_TrafCamBalanza.to_excel(PATH_OUTPUT_DATA + 'TrafCamBalanza.xlsx', index=False)
    df_Molienda.to_excel(PATH_OUTPUT_DATA + 'Molienda.xlsx', index=False)
    
    logging.info(f"Se guardaton los datos en: {PATH_OUTPUT_DATA}")


def main():
    ejecutar_tareas()
    
    schedule.every().day.at("08:00").do(ejecutar_tareas)
    
    logging.info(f"⏳ Esperando a la hora programada...")

    # Loop infinito que mantiene vivo el proceso
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()