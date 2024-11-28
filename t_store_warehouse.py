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
df = pd.read_excel(file_path, sheet_name='Almacen')

df['id_store_warehouse'] = range(1, len(df) + 1)
new_df = df[["id_store_warehouse"]].copy()
##new_df = df[['#']].copy()
new_df['tx_createdate'] = '2024-01-01 01:50:30'
new_df['tx_status'] = 'CREATED'
new_df['tx_company_code'] = 'AZALEIA'
new_df['tx_store_code'] = df['Codigo de Tienda']
new_df['tx_warehouse_code'] = df['CODIGO DE ALMACEN (SAP)'].astype(str)
new_df['tx_store_warehouse_code'] = 'W' + df['CODIGO DE ALMACEN (SAP)'].astype(str)
new_df['tx_ws_default'] = 'N'

# Ruta del archivo CSV de salida
output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_warehouse.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

new_df.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')