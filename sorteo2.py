import streamlit as st
import pandas as pd
import random

# Función para cargar nombres desde un archivo CSV
def cargar_nombres(file):
    data = pd.read_csv(file)
    nombres = data.iloc[:, 0].tolist()  # Asumimos que los nombres están en la primera columna
    return nombres

# Número total de heats y tamaño de heats
total_heats = 4
tamanio_heat = 2

def generar_heats(nombres):
    # Inicializar heats vacíos
    heats = [[] for _ in range(total_heats)]
    participacion = {nombre: 0 for nombre in nombres}

    # Asignar cada persona a heats 1-2 primero
    for nombre in nombres:
        heats_asignados = 0
        intentos = 0
        while heats_asignados < 1 and intentos < 100:
            # Seleccionar un heat aleatorio del 1 al 2
            heat_index = random.choice(range(2))
            if len(heats[heat_index]) < tamanio_heat and participacion[nombre] < 1:
                heats[heat_index].append(nombre)
                participacion[nombre] += 1
                heats_asignados += 1
            intentos += 1

    # Asignar cada persona a heats 3-4 después
    for nombre in nombres:
        heats_asignados = 0
        intentos = 0
        while heats_asignados < 1 and intentos < 100:
            # Seleccionar un heat aleatorio del 3 al 4
            heat_index = random.choice(range(2, 4))
            if len(heats[heat_index]) < tamanio_heat and participacion[nombre] < 2:
                heats[heat_index].append(nombre)
                participacion[nombre] += 1
                heats_asignados += 1
            intentos += 1

    # Asegurarse de que los participantes "NN NN" estén en heats de 2 personas
    for heat in heats:
        if len(heat) < 2 and "NN NN" in heat:
            for h in heats:
                if len(h) == 2 and "NN NN" not in h:
                    heat.append(h.pop())
                    if len(heat) == 2:
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
        
        # Generar el contenido del archivo de salida
        output_content = guardar_heats(heats)

        # Mostrar el botón para descargar el archivo de salida
        st.download_button(
            label="Descargar Heats",
            data=output_content,
            file_name="heats.txt",
            mime="text/plain"
        )

