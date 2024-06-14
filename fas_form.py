import streamlit as st

# Título del formulario
st.title("Formulario electrónico de Alta del Servicio (FAS)")

# Identificación del Establecimiento Educacional Subvencionado (EES)
st.header("Identificación del EES")
rbd = st.text_input("Código único de identificación (RBD)")
nombre_establecimiento = st.text_input("Nombre del establecimiento")

# Datos de Contacto
st.header("Datos de Contacto")
nombre_responsable = st.text_input("Nombre del responsable del establecimiento")
telefono_contacto = st.text_input("Teléfono de contacto")
correo_electronico = st.text_input("Correo electrónico del responsable")

# Detalles de la Conectividad
st.header("Detalles de la Conectividad")
tipo_conexion = st.selectbox("Tipo de conexión proporcionada", ["Fibra óptica", "ADSL", "Cable", "Inalámbrica"])
ancho_banda_total = st.number_input("Ancho de banda total comprometido (Mbps)", min_value=0.1, step=0.1)
ancho_banda_internacional = st.number_input("Ancho de banda internacional comprometido (Mbps)", min_value=0.1, step=0.1)

# Información de la Instalación
st.header("Información de la Instalación")
fecha_inicio_instalacion = st.date_input("Fecha de inicio de la instalación")
fecha_finalizacion_instalacion = st.date_input("Fecha de finalización de la instalación")
estado_instalacion = st.selectbox("Estado de la instalación", ["Pendiente", "En progreso", "Completado"])

# Datos Técnicos
st.header("Datos Técnicos")
ip_asignada = st.text_input("IP asignada")
equipos_instalados = st.text_area("Equipos instalados (routers, switches, etc.)")
configuraciones_especificas = st.text_area("Configuraciones específicas requeridas")

# Validación y Aprobación
st.header("Validación y Aprobación")
firma_responsable = st.text_input("Firma electrónica del responsable del establecimiento")
firma_tecnico = st.text_input("Firma electrónica del técnico instalador")
fecha_validacion = st.date_input("Fecha de validación y aprobación del servicio")

# Botón para enviar
if st.button("Enviar"):
    st.success("Formulario enviado con éxito!")
    # Aquí puedes agregar el código para guardar o procesar los datos

