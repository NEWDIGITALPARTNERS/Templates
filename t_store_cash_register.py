import pandas as pd
import uuid
import os
import warnings

# Suprimir warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Ruta del archivo Excel
file_path = 'Azaleia - (POS)Usuario.Tienda.Almacen (version 1) 24072024 SM.xlsx'

# Verificar si el archivo existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo {file_path} no se encontró.")

# Cargar el archivo Excel
df = pd.read_excel(file_path, sheet_name='Tienda')

df['id_cashregister'] = range(1, len(df) + 1)

df_csv = df[["id_cashregister"]].copy()
df_csv["tx_company_code"] = "AZALEIA"
df_csv["tx_createdate"] = '2023-07-10 01:17:57'
df_csv["tx_status"] = 'CREATED'
df_csv["tx_unique_identifier"] = [str(uuid.uuid4()) for _ in range(len(df))]
df_csv["tx_updatedate"] = '2023-09-08 15:19:40'
#df_csv["tx_cash_register_code"] = df["TIENDACODIGO"]
df_csv["tx_cash_register_code"] = df["TIENDACODIGO"].str.replace('ST', 'CHS')
df_csv["tx_is_active"] = "Y"
df_csv["tx_name"] = "CAJA " + df["TIENDA"].str.replace('TIENDA', '')
df_csv["fl_opened"] = 0
df_csv["tx_status_operation"] = "CLOSED"
df_csv["tx_store"] = df["TIENDACODIGO"]
df_csv["tx_store_name"] = df["TIENDA"]
df_csv["tx_type"] = "C"

# Ruta del archivo CSV de salida
output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_cashregister.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)
df_csv.to_csv(output_csv, index=False, sep=';', encoding='utf-8')
print(f'Archivo CSV guardado en {output_csv}')