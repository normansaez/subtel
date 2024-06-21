import streamlit as st
import pandas as pd
import random

# Función para cargar nombres desde un archivo CSV
def cargar_nombres(file):
    data = pd.read_csv(file)
    nombres = data.iloc[:, 0].tolist()  # Asumimos que los nombres están en la primera columna
    return nombres

# Número total de heats y tamaño de heats
total_heats = 10
tamanio_heat = 4

def generar_heats(nombres):
    # Inicializar heats vacíos
    heats = [[] for _ in range(total_heats)]
    participacion = {nombre: 0 for nombre in nombres}

    # Asignar cada persona a heats 1-5 primero
    for nombre in nombres:
        heats_asignados = 0
        intentos = 0
        while heats_asignados < 1 and intentos < 100:
            # Seleccionar un heat aleatorio del 1 al 5
            heat_index = random.choice(range(5))
            if len(heats[heat_index]) < tamanio_heat and participacion[nombre] < 1:
                heats[heat_index].append(nombre)
                participacion[nombre] += 1
                heats_asignados += 1
            intentos += 1

    # Asignar cada persona a heats 6-10 después
    for nombre in nombres:
        heats_asignados = 0
        intentos = 0
        while heats_asignados < 1 and intentos < 100:
            # Seleccionar un heat aleatorio del 6 al 10
            heat_index = random.choice(range(5, 10))
            if len(heats[heat_index]) < tamanio_heat and participacion[nombre] < 2:
                heats[heat_index].append(nombre)
                participacion[nombre] += 1
                heats_asignados += 1
            intentos += 1

    # Ajuste de heats para asegurar que haya al menos 3 personas en cada uno y no haya duplicados en heats de 3 personas
    for heat in heats:
        if len(heat) < 3:
            for h in heats:
                if len(h) > 3 and len(set(h)) == len(h):
                    heat.append(h.pop())
                    break

    return heats

def guardar_heats(heats):
    lines = []
    for i, heat in enumerate(heats):
        lines.append(f"heat{i + 1}")
        lines.extend(heat)
        lines.append("")
    return "\n".join(lines)

st.title('Generador de Heats')

uploaded_file = st.file_uploader("Sube el archivo CSV con la lista de participantes")

if uploaded_file is not None:
    nombres = cargar_nombres(uploaded_file)
    st.write("Participantes:")
    st.write(nombres)

    if st.button('Generar Heats'):
        heats = generar_heats(nombres)
        for i, heat in enumerate(heats):
            st.write(f"Heat {i + 1}: {', '.join(heat)}")
        
        # Generar y mostrar el contenido del archivo de salida
        output_content = guardar_heats(heats)
        st.download_button(
            label="Descargar Heats",
            data=output_content,
            file_name="heats.txt",
            mime="text/plain"
        )

