import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Tanya Odisea", page_icon="🕵️‍♀️", layout="wide")

# Estilo visual para que se vea profesional
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        color: #4F8BF9;
    }
    </style>
    """, unsafe_allow_html=True)

# Título y Subtítulo
st.title("🕵️‍♀️ Tanya Odisea")
st.subheader("Sistema Central de Perfilación y Negociación")

# Menú Lateral para navegar las funciones
with st.sidebar:
    st.image("https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d47353039331e16a02ad.svg", width=50)
    st.title("Panel de Control")
    opcion = st.radio("Seleccioná el módulo:", 
                     ["Inicio", "Perfilación FBI (Inductiva)", "Negociación (Chris Voss)", "Análisis de Escena"])
    st.info("Estado: Sistema Operativo")
    st.write("---")
    st.write("Usuario: Jefe")

# --- LÓGICA DE LOS MÓDULOS ---

if opcion == "Inicio":
    st.write("### Bienvenido al centro de mando, Jefe.")
    st.write("Tanya está lista para analizar patrones de comportamiento y tácticas de persuasión.")
    st.markdown("---")
    st.success("Carga de datos completada. Seleccioná un módulo a la izquierda para empezar.")

elif opcion == "Perfilación FBI (Inductiva)":
    st.header("Análisis de Patrones Inductivos")
    st.write("Este módulo busca similitudes con casos conocidos para predecir el perfil del sujeto.")
    
    col1, col2 = st.columns(2)
    with col1:
        evidencia = st.text_area("Evidencia física (ej. nudos, armas):", placeholder="Describí los hallazgos...")
    with col2:
        comportamiento = st.text_area("Firma o comportamiento:", placeholder="Ej: Ritualista, impulsivo...")
    
    if st.button("Generar Perfil Preliminar"):
        with st.spinner('Analizando base de datos criminal...'):
            st.warning("RESULTADO: Probabilidad de agresor 'Desorganizado'. Probable residencia en un radio de 5km.")

elif opcion == "Negociación (Chris Voss)":
    st.header("Tácticas de Negociación Crítica")
    st.write("Aplicando metodología: *Never Split the Difference*.")
    
    mensaje_sujeto = st.text_input("¿Qué dijo el interlocutor?", placeholder="Ej: 'No voy a salir de acá'...")
    
    if st.button("Generar Etiqueta (Labeling)"):
        etiqueta = f"Parece que sentís que {mensaje_sujeto} es la única forma de que te escuchemos."
        st.info(f"**Sugerencia de Tanya:** '{etiqueta}'")
        st.markdown("> **Tip:** No busques el 'Sí', buscá el 'Es verdad'.")

elif opcion == "Análisis de Escena":
    st.header("Carga de Datos de Campo")
    uploaded_file = st.file_uploader("Subir foto o reporte de la escena:", type=['png', 'jpg', 'jpeg', 'pdf'])
    if uploaded_file:
        st.success("Archivo recibido. Procesando metadatos para análisis de comportamiento...")
