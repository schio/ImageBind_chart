# from preprocess import Preprocess
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Chart_studio ImageBind",
    page_icon="🥰",
    # layout="wide",
    # initial_sidebar_state="expanded",
)

logo_color = "#d16246"


def m(text, head=0, color=None, head_color=None):
    if head:
        if head_color:
            text = f"<h{head} style='color:{head_color};'>{text}</h{head}>"
        else:
            text = f"<h{head}>{text}</h{head}>"
    if color:
        text = f'<p styple="color:{color}";>{text}</p>'
    st.markdown(text, unsafe_allow_html=True)
    return text

st.markdown("""
# ImageBind made by FAIR, Meta AI

[Github link](https://github.com/facebookresearch/ImageBind)
""")