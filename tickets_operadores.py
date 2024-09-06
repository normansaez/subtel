import streamlit as st

# Título de la aplicación
st.title("Causas de problemas de conectividad del operador EES")

# Lista de posibles causas
causas = [
    {
        "Causa": "Fallas en la infraestructura física",
        "Descripción": "Interrupciones eléctricas, daños en cables, vandalismo, o fenómenos climáticos."
    },
    {
        "Causa": "Problemas de configuración o software",
        "Descripción": "Errores en la configuración de routers, actualizaciones de software defectuosas, incompatibilidad de equipos."
    },
    {
        "Causa": "Capacidad de ancho de banda insuficiente",
        "Descripción": "Congestión de la red debido a un uso elevado de banda ancha o limitación de velocidad por parte del operador."
    },
    {
        "Causa": "Problemas de enlace y conectividad",
        "Descripción": "Interrupciones en los enlaces de comunicación o falta de un enlace de respaldo para la continuidad del servicio."
    },
    {
        "Causa": "Problemas de seguridad",
        "Descripción": "Ataques de ciberseguridad, como ataques DDoS, que sobrecargan la red, o malware afectando la conectividad."
    },
    {
        "Causa": "Factores geográficos y climatológicos",
        "Descripción": "Cobertura limitada en zonas remotas o condiciones climáticas extremas que afectan la infraestructura."
    },
    {
        "Causa": "Incumplimiento de los acuerdos de servicio (SLA)",
        "Descripción": "Tiempos de respuesta prolongados, falta de redundancia en la red o incumplimiento del ancho de banda garantizado."
    },
    {
        "Causa": "Problemas con el proveedor",
        "Descripción": "Mala gestión del soporte técnico o incumplimiento de las condiciones del contrato por parte del proveedor."
    }
]

# Mostrar las causas con descripciones y pickers de horas
st.header("Posibles causas y estimación de duración (en horas)")

# Inicializar un diccionario para almacenar las horas seleccionadas por el usuario
duraciones = {}

for causa in causas:
    st.write(f"### {causa['Causa']}")
    st.write(causa["Descripción"])
    
    # Picker de horas
    horas = st.number_input(f"Selecciona las horas estimadas de duración del problema para '{causa['Causa']}'", min_value=0, max_value=72, value=1, step=1)
    
    # Almacenar la duración seleccionada
    duraciones[causa['Causa']] = horas

# Mostrar las duraciones seleccionadas
st.write("## Duración estimada para cada causa:")
st.write(duraciones)

# Sección de comentarios
st.header("¿Tienes más información?")
st.text_area("Agrega tus observaciones o comentarios aquí:")

