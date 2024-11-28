import pandas as pd
import os
import warnings
import uuid

# Suprimir warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Ruta del archivo Excel
file_path = 'Azaleia - (POS)Usuario.Tienda.Almacen (version 1) 24072024 SM.xlsx'

# Verificar si el archivo existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo {file_path} no se encontró.")

# Cargar el archivo Excel
df = pd.read_excel(file_path, sheet_name='Series')

df = df[df["CONTINGENCIA"] == "NO"]

df['id_correlative'] = range(106, len(df) + 106)

df_csv = df[["id_correlative"]].copy()
df_csv["tx_company_code"] = "AZALEIA"
df_csv["tx_createdate"] = '2023-10-07 20:02:04'
df_csv["tx_status"] = 'CREATED'
df_csv["tx_unique_identifier"] = [str(uuid.uuid4()) for _ in range(len(df))]
df_csv["tx_updatedate"] = '2023-10-09 19:40:15'
df_csv["tx_cash_register_code"] = df["TIENDA"].str.replace('ST', 'CHS')
df_csv["tx_correlative_code"] = ["CRV" + str(i).zfill(3) for i in range(1, len(df) + 1)]
df_csv["tx_finalserie"] = df["NUMERO FINAL"]
df_csv["tx_initialserie"] = df["NUMERO INICIAL"]
df_csv["fl_iscontingency"] = "N"
df_csv["islegal"] = ""
df_csv["tx_lengthnumber"] = "8"
df_csv["tx_nextnumber"] = df["NUMERO ACTUAL"]
df_csv["tx_parentreceipttype"] = df["# TIPO PROCEDENCIA"]
df_csv["tx_receipttype"] = '0'+df['# TIPO'].astype(str)
df_csv["tx_reftype"] = 'F'
df_csv["tx_serie"] = df["SERIE"]
df_csv["tx_store"] = df["TIENDA"]
df_csv["nu_version"] = "1"
df_csv["fl_isexternal"] = ""

# Ruta del archivo CSV de salida
output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_correlative.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

df_csv.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')
