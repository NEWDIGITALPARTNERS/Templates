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
df = pd.read_excel(file_path, sheet_name='Tienda')

# Mapeo de columnas
column_mapping = {
    'TIENDACODIGO': 'tx_store_code',
    'TIENDA': 'tx_name',
    'Direccion': 'tx_address',
    'correo de SuperVisor de Tienda': 'tx_user_admin',
    'Centro de Costo 1': 'tx_costing_code',
    'Centro de Costo 2': 'tx_costing_code2',
    'Centro de Costo 3': 'tx_costing_code3',
    'Modificación de precios': 'tx_modify_price',
    'Percepción': 'tx_is_perception'
}

# Renombrar columnas
df = df.rename(columns=column_mapping)

# Agregar columnas adicionales requeridas con valores predeterminados
df['tx_createdate'] = '2023-10-27 01:50:30'
df['tx_status'] = 'CREATED'
df['tx_company_code'] = 'AZALEIA'
df['tx_description'] = '-'
df['tx_location'] = ''
df['tx_location_code'] = ''
df['tx_type'] = ''

# Orden de las columnas
column_order = [
    'tx_createdate', 'tx_status', 'tx_address', 'tx_company_code', 'tx_costing_code',
    'tx_costing_code2', 'tx_costing_code3', 'tx_description', 'tx_is_perception',
    'tx_location', 'tx_location_code', 'tx_name', 'tx_store_code', 'tx_type',
    'tx_user_admin', 'tx_modify_price'
]

df = df[column_order]

# Ruta del archivo CSV de salida
output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

df.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')
