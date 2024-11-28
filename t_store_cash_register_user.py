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
df = pd.read_excel(file_path, sheet_name='Usuario Login')

df = df[df["CAJERO"] == "SI"]

df['id_cashregister_user'] = range(1, len(df) + 1)

df_csv = df[["id_cashregister_user"]].copy()
df_csv["tx_company_code"] = "AZALEIA"
df_csv["tx_createdate"] = '2023-09-08 15:19:24'
df_csv["tx_status"] = 'CREATED'
df_csv["tx_unique_identifier"] = [str(uuid.uuid4()) for _ in range(len(df))]
df_csv["tx_updatedate"] = '2023-09-08 15:19:24'
df_csv["tx_cash_register_code"] = df["TIENDACODIGO"].str.replace('ST', 'CHS')
df_csv["tx_cash_register_user_code"] = "CSHRUSR" + df["TIENDACODIGO"].str[-3:]
df_csv["tx_user_doc_number"] = df["DNI/DOC"]
df_csv["tx_user_mail"] = df["CORREO"]
df_csv["tx_user"] = ''
df_csv["tx_user_name"] = df["NOMBRES"] + " " + df["APELLIDOS"]

# Ruta del archivo CSV de salida
output_dir = 'result/'
output_csv = os.path.join(output_dir, 't_store_cash_register_user.csv')

# Verificar y crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

df_csv.to_csv(output_csv, index=False, sep=';')

print(f'Archivo CSV guardado en {output_csv}')

#UPDATE core.t_cashregister_user AS cru
#JOIN `security`.t_credential AS tc ON cru.tx_user_mail  = tc.tx_identifier
#JOIN `security`.t_member AS tm ON tc.id_member = tm.id_member
#SET cru.tx_user = tm.tx_uniqueidentifier;