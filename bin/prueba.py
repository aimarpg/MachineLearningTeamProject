from scipy.io import arff
import pandas as pd

# Cargar el archivo ARFF usando scipy
with open('../resources/raw_datasets/phpkIxskf.arff', 'r') as f:
    data, meta = arff.loadarff(f)

# Crear un DataFrame con los datos cargados
df = pd.DataFrame(data)

# Verificar los primeros registros del DataFrame antes de cambiar nombres
print("Datos antes de cambiar nombres:")
print(df.head())

# Lista de nombres de columnas basado en la descripción proporcionada
column_names = [
    'age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
    'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
    'previous', 'poutcome', 'y'
]

# Verificar si el número de columnas coincide con los nombres proporcionados
if df.shape[1] == len(column_names):
    # Asignar los nombres de las columnas correctos
    df.columns = column_names
    print("Nombres de columnas asignados correctamente.")
else:
    print(f"Error: El número de columnas ({df.shape[1]}) no coincide con los nombres proporcionados ({len(column_names)}).")

# Verificar los primeros registros después de cambiar nombres
print("Datos después de cambiar nombres:")
print(df.head())

# Guardar el DataFrame en un archivo CSV si los nombres se han asignado correctamente
df.to_csv('../resources/processed_datasets/Bank_Marketing.csv', index=False)

print("Bank Marketing dataset processed and saved as CSV")
