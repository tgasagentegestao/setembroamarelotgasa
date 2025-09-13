import streamlit as st
import random
import base64

# -------------------------
# Estado
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "sentimento" not in st.session_state:
    st.session_state.sentimento = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# -------------------------
# Page config (WIDE = marcado por padrão)
# -------------------------
st.set_page_config(page_title="Feedback de Sentimento", page_icon="🙂", layout="wide")

# -------------------------
# CSS (sem mexer na largura dos botões)
# -------------------------
st.markdown("""
<style>
.main-title { text-align:center; font-size:28px; color:#FF8C00; font-weight:700; margin: 0 0 1rem; }
.stButton > button {
    background-color:#e0f0ff !important;
    color:#2563eb !important;
    font-size:18px !important;
    font-weight:700 !important;
    padding:0.8em !important;
    border-radius:12px !important;
    margin: .35rem 0 !important;
}
.footer-container { text-align:center; margin-top:2.5rem; }
.footer-text { font-size:18px; font-weight:700; color:#FF8C00; margin-bottom:1rem; }
.footer-logo img { max-width:150px; width:100%; height:auto; display:block; margin:0 auto; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Funções
# -------------------------
def go_to_feedback(sentimento):
    st.session_state.sentimento = sentimento
    st.session_state.feedback = random.choice(
        feedbacks.get(sentimento, ["Não há feedback disponível."])
    )
    st.session_state.page = "feedback"
    st.rerun()

def load_image_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------------
# Feedbacks
# -------------------------
feedbacks = {
    "feliz": [
    "Continue espalhando essa alegria!",
    "A sua felicidade é contagiante!",
    "Que bom te ver assim, sorridente.",
    "Aproveite cada instante desse bom humor."
],
    "triste": [
    "Você não está sozinho nessa caminhada.",
    "Tudo passa, até os momentos mais difíceis.",
    "Se permita sentir, mas lembre-se: isso não é para sempre.",
    "A tristeza também ensina e fortalece."
],
    "ansioso": [
    "Respire fundo: você está seguro agora.",
    "Coloque os pés no chão e sinta o apoio do solo.",
    "Inspire por 4, segure por 4, expire por 6 — repita algumas vezes.",
    "Você não precisa resolver tudo hoje.",
    "Uma coisa de cada vez: priorize o que está ao seu alcance."
],
    "motivado": [
    "Essa energia vai te levar longe!",
    "Aproveite a motivação para dar o próximo passo.",
    "Você está no caminho certo, continue firme!",
    "Nada pode parar quem está determinado."
],
    "calmo": [
    "A serenidade é um tesouro que você já carrega.",
    "Sua calma inspira confiança ao seu redor.",
    "A paz interior que você sente é poderosa.",
    "Esse equilíbrio é sua maior força.",
    "Sua tranquilidade ilumina o ambiente."
],
    "grato": [
    "A gratidão ilumina ainda mais o seu caminho.",
    "Seu coração grato é fonte de abundância.",
    "Na gratidão, você encontra felicidade verdadeira.",
    "Sua gratidão transforma simples momentos em tesouros.",
    "Agradecer é multiplicar bênçãos, e você já faz isso."
],
    "cansado": [
    "Você merece descansar, seu corpo agradece.",
    "Respeite seus limites, o descanso também é produtividade.",
    "Até os mais fortes precisam de pausa.",
    "Um bom descanso pode renovar suas forças."
],
    "confuso": [
    "A confusão é parte natural do aprendizado.",
    "Nem sempre precisamos ter todas as respostas.",
    "É no meio da dúvida que nascem as descobertas.",
    "A clareza vem com o tempo, confie no processo.",
    "Respire fundo, organize seus pensamentos."
],
    "confiante": [
    "Sua confiança abre portas todos os dias.",
    "Acreditar em si mesmo é sua maior força.",
    "Com confiança, você conquista qualquer desafio.",
    "Você transmite segurança e determinação.",
    "Sua confiança inspira quem está ao seu redor."
],
    "esperançoso": [
    "A esperança ilumina seu caminho todos os dias.",
    "Com esperança, você enxerga além dos desafios.",
    "Sua esperança é força que move montanhas.",
    "Nunca perca a esperança, ela é sua maior aliada."
],
    "animado": [
    "Sua animação é contagiante e inspira todos ao redor.",
    "Quando você está animado, tudo fica mais leve.",
    "A energia da sua animação abre caminhos.",
    "Com esse entusiasmo, nada pode te parar.",
    "Sua animação traz alegria para qualquer lugar."
],
    "leve": [
    "Sentir-se leve é como deixar o coração respirar.",
    "Sua leveza ilumina o caminho de quem está perto.",
    "Estar leve é encontrar paz no simples.",
    "Sua leveza inspira tranquilidade."
],
    "realizado": [
    "Você merece celebrar cada conquista realizada.",
    "Sentir-se realizado é colher os frutos do seu esforço.",
    "Sua realização é inspiração para muitos.",
    "Cada passo realizado mostra sua dedicação.",
    "Você é prova de que determinação traz realização."
],
    "inspirado": [
    "Você está inspirado e isso ilumina seu caminho.",
    "A inspiração é o combustível dos grandes sonhos.",
    "Sua inspiração é contagiante para quem está ao seu lado.",
    "Quando você se sente inspirado, o mundo ganha mais cores."
],
    "estressado": [
    "Respire fundo: você é maior que o estresse.",
    "O estresse é passageiro, sua força é permanente.",
    "Faça uma pausa, sua mente agradece.",
    "Você tem o controle da situação, mesmo que pareça difícil.",
    "Cada respiração profunda traz mais calma."
],
    "sozinho": [
    "Você nunca está realmente sozinho, sempre há alguém que se importa.",
    "Sua presença já é valiosa neste mundo.",
    "Há pessoas que torcem por você, mesmo em silêncio.",
    "O universo sempre prepara encontros inesperados.",
    "Você é importante demais para ser esquecido."
]
}

# -------------------------
# Opções
# -------------------------
opcoes = [
    {"emoji": "😊", "label": "Feliz", "key": "feliz"},
    {"emoji": "😞", "label": "Triste", "key": "triste"},
    {"emoji": "😰", "label": "Ansioso", "key": "ansioso"},
    {"emoji": "💪", "label": "Motivado", "key": "motivado"},
    {"emoji": "😌", "label": "Calmo", "key": "calmo"},
    {"emoji": "🙏", "label": "Grato", "key": "grato"},
    {"emoji": "😴", "label": "Cansado", "key": "cansado"},
    {"emoji": "🤔", "label": "Confuso", "key": "confuso"},
    {"emoji": "😎", "label": "Confiante", "key": "confiante"},
    {"emoji": "🌅", "label": "Esperançoso", "key": "esperançoso"},
    {"emoji": "🤩", "label": "Animado", "key": "animado"},
    {"emoji": "🍃", "label": "Leve", "key": "leve"},
    {"emoji": "🏆", "label": "Realizado", "key": "realizado"},
    {"emoji": "✨", "label": "Inspirado", "key": "inspirado"},
    {"emoji": "😣", "label": "Estressado", "key": "estressado"},
    {"emoji": "🌙", "label": "Sozinho", "key": "sozinho"}
]

# -------------------------
# Home
# -------------------------
if st.session_state.page == "home":
    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            font-size: 28px;  /* levemente menor */
            font-weight: bold;
            color: #FF8C00; /* laranja */
            margin-bottom: 10px;
        }
        .title-container {
            text-align: center;
            font-size: 24px;  /* levemente menor */
            font-weight: bold;
        }
        .title-heart {
            display: inline-block;
            color: #FFD700; /* amarelo dourado */
            animation: heartbeat 1.2s infinite;
            margin-right: 6px;
        }
        .title-text {
            color: #FF8C00; /* laranja */
        }
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.2); }
            50% { transform: scale(1); }
            75% { transform: scale(1.2); }
        }
        </style>

        <div class="main-title">Setembro Amarelo - Falar é a melhor solução</div>
        <div class="title-container">
            <span class="title-heart">💛</span>
            <span class="title-text">A TGA quer saber: Como você está se sentindo hoje?</span>
        </div>
    """, unsafe_allow_html=True)

    # 4 colunas exatamente iguais
    for i in range(0, len(opcoes), 4):
        c1, c2, c3, c4 = st.columns(4, gap="small")
        for col, opcao in zip((c1, c2, c3, c4), opcoes[i:i+4]):
            with col:
                # use_container_width => ocupa 100% da coluna (mesma largura)
                if st.button(f"{opcao['emoji']} {opcao['label']}",
                             key=opcao["key"],
                             use_container_width=True):
                    go_to_feedback(opcao["key"])

    # Footer
    try:
        encoded = load_image_base64("tgalogo.png")
        st.markdown(
            f"""
            <div class="footer-container">
                <div class="footer-text">Cada resposta é única e exclusiva para você</div>
                <div class="footer-logo">
                    <img src="data:image/png;base64,{encoded}">
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        st.markdown(
            """
            <div class="footer-container">
                <div class="footer-text">Cada resposta é única e exclusiva para você</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------
# Feedback
# -------------------------
elif st.session_state.page == "feedback":
    emoji = next(o['emoji'] for o in opcoes if o['key'] == st.session_state.sentimento)
    st.markdown(
        f"<h2 style='text-align: center; font-size: 28px; color: #2563eb;'>Você escolheu: {st.session_state.sentimento.capitalize()} {emoji}</h2>",
        unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='font-size:22px; font-weight:600; color:#2563eb; text-align:center; margin-top:25px;'>{st.session_state.feedback}</div>",
        unsafe_allow_html=True
    )
