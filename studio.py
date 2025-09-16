import streamlit as st
import requests

# Imagens dos personagens
IMAGES = {
    "Totoro": "https://i.pinimg.com/736x/3f/df/c3/3fdfc3c44e785d234cac00a90b88d2a8.jpg",
    "Satsuki": "https://i.pinimg.com/736x/1c/2f/ff/1c2fff27e3c9754e50829b2fb8eb0898.jpg",
    "Mei": "https://i.pinimg.com/1200x/6a/b1/f7/6ab1f7c48c1a3b29e8f9d7564b4cf891.jpg",
    "Catbus": "https://i.pinimg.com/736x/8f/24/55/8f24556755d8763398a830e067434872.jpg",
    "Pai": "https://i.pinimg.com/736x/e0/3d/f2/e03df2c9f97b6c44123897b66d448808.jpg",
    "Mãe": "https://i.pinimg.com/736x/10/5a/6d/105a6db281101a11fd838718ecf0f955.jpg",
    "Chibi-Totoro": "https://i.pinimg.com/736x/8b/1a/a8/8b1aa8815667105a24bed183d4f83b77.jpg",
    "Chibi-Chibi": "https://i.pinimg.com/736x/ec/fd/7d/ecfd7ddabe2163db97609ae60b85fc9a.jpg",
    "Kanta": "https://i.pinimg.com/736x/23/26/8f/23268fe977c989915ef4e95be0ff1e97.jpg"
}


def get_totoro_data():
    try:
        response = requests.get("https://ghibliapi.vercel.app/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49")
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def get_locations_data():
    try:
        response = requests.get("https://ghibliapi.vercel.app/locations/")
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def mostrar_dados_filme(film):
    st.header(f"🎬 {film.get('title', 'Título não disponível')}")
    st.subheader("📖 Sinopse")
    st.write(film.get('description', 'Descrição não disponível.'))

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Diretor:** {film.get('director', 'Desconhecido')}")
        st.markdown(f"**Produção:** {film.get('producer', 'Desconhecido')}")
        st.markdown(f"**Lançamento:** {film.get('release_date', 'Desconhecido')}")
        st.markdown(f"**Duração:** {film.get('running_time', 'Desconhecido')} minutos")
        st.markdown(f"**Classificação:** {film.get('rt_score', 'Desconhecido')}/100")
        st.markdown(f"**Gêneros:** {', '.join(film.get('genre', [])) if 'genre' in film else 'Não disponível'}")
    with col2:
        st.markdown(f"**Links:**")
        st.markdown("- Assistir Trailer (https://www.youtube.com/watch?v=92a7Hj0ijLs)")

def curiosidades_section():
    st.subheader("🌟 Curiosidades sobre Totoro")
    curiosidades = [
        "Totoro se tornou o mascote oficial do Studio Ghibli.",
        "O filme estreou em 1988, junto com 'Túmulo dos Vagalumes' no Japão.",
        "O nome Totoro vem da forma como a personagem Mei pronuncia 'Troll' (トロール).",
        "O ônibus-gato (Nekobasu) foi inspirado em lendas urbanas japonesas sobre criaturas felinas.",
        "Hayao Miyazaki criou Totoro como um símbolo de inocência, natureza e imaginação.",
        "No Japão, existe até uma floresta chamada 'Floresta de Totoro', preservada por fãs."
    ]
    for c in curiosidades:
        st.markdown(f"- {c}")

def localidades_section():
    st.subheader("🗺️ Localidades Principais do filme!")
    localidades = [
        {"nome": "Casa dos Kusakabe", "descricao": "Residência das irmãs Satsuki e Mei."},
        {"nome": "Floresta", "descricao": "Onde elas encontram os Totoros."},
        {"nome": "Ponto de ônibus", "descricao": "Onde esperam por Totoro em uma das cenas mais icônicas."},
        {"nome": "Hospital de Yasuko", "descricao": "O hospital onde a mãe das meninas, Yasuko, está internada."},
        {"nome": "Campo de Arroz", "descricao": "Onde as irmãs exploram a natureza ao lado de Totoro."}
    ]
    for local in localidades:
        st.markdown(f"### {local['nome']}")
        st.write(local['descricao'])
        st.markdown("---")

