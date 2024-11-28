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
df = pd.read_excel(file_path, sheet_name='Usuario Login')

# Crear un DataFrame con la estructura deseada
new_df = df[['#']].copy()
new_df['tx_createdate'] = '2023-10-27 01:50:30'
new_df['tx_status'] = 'CREATED'
new_df['tx_company_code'] = 'AZALEIA'
new_df['tx_is_admin'] = 'NO'
new_df['tx_is_default'] = ''
new_df['tx_sales_person_code'] = '-1'
new_df['tx_store_code'] = df['TIENDACODIGO']
new_df['tx_user_code'] = ''
new_df['tx_user_doc'] = df['DNI/DOC']
new_df['tx_user_email'] = df['CORREO']
new_df['tx_user_name'] = df['NOMBRES']
new_df['tx_user_role'] = df['CARGO / ROL']

new_df.drop(columns='#', inplace=True)

# Ruta del archivo CSV de salida
output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_user.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

new_df.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')

# ACTUALIZAR EL UID DEL MEMBER POR CONSULTA
#UPDATE admin.t_store_user AS su
#JOIN `security`.t_credential AS c ON su.tx_user_email = c.tx_identifier
#JOIN `security`.t_member AS m ON c.id_member = m.id_member
#SET su.tx_user_code = m.tx_uniqueidentifier;