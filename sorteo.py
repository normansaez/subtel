import streamlit as st
import random

# Lista de nombres
nombres = [
    'Persona1', 'Persona2', 'Persona3', 'Persona4', 'Persona5', 
    'Persona6', 'Persona7', 'Persona8', 'Persona9', 'Persona10',
    'Persona11', 'Persona12', 'Persona13', 'Persona14', 'Persona15',
    'Persona16', 'Persona17', 'Persona18', 'Persona19'
]

# Número total de heats y tamaño de heats
total_heats = 10
tamanio_heat = 4

def generar_heats():
    # Inicializar heats vacíos
    heats = [[] for _ in range(total_heats)]
    participacion = {nombre: 0 for nombre in nombres}

    # Asignar cada persona a dos heats
    for nombre in nombres:
        heats_asignados = 0
        while heats_asignados < 2:
            # Seleccionar un heat aleatorio
            heat_index = random.choice(range(total_heats))
            if len(heats[heat_index]) < tamanio_heat and participacion[nombre] < 2:
                heats[heat_index].append(nombre)
                participacion[nombre] += 1
                heats_asignados += 1

    # Ajuste de heats para asegurar que haya al menos 3 personas en cada uno
    heats = [heat for heat in heats if len(heat) > 0]

    for heat in heats:
        if len(heat) < 3:
            for h in heats:
                if len(h) > 3:
                    heat.append(h.pop())
                    break

    return heats

st.title('Generador de Heats')

if st.button('Generar Heats'):
    heats = generar_heats()
    for i, heat in enumerate(heats):
        st.write(f"Heat {i + 1}: {', '.join(heat)}")

