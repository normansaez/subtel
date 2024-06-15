import streamlit as st
import pandas as pd

# Datos de ejemplo para FAS y FUS
fas_data = {
    'FAS ID': [201, 202, 203],
    'EES': ['EES 1', 'EES 2', 'EES 3'],
    'Estado': ['Pendiente de Validación', 'Pendiente de Validación', 'Validado'],
    'Fecha': ['2024-06-01', '2024-06-02', '2024-06-03'],
    'Descripción': ['Alta de Servicio', 'Alta de Servicio', 'Alta de Servicio']
}

fus_data = {
    'FUS ID': [301, 302],
    'EES': ['EES 1', 'EES 2'],
    'Estado': ['Pendiente de Validación', 'Validado'],
    'Fecha': ['2024-06-05', '2024-06-06'],
    'Descripción': ['Upgrade de Servicio', 'Upgrade de Servicio']
}

prefactura_data = {
    'Prefactura ID': [401, 402],
    'EES': ['EES 1', 'EES 2'],
    'Monto': [1000, 1500],
    'Estado': ['Pendiente de Autorización', 'Autorizada'],
    'Fecha': ['2024-06-07', '2024-06-08']
}

fas_df = pd.DataFrame(fas_data)
fus_df = pd.DataFrame(fus_data)
prefactura_df = pd.DataFrame(prefactura_data)

# Título de la aplicación
st.title('Interfaz del Validador SUBTEL - SAGEC')

# Descripción de la aplicación
st.write("""
Esta interfaz permite al Validador SUBTEL ratificar y validar los formularios FAS y FUS, así como autorizar las Pre-facturas.
""")

# Sección de validación de FAS
st.header('Validación de FAS')
st.dataframe(fas_df)
fas_id = st.number_input('Ingrese el ID del FAS para validar:', min_value=201, max_value=203, step=1)
if st.button('Validar FAS'):
    fas_df.loc[fas_df['FAS ID'] == fas_id, 'Estado'] = 'Validado'
    st.success(f'El FAS ID {fas_id} ha sido validado.')
    st.dataframe(fas_df)

# Sección de validación de FUS
st.header('Validación de FUS')
st.dataframe(fus_df)
fus_id = st.number_input('Ingrese el ID del FUS para validar:', min_value=301, max_value=302, step=1)
if st.button('Validar FUS'):
    fus_df.loc[fus_df['FUS ID'] == fus_id, 'Estado'] = 'Validado'
    st.success(f'El FUS ID {fus_id} ha sido validado.')
    st.dataframe(fus_df)

# Sección de autorización de Pre-facturas
st.header('Autorización de Pre-facturas')
st.dataframe(prefactura_df)
prefactura_id = st.number_input('Ingrese el ID de la Prefactura para autorizar:', min_value=401, max_value=402, step=1)
if st.button('Autorizar Prefactura'):
    prefactura_df.loc[prefactura_df['Prefactura ID'] == prefactura_id, 'Estado'] = 'Autorizada'
    st.success(f'La Prefactura ID {prefactura_id} ha sido autorizada.')
    st.dataframe(prefactura_df)


