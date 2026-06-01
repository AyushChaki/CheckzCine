import streamlit as st
from core import extract_movie_information


st.set_page_config(
    page_title="CheckzCine",
    page_icon="🎬",
    layout="wide"
)


st.markdown("""
<style>
.stApp {
    background: #fbf4e8;
}

section[data-testid="stSidebar"] {
    background: #efe0bf;
    border-right: 3px solid #7b5b36;
}

section[data-testid="stSidebar"] * {
    color: #241c15 !important;
}

.main .block-container {
    padding-top: 4rem;
    max-width: 1100px;
}

.classic-title {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 58px;
    font-weight: 800;
    color: #2b2118;
    margin-bottom: 10px;
}

.classic-subtitle {
    font-family: Georgia, 'Times New Roman', serif;
    color: #6b5842;
    font-size: 22px;
    margin-top: 10px;
    margin-bottom: 34px;
}

.input-card {
    background: #fff7e8;
    border: 1.5px solid #c9a96a;
    border-radius: 18px;
    padding: 24px 28px;
    margin-bottom: 26px;
    box-shadow: 0 8px 24px rgba(80, 55, 20, 0.10);
}

.info-card {
    background: #fffaf1;
    border-left: 6px solid #7b4f2c;
    border-radius: 18px;
    padding: 22px 26px;
    margin-top: 22px;
    box-shadow: 0 8px 24px rgba(80, 55, 20, 0.12);
}

.metric-card {
    background: #f3ead8;
    border: 1px solid #c9a96a;
    border-radius: 16px;
    padding: 18px 20px;
    margin-bottom: 16px;
    min-height: 120px;
}

.metric-title {
    font-size: 14px;
    font-weight: 700;
    color: #6b5842;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 20px;
    font-weight: 800;
    color: #241c15;
}

textarea {
    background-color: #fffaf1 !important;
    color: #241c15 !important;
    border: 1.5px solid #c9a96a !important;
    border-radius: 14px !important;
    font-size: 16px !important;
}

.stButton > button {
    background: #7b4f2c;
    color: #fffaf1;
    border-radius: 12px;
    border: none;
    padding: 0.75rem 1.5rem;
    font-weight: 700;
}

.stButton > button:hover {
    background: #5f3b20;
    color: #ffffff;
}

h1, h2, h3, h4, h5, h6, p, li, label, span, div {
    color: #241c15;
}
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""
## 🎬 About CheckzCine

**CheckzCine** is a structured movie information extraction app built with **Mistral Small 2603**, **LangChain**, **Pydantic**, and **Streamlit**.

It converts an unstructured movie paragraph into a validated structured output using a Pydantic schema.

### Technical Flow

1. User enters a movie description.
2. LangChain ChatPromptTemplate formats the instruction prompt.
3. Mistral Small 2603 extracts movie metadata.
4. PydanticOutputParser validates the response.
5. Streamlit displays the extracted fields in a clean UI.

### Extracted Fields

- Title
- Release Year
- Genre
- Director
- Cast
- Rating
- Awards
- Plot Summary

### Model Configuration

- Model: Mistral Small 2603
- Temperature: 0.3
- Parser: PydanticOutputParser
- Schema: Movie BaseModel
""")

    st.divider()

    st.markdown("""
## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Pydantic
- python-dotenv
""")


st.markdown(
    '<div class="classic-title">🎬 CheckzCine</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="classic-subtitle">Extract structured movie information from any paragraph using AI.</div>',
    unsafe_allow_html=True
)


st.markdown('<div class="input-card">', unsafe_allow_html=True)

movie_description = st.text_area(
    "Enter the movie paragraph:",
    height=260,
    placeholder="Paste your movie description here..."
)

extract_button = st.button("Extract Information")

st.markdown('</div>', unsafe_allow_html=True)


if extract_button:
    if movie_description.strip() == "":
        st.warning("Please enter a movie paragraph first.")
    else:
        with st.spinner("Extracting structured movie information..."):
            result = extract_movie_information(movie_description)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Movie Title</div>
                    <div class="metric-value">{result.title}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Release Year</div>
                    <div class="metric-value">{result.release_year if result.release_year else "Not Available"}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Rating</div>
                    <div class="metric-value">{result.rating if result.rating else "Not Available"}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('<div class="info-card">', unsafe_allow_html=True)

        st.subheader("🎞️ Core Movie Details")
        st.write("**Director:**", result.director if result.director else "Not Available")
        st.write("**Genre:**", ", ".join(result.genre) if result.genre else "Not Available")
        st.write("**Cast:**", ", ".join(result.cast) if result.cast else "Not Available")

        st.subheader("🏆 Awards & Recognition")
        if result.awards:
            for award in result.awards:
                st.write("-", award)
        else:
            st.write("Not Available")

        st.subheader("📝 Plot Summary")
        st.write(result.plot_summary)

        st.markdown('</div>', unsafe_allow_html=True)