import streamlit as st

# Configuración de la página con el nombre de Fufi
st.set_page_config(page_title="Para Fufi 🌻", page_icon="💛", layout="wide")

# CSS Personalizado: Más "aesthetic" y dedicado a Fufi
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@300;500&display=swap');

    .main {
        background-color: #fffdf0;
    }
    
    .fufi-title {
        text-align: center;
        color: #d4a017;
        font-family: 'Dancing Script', cursive;
        font-size: 65px;
        margin-bottom: 0px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .fufi-subtitle {
        text-align: center;
        color: #b8860b;
        font-family: 'Quicksand', sans-serif;
        font-size: 20px;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 50px;
        border: 2px solid #ffd700;
        background-color: white;
        color: #8b4513;
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        transition: all 0.4s ease;
        height: 3em;
    }

    .stButton>button:hover {
        background-color: #ffd700;
        color: white;
        transform: scale(1.05);
        box-shadow: 0px 5px 15px rgba(255, 215, 0, 0.4);
    }

    .poem-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 20px;
        border: 1px dashed #ffd700;
        font-family: 'Dancing Script', cursive;
        font-size: 24px;
        color: #5d4037;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
        animation: fadeIn 1.5s;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Personalizado
st.markdown("<h1 class='fufi-title'>Flores Amarillas para Fufi</h1>", unsafe_allow_html=True)
st.markdown("<p class='fufi-subtitle'>Porque te mereces un jardín que nunca se marchite ✨</p>", unsafe_allow_html=True)

# Música de fondo (El hit de Floricienta para Fufi)
st.markdown(
    f'<iframe width="0" height="0" src="https://www.youtube.com/embed/wIC18c1Qkcg?autoplay=1&mute=0&loop=1&playlist=wIC18c1Qkcg" frameborder="0" allow="autoplay; encrypted-media"></iframe>',
    unsafe_allow_html=True
)

# Datos de las Flores y Poemas dedicados
flores = [
    {
        "nombre": "Girasol Radiante",
        "imagen": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=500&auto=format&fit=crop",
        "poema": "Fufi, como este girasol que busca el sol, mi mirada siempre busca tu alegría. Eres la luz que ilumina mis días más grises."
    },
    {
        "nombre": "Tulipán Dorado",
        "imagen": "https://images.unsplash.com/photo-1554631221-f9603e6808be?q=80&w=500&auto=format&fit=crop",
        "poema": "Un tulipán para Fufi, elegante y sincero. Representa este cariño puro que por ti siempre espero."
    },
    {
        "nombre": "Rosa de Oro",
        "imagen": "https://images.unsplash.com/photo-1596431933107-00977800729f?q=80&w=500&auto=format&fit=crop",
        "poema": "No hay rosa más bella que la que lleva tu nombre. Que este color amarillo te recuerde lo especial que eres para mí."
    },
    {
        "nombre": "Margarita Feliz",
        "imagen": "https://images.unsplash.com/photo-1464851707681-f9d5fdaccea8?q=80&w=500&auto=format&fit=crop",
        "poema": "Deshojando margaritas supe que te quería, pero estas amarillas dicen que te querré toda la vida, Fufi."
    },
    {
        "nombre": "Orquídea Única",
        "imagen": "https://images.unsplash.com/photo-1521320211110-612140401865?q=80&w=500&auto=format&fit=crop",
        "poema": "Exótica y valiosa, como tu presencia en mi mundo. Una orquídea para la persona más increíble: Fufi."
    }
]

# Distribución del Floral
cols = st.columns(5)

for i, col in enumerate(cols):
    with col:
        st.image(flores[i]["imagen"], use_container_width=True)
        # El botón ahora es una invitación a "tocar" el corazón de la flor
        if st.button(f"Para Fufi 💛", key=i):
            st.session_state[f'selected_{i}'] = True

# Mostrar el poema debajo de la flor seleccionada (con efecto de enfoque)
for i in range(5):
    if st.session_state.get(f'selected_{i}'):
        st.write("---")
        st.markdown(f"<div class='poem-box'>{flores[i]['poema']}</div>", unsafe_allow_html=True)
        st.balloons() # ¡Efecto de celebración al abrir un poema!

# Pie de página
st.markdown("<br><br><p style='text-align: center; color: #d4a017;'>Hecho con mucho 💛 para la mejor persona del mundo.</p>", unsafe_allow_html=True)

