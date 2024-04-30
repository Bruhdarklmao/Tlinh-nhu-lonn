import requests
import streamlit as st
from streamlit_lottie import st_lottie
def load_gif(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
gif = load_gif("https://lottie.host/f457ac70-c429-434d-8d3e-87a0e075b3f9/jNmKqcOU1M.json")
gif1 = load_gif("https://lottie.host/91674f66-ae5e-4a95-8ebe-a5397b16bed5/s03HhgIkdG.json")
st.set_page_config(page_title="Thich Tlinh qua roi",page_icon="🗣",layout="wide")
st.subheader("A chợt nhận ra mình có một cái gì đó với Tlinh mất rồi")
st.title("Cho a xin một phút để xem nó là gì được không?🗣☝⏰")
st.write("Chỉ một phút thôi[...](https://open.spotify.com/track/1Ph96WpdjNlwD6iKRE2Xa3?si=16485265c8b34d4a)")
st.write("[Đừng bấm vào link segg đấy...](https://youtu.be/SY6KRlMHHd0)")
st.write("----------")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("[Xanh](https://open.spotify.com/track/7vyRxHk6QcuvexB9vXmhlV?si=11996240a525473b)")
        st.write("Mơ một giấc mơ màu xanh")
        st.write("Âm nhạc lướt đi thật nhanh")
        st.write("Như một thói quen của anh")
        st.write("Con đường màu xanh")
        st.write("Xanh màu lá xanh đại dương")
        st.write("Em là nắng anh là sương")
        st.write("Không còn nhớ không còn thương")
        st.write("Thiên đường")
        st.write("Cho tới khi")
        st.write("Báo thức bắt anh quay về thực tế")
        st.write("Cho một giây vượt qua giấc mơ chợt quên chợt quên đi")
        st.write("Chuyện tình hư cấu")
        st.write("Anh ngáp dài")
        st.write("Giấu giấc mơ em sâu vào chăn gối")
        st.write("Xanh thật xanh một câu hát ru rồi phai nhòa phai nhòa trong ban sơ")
        st.write("⚪⚪⚪")
    with right_column:
        st_lottie(gif, height=500, key="gif")
st.write("-----------")
st.write("Làm hết đống này xong lưng biến thành đường cong hoàn hảo rồi mà tlinh vẫn bỏ đòngphin thì chịu rồi😔😭")