import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
def load_gif(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
gif = load_gif("https://lottie.host/64c4691d-289b-4607-a5d3-fce765442fa3/KSzwm2b1xU.json")
gif1 = load_gif("https://lottie.host/68e189ac-3323-4b72-ba0a-2754b5257fe6/Sx1DzMYTaN.json")
st.set_page_config(page_title="Anh thich em nhieu qua roi", page_icon="😭", layout="wide")
st.subheader("Anh thực sự xin lỗi, rất rất rất xin lỗi, anh không muốn nó kết thúc như thế này")
st.title("Anh không thể chấp nhận việc mình phải ngừng lại như vậy vì anh đã quá yêu em💔")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Mọi lời giải thích bây giờ anh thốt ra đều có thể quay lại đấm nát mặt anh nhưng anh vẫn")
        st.write("sẽ nói là cái lúc con l nớ gửi link anh chỉ nghĩ đơn giản là mình bấm vào kết bạn nó sau ")
        st.write("đó xoá thôi nhưng mà cái locket nó bị thế đấy nên anh chả ngờ được, cái lúc kể cho em")
        st.write("thì anh nghĩ đã xoá rồi thế nên lúc đấy anh nghĩ là bảo chưa bấm vào link hay bấm rồi thì ")
        st.write("nó cũng không khác gì nhau với lúc đấy em có vẻ rất bực nên anh nói chưa bấm vào để")
        st.write("em nguôi thôi chứ không có gì sâu xa cả, em cũng biết là anh là 1 cái thằng nghĩ rất ít ")
        st.write("nên những cái chuyện như thế này anh không nghĩ gì nhiều cả, dù trước đó đã có rất ")
        st.write("nhiều chuyện tương tự xảy ra và tất cả đều do anh không nghĩ thông suốt, anh biết là anh")
        st.write("làm ẩu, anh biết là anh ngu nhưng anh cũng biết là anh rất yêu em thế nhưng anh quá ")
        st.write("tệ trong việc thay đổi cái tính này nên anh muốn thay đổi nó để không làm em ")
        st.write("phải buồn.")
    with right_column:
        st_lottie(gif, height=500, key="gif")
st.write("----------")
st.write("Hiện tại anh rất sợ việc em bỏ đi vì anh quá yêu em rồi, biết có lẽ những dòng này có thể phang lại")
st.write("anh như những nhân vật nữ trong các bộ haiten gangbang nhưng anh vẫn muốn nói ra, anh muốn mình có")
st.write("thể giải quyết chuyện này một cách rõ ràng, anh không thể chấp nhận việc mình kết thúc, anh không")
st.write("thể để mất em được vì em là tất cả mọi thứ hiện tại của anh, anh yêu em...")
st.write("----------")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("[Chết trong em](https://open.spotify.com/track/1dUmmBh2nw8XzEI3au0uFs?si=cd622b86823e4014)")
        st.write("Chết trong tôi một phần tim thao thức")
        st.write("Chết trên môi một mùi hương chưa dứt")
        st.write("Chết theo em bầu trời sấm chớp mây đen")
        st.write("Chết trong em một niềm tin chôn giấu")
        st.write("Chết trong tôi một phần tim nung nấu")
        st.write("Chết trong đêm và tình mãi chết trong đêm")
        st.write("Tình như khúc nhạc xót xa")
        st.write("Trong đêm tối lặng")
        st.write("Mắt ta đang nơi lặng im một mình")
        st.write("Ôm lấy hết cô đơn như trong đời ta")
        st.write("💔💔💔")
    with right_column:
        st_lottie(gif1, height=500, key="gif1")
st.write("-----------")
st.write("Anh thực sự quá yêu em rồi, em là tất cả đối với anh, anh không muốn nó kết thúc như thế này")
st.write("giờ mà em đi anh không còn bất kì mục đích gì để tồn tại nữa, anh không chấp nhận đâu😔😭")
video1 = open("video.mp4", "rb")
st.video(video1)
st.write("-----------")
st.write("P/s: hjhj iu tlinh quá rùi, đp ngồi từ 1h30 đến 5h30 sáng đấy đều đp vẫn sẽ làm vì Tlinh")
st.write("chi chơ đau lưng, bùn ngủ mấy ngày là hết à nhưng mờ mất tlinh thì đau đến cúi đời quái")