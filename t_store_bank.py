import pandas as pd
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
df = pd.read_excel(file_path, sheet_name='Tienda')# Suprimir warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Ruta del archivo Excel
file_path = 'Azaleia - (POS)Usuario.Tienda.Almacen (version 1) 24072024 SM.xlsx'

# Verificar si el archivo existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo {file_path} no se encontró.")

# Cargar el archivo Excel
df = pd.read_excel(file_path, sheet_name='Banco')

df['id_store_bank'] = range(1, 1 + len(df))

df_csv = df[["id_store_bank"]].copy()
df_csv["tx_createdate"] = "2023-07-16 13:00:39"
df_csv["tx_status"] = "CREATED"
df_csv["tx_company_code"] = "AZALEIA"
df_csv["tx_gl_account"] = df["CUENTA CONTABLE"]
df_csv["tx_store_bank_code"] = df["NUMERO DE CUENTA"]
df_csv["tx_store_code"] = df["TIENDA"]

output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_bank.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

df_csv.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')