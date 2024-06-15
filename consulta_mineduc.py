import streamlit as st
import pandas as pd

# Datos de ejemplo para informes y validaciones
informes_data = {
    'Informe ID': [1, 2, 3],
    'Tipo de Informe': ['Calidad de Servicio', 'Estado de Conectividad', 'Rendimiento de Operadores'],
    'Fecha': ['2024-06-01', '2024-06-02', '2024-06-03'],
    'Descripción': ['Informe mensual sobre la calidad del servicio', 'Informe diario sobre el estado de conectividad', 'Informe semanal sobre el rendimiento de los operadores']
}

validaciones_data = {
    'Validación ID': [101, 102],
    'Tipo': ['FAS', 'FUS'],
    'Estado': ['Validado', 'Pendiente'],
    'Fecha': ['2024-06-05', '2024-06-06'],
    'Descripción': ['Validación de Alta de Servicio', 'Validación de Upgrade de Servicio']
}

informes_df = pd.DataFrame(informes_data)
validaciones_df = pd.DataFrame(validaciones_data)

# Título de la aplicación
st.title('Interfaz de Consulta MINEDUC - SAGEC')

# Descripción de la aplicación
st.write("""
Esta interfaz permite al usuario Consulta MINEDUC acceder a informes, monitorear el estado del servicio de conectividad y revisar validaciones en la plataforma SAGEC.
""")

# Sección de Informes
st.header('Acceso a Informes')
st.dataframe(informes_df)
informe_id = st.number_input('Ingrese el ID del Informe para visualizar:', min_value=1, max_value=3, step=1)
if st.button('Ver Informe'):
    informe = informes_df[informes_df['Informe ID'] == informe_id]
    st.write(f"Informe ID: {informe['Informe ID'].values[0]}")
    st.write(f"Tipo de Informe: {informe['Tipo de Informe'].values[0]}")
    st.write(f"Fecha: {informe['Fecha'].values[0]}")
    st.write(f"Descripción: {informe['Descripción'].values[0]}")

# Sección de Paneles de Control
st.header('Paneles de Control en Tiempo Real')
# Aquí se pueden agregar gráficos y estadísticas en tiempo real
st.write("Panel de Control de Calidad del Servicio")
st.line_chart(data=[1, 2, 3, 4, 5])  # Ejemplo de gráfico

# Sección de Validaciones
st.header('Historial de Validaciones')
st.dataframe(validaciones_df)
validacion_id = st.number_input('Ingrese el ID de la Validación para revisar:', min_value=101, max_value=102, step=1)
if st.button('Ver Validación'):
    validacion = validaciones_df[validaciones_df['Validación ID'] == validacion_id]
    st.write(f"Validación ID: {validacion['Validación ID'].values[0]}")
    st.write(f"Tipo: {validacion['Tipo'].values[0]}")
    st.write(f"Estado: {validacion['Estado'].values[0]}")
    st.write(f"Fecha: {validacion['Fecha'].values[0]}")
    st.write(f"Descripción: {validacion['Descripción'].values[0]}")


