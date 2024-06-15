import streamlit as st
import pandas as pd

# Ejemplo de datos para consultas y generación de informes
data = {
    'ID': [1, 2, 3, 4],
    'Nombre': ['EES 1', 'EES 2', 'EES 3', 'EES 4'],
    'Ancho de Banda (Mbps)': [100, 150, 200, 250],
    'Estado': ['Pendiente', 'Aprobado', 'En Proceso', 'Completado']
}

df = pd.DataFrame(data)

# Título de la aplicación
st.title('Interfaz del Analista Avanzado - SAGEC')

# Descripción
st.write("""
Esta interfaz permite al Analista Avanzado realizar consultas a la base de datos y generar informes personalizados.
""")

# Sección de consultas
st.header('Consultas a la Base de Datos')
consulta = st.text_input('Ingrese su consulta SQL:')
if st.button('Ejecutar Consulta'):
    # Aquí se simula la ejecución de una consulta SQL
    st.write('Resultados de la consulta:')
    st.write(df)

# Sección de generación de informes
st.header('Generación de Informes')
tipo_informe = st.selectbox('Seleccione el tipo de informe:', ['Resumen', 'Detallado', 'Gráfico'])
if st.button('Generar Informe'):
    if tipo_informe == 'Resumen':
        st.write('Informe Resumen:')
        st.write(df.describe())
    elif tipo_informe == 'Detallado':
        st.write('Informe Detallado:')
        st.write(df)
    elif tipo_informe == 'Gráfico':
        st.write('Informe Gráfico:')
        st.bar_chart(df.set_index('Nombre')['Ancho de Banda (Mbps)'])


