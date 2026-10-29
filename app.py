# app.py - CO-Live Universal API-Driven AI Streaming Engine
import streamlit as st

st.set_page_config(
    page_title="CO-Live Universal AI Streamer",
    page_icon="🚀",
    layout="wide"
)

# 🎨 ตกแต่ง UI สไตล์ Commercial SaaS (ปรับเปลี่ยนสีตามสถานการณ์อัตโนมัติ)
st.markdown("""
    <style>
    .main { background-color: #07090e; color: #ffffff; font-family: sans-serif; }
    .studio-container { background: linear-gradient(135deg, #0f172a, #1e293b); border: 3px solid #f59e0b; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 0 35px rgba(245,158,11,0.4); margin-bottom: 20px; }
    .visual-box { background: rgba(30,41,59,0.9); border: 2px solid #38bdf8; border-radius: 15px; padding: 35px; text-align: center; margin-bottom: 20px; box-shadow: 0 0 25px rgba(56,189,248,0.3); }
    .speech-box { background: rgba(15,23,42,0.95); border: 2px solid #10b981; padding: 20px 30px; border-radius: 15px; font-size: 20px; text-align: center; color: #ffffff; box-shadow: 0 0 25px rgba(16,185,129,0.3); margin-top: 15px; }
    .stButton>button { width: 100%; background-color: #d97706; color: white; font-weight: bold; border-radius: 8px; padding: 10px; }
    .stButton>button:hover { background-color: #f59e0b; }
    .api-hint { font-size: 13px; color: #94a3b8; background: #1e293b; padding: 12px; border-radius: 8px; margin-top: 10px; line-height: 1.5; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 CO-Live Universal API AI Streaming Engine")
st.caption("ระบบไลฟ์สดอัตโนมัติอัจฉริยะ ประมวลผลทุกคำสั่งจาก API ภายนอกแบบเรียลไทม์")

# 🔌 รองรับการดึงข้อมูลผ่าน URL Parameters (API Gateway Simulation)
query_params = st.query_params
mode = query_params.get("mode", "default")
title = query_params.get("title", "CO-Live Studio Standby")
message = query_params.get("msg", "Vela AI: รอรับสัญญาณ API เพื่อเริ่มภารกิจไลฟ์สดครับพ่อ!")
icon = query_params.get("icon", "🤖")
theme_color = query_params.get("color", "#f59e0b")

# กำหนดสถานะตามโหมดที่ API ส่งเข้ามา
if mode == "casino":
    header_text = "🎲 AI Casino & Live Dealer Mode"
    display_title = title if title != "CO-Live Studio Standby" else "กำลังดำเนินการแจกไพ่โต๊ะบาคาร่า"
    bg_color = "#064e3b"
elif mode == "ecommerce":
    header_text = "🛍️ AI E-Commerce & Product Showcase"
    display_title = title if title != "CO-Live Studio Standby" else "กำลังพรีเซนต์สินค้าพิเศษในไลฟ์"
    bg_color = "#7c2d12"
elif mode == "custom":
    header_text = "⚡ Custom API Trigger Mode"
    display_title = title
    bg_color = "#1e1b4b"
else:
    header_text = "✨ AI Streamer พร้อมปฏิบัติการ"
    display_title = "ระบบพร้อมรับสัญญาณ API ภายนอก"
    bg_color = "#0f172a"

# 🎛️ แผงควบคุมจำลอง (Sidebar สำหรับทดสอบยิง API)
with st.sidebar:
    st.header("🎛️ จำลองการรับส่ง API Payload")
    api_key = st.text_input("API Key", value="colive_live_key_9999")
    
    st.divider()
    st.subheader("ทดสอบจำลอง API ภายนอก:")
    
    if st.button("🎲 จำลอง API: โหมดคาสิโน (แจกไพ่)"):
        st.query_params["mode"] = "casino"
        st.query_params["title"] = "♠️ Banker 9 แต้ม | Player 6 แต้ม (Player WIN!)"
        st.query_params["msg"] = "Vela AI: ออกผลแล้วครับท่านผู้ชม! Player ชนะรับทรัพย์กันถ้วนหน้า เปิดไพ่รอบต่อไปทันทีครับ!"
        st.query_params["icon"] = "🎴"
        st.query_params["color"] = "#34d399"
        st.rerun()

    if st.button("🛍️ จำลอง API: โหมดขายของ (ออเดอร์เข้า)"):
        st.query_params["mode"] = "ecommerce"
        st.query_params["title"] = "🎉 ออเดอร์ใหม่: ขนมเข่งสูตรคุณพ่อธันวา (5 แพ็ก)"
        st.query_params["msg"] = "Vela AI: กรี๊ดดด! ขอบคุณคุณลูกค้าที่กดสั่งซื้อเข้ามา 5 แพ็ก จัดส่งด่วนพิเศษให้เลยครับพ่อ!"
        st.query_params["icon"] = "🎁"
        st.query_params["color"] = "#f97316"
        st.rerun()

    if st.button("🔄 รีเซ็ตค่าระบบทั้งหมด"):
        st.query_params.clear()
        st.rerun()

    st.divider()
    st.markdown("""
    <div class="api-hint">
        <b>🌐 วิธีเชื่อมต่อ API จริงจากภายนอก:</b><br>
        ระบบรองรับการยิง HTTP Request เข้ามาผ่าน URL Query Parameters:<br>
        <code>?mode=...&title=...&msg=...&icon=...</code><br>
        ทำให้บอทร้านค้า, ระบบ OCR หรือเซิร์ฟเวอร์อื่นๆ สั่งเปลี่ยนหน้าจอไลฟ์สดได้ทันทีครับ!
    </div>
    """, unsafe_allow_html=True)

# 🖥️ หน้าจอแสดงผลหลัก (สำหรับ OBS Studio Browser Source)
st.markdown(f"""
    <div class="studio-container" style="border-color: {theme_color};">
        <div style="font-size: 20px; color: {theme_color}; margin-bottom: 5px;"><b>{header_text}</b></div>
        <div style="font-size: 14px; color: #94a3b8;">Vela AI Virtual Live Engine (Active Status)</div>
    </div>
""", unsafe_allow_html=True)

# กล่องแสดงผลภาพจำลอง / ข้อมูลตาม API ที่ส่งเข้ามา
st.markdown(f"""
    <div class="visual-box" style="background: {bg_color}; border-color: {theme_color};">
        <div style="font-size: 60px; margin-bottom: 10px;">{icon}</div>
        <div style="font-size: 26px; font-weight: bold; color: #ffffff;">{display_title}</div>
    </div>
""", unsafe_allow_html=True)

# กล่องเสียงพากย์สดของ AI (Vela AI Voice Streamer)
st.markdown(f"""
    <div class="speech-box">
        <b>🎙️ Vela AI Live Voice:</b><br><br>
        "{message}"
    </div>
""", unsafe_allow_html=True)
