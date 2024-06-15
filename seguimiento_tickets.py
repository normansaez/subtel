import streamlit as st
import pandas as pd

# Datos de ejemplo para los tickets
tickets_data = {
    'Ticket ID': [101, 102, 103, 104],
    'EES': ['EES 1', 'EES 2', 'EES 3', 'EES 4'],
    'Fecha de Creación': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04'],
    'Descripción': ['Problema de conexión', 'Baja velocidad', 'Corte de servicio', 'Intermitencia en la conexión'],
    'Estado': ['Pendiente', 'En Proceso', 'Resuelto', 'Pendiente']
}

# Convertir los datos en un DataFrame
tickets_df = pd.DataFrame(tickets_data)

# Título de la aplicación
st.title('Interfaz del Operador Seguimiento Tickets - SAGEC')

# Descripción de la aplicación
st.write("""
Esta interfaz permite al Operador Seguimiento Tickets realizar el seguimiento y gestión de los tickets de ayuda ingresados en la Plataforma de Gestión Integrada.
""")

# Mostrar los tickets en una tabla
st.header('Listado de Tickets')
st.dataframe(tickets_df)

# Filtro por Estado
st.header('Filtrar Tickets por Estado')
estado = st.selectbox('Seleccione el estado del ticket:', ['Todos', 'Pendiente', 'En Proceso', 'Resuelto'])
if estado != 'Todos':
    filtered_df = tickets_df[tickets_df['Estado'] == estado]
else:
    filtered_df = tickets_df
st.dataframe(filtered_df)

# Actualizar el estado de un ticket
st.header('Actualizar Estado del Ticket')
ticket_id = st.number_input('Ingrese el ID del Ticket:', min_value=101, max_value=104, step=1)
nuevo_estado = st.selectbox('Nuevo Estado:', ['Pendiente', 'En Proceso', 'Resuelto'])
if st.button('Actualizar Estado'):
    tickets_df.loc[tickets_df['Ticket ID'] == ticket_id, 'Estado'] = nuevo_estado
    st.success(f'El estado del Ticket ID {ticket_id} ha sido actualizado a {nuevo_estado}.')
    st.dataframe(tickets_df)

