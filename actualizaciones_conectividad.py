import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la aplicación
st.title("Actualizaciones del Servicio de Conectividad y Parque de EES")

# Sección de Actualizaciones del Servicio de Conectividad
st.header("Actualizaciones del Servicio de Conectividad")
st.write("""
Las actualizaciones del servicio de conectividad aseguran que los establecimientos educacionales subvencionados (EES) mantengan una conexión eficiente y acorde a las nuevas necesidades. 
Se realizan mejoras técnicas y de infraestructura, garantizando un monitoreo continuo y una gestión actualizada del parque de EES para optimizar el rendimiento y la calidad del servicio.
""")

# Datos de ejemplo para actualizaciones de conectividad
data_conectividad = {
    'Fecha': [datetime(2024, 1, 15), datetime(2024, 3, 20), datetime(2024, 5, 10)],
    'Descripción': [
        'Actualización de routers y switches en zona norte',
        'Incremento de ancho de banda en zona central',
        'Implementación de redundancia en conexiones de zona sur'
    ]
}

df_conectividad = pd.DataFrame(data_conectividad)

st.subheader("Historial de Actualizaciones")
st.dataframe(df_conectividad)

# Sección del Parque de EES
st.header("Parque de Establecimientos Educacionales Subvencionados (EES)")
st.write("""
El parque de EES incluye todos los establecimientos educacionales que son beneficiarios del servicio de conectividad. 
Este parque es gestionado y actualizado continuamente para asegurar la calidad del servicio y atender las necesidades específicas de cada establecimiento.
""")

# Datos de ejemplo para el parque de EES
data_ees = {
    'ID': [1, 2, 3, 4],
    'Nombre del Establecimiento': ['Escuela A', 'Colegio B', 'Liceo C', 'Instituto D'],
    'Región': ['Norte', 'Central', 'Sur', 'Norte'],
    'Conectividad Actual': ['50 Mbps', '100 Mbps', '200 Mbps', '50 Mbps']
}

df_ees = pd.DataFrame(data_ees)

st.subheader("Parque de EES")
st.dataframe(df_ees)

# Funcionalidad para agregar nuevas actualizaciones
st.subheader("Agregar Nueva Actualización")
new_date = st.date_input("Fecha de Actualización")
new_desc = st.text_area("Descripción de la Actualización")

if st.button("Agregar Actualización"):
    new_data = {'Fecha': [new_date], 'Descripción': [new_desc]}
    new_df = pd.DataFrame(new_data)
    df_conectividad = pd.concat([df_conectividad, new_df], ignore_index=True)
    st.success("Actualización agregada con éxito!")
    st.dataframe(df_conectividad)

# Funcionalidad para agregar nuevos EES
st.subheader("Agregar Nuevo EES")
new_id = st.number_input("ID del EES", min_value=1, step=1)
new_name = st.text_input("Nombre del Establecimiento")
new_region = st.selectbox("Región", ['Norte', 'Central', 'Sur'])
new_connectivity = st.text_input("Conectividad Actual")

if st.button("Agregar EES"):
    new_ees_data = {
        'ID': [new_id],
        'Nombre del Establecimiento': [new_name],
        'Región': [new_region],
        'Conectividad Actual': [new_connectivity]
    }
    new_ees_df = pd.DataFrame(new_ees_data)
    df_ees = pd.concat([df_ees, new_ees_df], ignore_index=True)
    st.success("Nuevo EES agregado con éxito!")
    st.dataframe(df_ees)

