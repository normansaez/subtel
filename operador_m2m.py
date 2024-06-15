import streamlit as st
import pandas as pd

# Datos de ejemplo para archivos subidos
archivos_data = {
    'Archivo ID': [501, 502, 503],
    'Nombre del Archivo': ['archivo1.csv', 'archivo2.csv', 'archivo3.csv'],
    'Fecha de Subida': ['2024-06-10', '2024-06-11', '2024-06-12'],
    'Estado': ['Procesado', 'Pendiente', 'Procesado']
}

archivos_df = pd.DataFrame(archivos_data)

# Título de la aplicación
st.title('Interfaz del Operador M2M - SAGEC')

# Descripción de la aplicación
st.write("""
Esta interfaz permite al Operador M2M subir archivos provenientes de la red del Operador de telecomunicaciones y monitorear el estado de procesamiento de dichos archivos en la plataforma SAGEC.
""")

# Sección de subida de archivos
st.header('Subida de Archivos')
uploaded_file = st.file_uploader("Seleccione un archivo para subir", type=["csv", "xlsx", "txt"])
if uploaded_file is not None:
    # Aquí se simula la subida y procesamiento del archivo
    st.success(f'El archivo {uploaded_file.name} ha sido subido y procesado correctamente.')
    nuevo_archivo = {
        'Archivo ID': archivos_df['Archivo ID'].max() + 1,
        'Nombre del Archivo': uploaded_file.name,
        'Fecha de Subida': '2024-06-13',
        'Estado': 'Procesado'
    }
    archivos_df = archivos_df.append(nuevo_archivo, ignore_index=True)
    st.dataframe(archivos_df)

# Sección de monitoreo de archivos
st.header('Monitoreo de Archivos Subidos')
st.dataframe(archivos_df)

# Filtro por Estado
st.header('Filtrar Archivos por Estado')
estado = st.selectbox('Seleccione el estado del archivo:', ['Todos', 'Procesado', 'Pendiente'])
if estado != 'Todos':
    filtered_df = archivos_df[archivos_df['Estado'] == estado]
else:
    filtered_df = archivos_df
st.dataframe(filtered_df)


