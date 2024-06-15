import streamlit as st
import pandas as pd

# Datos de ejemplo para FAS y FUS
fas_data = {
    'FAS ID': [201, 202, 203],
    'EES': ['EES 1', 'EES 2', 'EES 3'],
    'Estado': ['Pendiente de Aprobación', 'Pendiente de Aprobación', 'Aprobado'],
    'Fecha': ['2024-06-01', '2024-06-02', '2024-06-03'],
    'Descripción': ['Alta de Servicio', 'Alta de Servicio', 'Alta de Servicio']
}

fus_data = {
    'FUS ID': [301, 302],
    'EES': ['EES 1', 'EES 2'],
    'Estado': ['Pendiente de Aprobación', 'Aprobado'],
    'Fecha': ['2024-06-05', '2024-06-06'],
    'Descripción': ['Upgrade de Servicio', 'Upgrade de Servicio']
}

fas_df = pd.DataFrame(fas_data)
fus_df = pd.DataFrame(fus_data)

# Título de la aplicación
st.title('Interfaz del Representante EES - SAGEC')

# Descripción de la aplicación
st.write("""
Esta interfaz permite al Representante EES aprobar los datos cargados en los formularios FAS y FUS, así como monitorear y gestionar el servicio de conectividad.
""")

# Sección de aprobación de FAS
st.header('Aprobación de FAS')
st.dataframe(fas_df)
fas_id = st.number_input('Ingrese el ID del FAS para aprobar:', min_value=201, max_value=203, step=1)
if st.button('Aprobar FAS'):
    fas_df.loc[fas_df['FAS ID'] == fas_id, 'Estado'] = 'Aprobado'
    st.success(f'El FAS ID {fas_id} ha sido aprobado.')
    st.dataframe(fas_df)

# Sección de aprobación de FUS
st.header('Aprobación de FUS')
st.dataframe(fus_df)
fus_id = st.number_input('Ingrese el ID del FUS para aprobar:', min_value=301, max_value=302, step=1)
if st.button('Aprobar FUS'):
    fus_df.loc[fus_df['FUS ID'] == fus_id, 'Estado'] = 'Aprobado'
    st.success(f'El FUS ID {fus_id} ha sido aprobado.')
    st.dataframe(fus_df)


