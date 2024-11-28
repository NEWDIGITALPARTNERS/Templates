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
df = pd.read_excel(file_path, sheet_name='Tienda')

# Crear una columna iterativa para id_store_price_list
df['id_store_price_list'] = range(1, len(df) + 1)

# Crear un DataFrame con la estructura deseada
df_csv = df[["id_store_price_list"]].copy()
df_csv["tx_createdate"] = '2023-10-27 01:50:30'
df_csv["tx_status"] = 'CREATED'
df_csv["tx_price_list_code"] = "3"
df_csv["tx_store_code"] = df["TIENDACODIGO"]
df_csv["tx_store_price_list_code"] = "LP" + df["TIENDACODIGO"].str[-3:]
df_csv["tx_company_code"] = "AZALEIA"

output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_list.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

df_csv.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')