import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from gtts import gTTS
import os
# صورة المساعد
st.image("robot.png", width=200)

# قراءة كل الشيتات
xls = pd.ExcelFile("data.xlsx")

# اختيار الشيت
sheet = st.selectbox("اختار الشيت", xls.sheet_names)

# قراءة الشيت المختار
df = pd.read_excel("data.xlsx", sheet_name=sheet)

st.write("📊 البيانات:", df.head())

st.title("🤖 المساعد الذكي")

# إدخال الرقم
number = st.text_input("ادخل الرقم التعريفي")

# دالة الصوت داخل المتصفح
def speak(text):
    tts = gTTS(text=text, lang='ar')
    filename = "voice.mp3"
    tts.save(filename)
    audio_file = open(filename, 'rb')
    st.audio(audio_file.read(), format='audio/mp3')

# زر البحث
if st.button("بحث"):

    number = str(number).strip()

    result = df[df.iloc[:, 0].astype(str).str.strip() == number]

    if not result.empty:
        st.success("تم العثور على البيانات ✔️")
        st.write(result)
        speak("تم العثور على البيانات")
    else:
        st.error("الرقم غير موجود ❌")
        speak("الرقم غير موجود")