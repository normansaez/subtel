import streamlit as st
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import base64

# Función para firmar datos
def sign_data(private_key, data):
    signer = private_key.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signer

# Cargar la clave privada del archivo PEM
def load_private_key(file_path, password=None):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=password
        )
    return private_key

# Formulario en Streamlit
st.title("Formulario Único de Solicitud (FUS)")

st.header("Información Personal")
nombre = st.text_input("Nombre")
apellido = st.text_input("Apellido")
rut = st.text_input("RUT")
direccion = st.text_input("Dirección")
telefono = st.text_input("Teléfono")
email = st.text_input("Correo Electrónico")

st.header("Detalles de la Solicitud")
tipo_solicitud = st.selectbox("Tipo de Solicitud", ["Solicitud de Certificado", "Solicitud de Cambio de Datos", "Solicitud de Baja", "Otra"])
descripcion = st.text_area("Descripción de la Solicitud")

if st.button("Firmar y Enviar"):
    if not nombre or not apellido or not rut or not direccion or not telefono or not email or not descripcion:
        st.error("Por favor, complete todos los campos.")
    else:
        # Datos a firmar
        data = f"Nombre: {nombre}\nApellido: {apellido}\nRUT: {rut}\nDirección: {direccion}\nTeléfono: {telefono}\nCorreo Electrónico: {email}\nTipo de Solicitud: {tipo_solicitud}\nDescripción: {descripcion}".encode('utf-8')

        # Cargar clave privada
        private_key = load_private_key("ruta_a_tu_clave_privada.pem")

        # Firmar los datos
        firma = sign_data(private_key, data)

        # Mostrar la firma en base64
        st.success("Formulario firmado y enviado con éxito!")
        st.write("Firma (Base64):")
        st.code(base64.b64encode(firma).decode('utf-8'))

        # Guardar los datos firmados y la firma en un archivo (opcional)
        with open("fus_firmado.txt", "wb") as f:
            f.write(data)
            f.write(b"\nFirma:\n")
            f.write(firma)