def locations_section():
    st.subheader("📍 Localidades do universo Ghibli")
    locations = get_locations_data()
    if locations:
        for location in locations:
            st.markdown(f"### {location['name']}")
            st.write(f"**Clima:** {location['climate']}")
            st.write(f"**Topografia:** {location['terrain']}")
            st.markdown("---")
    else:
        st.write("Não foi possível carregar os dados das localidades.")

def personagens_section():
    st.subheader("👥 Personagens")

    personagens = {
        "Totoro": {
            "descricao": "Criatura mágica da floresta, símbolo de inocência e amizade.",
            "curiosidade": "Totoro se comunica de forma misteriosa e é o mascote do Studio Ghibli."
        },
        "Satsuki": {
            "descricao": "Irmã mais velha, corajosa e responsável.",
            "curiosidade": "Ela cuida da irmã e enfrenta desafios para manter a família unida."
        },
        "Mei": {
            "descricao": "Irmã mais nova, curiosa e energética.",
            "curiosidade": "Ela foi quem descobriu Totoro pela primeira vez."
        },
        "Catbus": {
            "descricao": "Ônibus-gato mágico que transporta os personagens pela floresta.",
            "curiosidade": "Inspirado em lendas japonesas sobre criaturas felinas."
        },
        "Pai": {
            "descricao": "Tatsuo Kusakabe, professor universitário e pai amoroso.",
            "curiosidade": "Ele mantém a família unida e apoia as filhas nas aventuras."
        },
        "Mãe": {
            "descricao": "Yasuko Kusakabe, mãe das meninas, hospitalizada durante o filme.",
            "curiosidade": "Mesmo doente, inspira coragem e afeto para a família."
        },
        "Chibi-Totoro": {
            "descricao": "Pequeno Totoro azul, acompanha os outros Totoro.",
            "curiosidade": "Muito tímido, aparece e desaparece rapidamente em algumas cenas."
        },
        "Chibi-Chibi": {
            "descricao": "Menor Totoro branco, mais difícil de ver.",
            "curiosidade": "Simboliza a magia da floresta e aparece em momentos especiais do filme."
        },
        "Kanta": {
            "descricao": "Garoto vizinho das meninas, simpático e prestativo.",
            "curiosidade": "Ajuda Satsuki e Mei em várias pequenas aventuras."
        }
    }

    for nome, dados in personagens.items():
        colunas = st.columns([1, 2, 3])
        with colunas[0]:
            if nome in IMAGES:
                st.image(IMAGES[nome], width=100)
        with colunas[1]:
            st.markdown(f"**{nome}**")
            st.markdown(f"_{dados['descricao']}_")
        with colunas[2]:
            st.markdown(f"🧠 **Curiosidade:** {dados['curiosidade']}")
        st.markdown("---")


def main():
    st.set_page_config(page_title="Meu Amigo Totoro", page_icon="🍂")

    
    st.image(IMAGES["Totoro"], use_column_width=True)
    st.title("🌿 Meu Amigo Totoro")
    st.write("Explore informações sobre esse clássico do Studio Ghibli.")

    if st.button("🔎 Carregar informações do filme"):
        film = get_totoro_data()
        if film:
            st.success("✨ Dados carregados com sucesso!")
            mostrar_dados_filme(film)
            curiosidades_section()
            localidades_section()
            personagens_section()
            locations_section()
        else:
            st.error("❌ Não foi possível obter os dados do filme.")

    st.markdown("---")
    st.caption("📡 Dados fornecidos pela API Studio Ghibli — https://ghibliapi.vercel.app")

if __name__ == "__main__":
    main()
