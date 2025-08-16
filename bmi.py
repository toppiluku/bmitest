import streamlit as st
import requests
from pathlib import Path

st.set_page_config(page_title='BODY MASS INDEX')

st.title('BMI Calculator :)')
resx = st.empty()
resx.image('bmi_chart.png')
st.header('Input Your Weight and Height in Box!')

weight = st.number_input('Weight (in Kg.)')
height = st.number_input('Height (in Cm.)')
res = st.empty()

API_URL = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
API_TOKEN = "UrOxuYDAufKNES4N91COk75zwt7dCddH"
SPEAKER_ID = "1"
def vc(text):
    payload = {
        "text": text,
        "speaker": SPEAKER_ID,
        "volume": 1,
        "speed": 1,
        "type_media": "mp3",
        "save_file": "true",
        "language": "th",
        "page": "user"
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "botnoi-token": API_TOKEN
    }

    try:
        res = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        res.raise_for_status()
        data = res.json()

        audio_url = (
            data.get("url")
            or data.get("audio_url")
            or (data.get("data") or {}).get("url")
        )

        if audio_url:
            audio_bytes = requests.get(audio_url, timeout=30).content
            out_path = Path("botnoi_voice.mp3")
            out_path.write_bytes(audio_bytes)
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("ไม่พบลิงก์ไฟล์เสียงใน response")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")

if st.button('Calculate'):
    if height and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"BMI is {bmi:.3f}")
        if bmi > 30:
            st.error('Fat Stage 3')
            res.image('sf.png')
            textsp = "อ้วนแล้วๆๆๆ"
        elif bmi >= 23:
            st.warning('Fat Stage 1-2')
            res.image('cf.png')
            textsp = "เริ่มอ้วนแล้วนะ"
        elif bmi >= 18.5:
            st.success('Normal')
            res.image('nm.png')
            textsp = "ปกติแล้ว ไม่ต้องทำไร"
        else:
            st.info('Thin')
            res.image('th.png')
            textsp = "คุณผอมแล้วนะ"
        vc(textsp)
    else:
        st.write(f"Invalid")
