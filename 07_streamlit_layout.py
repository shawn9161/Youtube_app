import streamlit as st

# 페이지의 기본 설정을 정의합니다.
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
)

# 타이틀과 헤더를 추가합니다.
st.title('이것은 타이틀 입니다')
st.header('헤더를 입력할 수 있어요!')

# 페이지를 세 개의 세로 열로 나눕니다.
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

# 열의 너비 비율을 조정합니다.
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
   st.video("https://www.youtube.com/watch?v=A8brfTw5S0w")
   st.video("https://www.youtube.com/watch?v=jIG4AaIy-5k")
   st.video("https://www.youtube.com/watch?v=7fg_klS-2kw")
   st.video("https://www.youtube.com/watch?v=CHp0Kaidr14")

# 사이드바를 생성하고, 라디오 버튼을 추가합니다.
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# 세 개의 탭을 생성합니다.
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

