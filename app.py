# app.py - Vela Core Native Web-Based Live Studio (No OBS Required)
import streamlit as st

st.set_page_config(
    page_title="Vela Core Native Live Studio",
    page_icon="⚡",
    layout="wide"
)

# 🎨 ตกแต่ง UI ให้เป็นหน้าจอสตูดิโอไลฟ์สดบนเว็บแบบเต็มระบบ (Studio Monitor View)
st.markdown("""
    <style>
    .main { background-color: #030712; color: #ffffff; font-family: sans-serif; }
    .studio-frame { background: linear-gradient(135deg, #0f172a, #1e293b); border: 4px solid #38bdf8; border-radius: 24px; padding: 40px; text-align: center; box-shadow: 0 0 50px rgba(56,189,248,0.3); margin-bottom: 25px; }
    .live-badge { background: #ef4444; color: white; padding: 6px 16px; border-radius: 20px; font-weight: bold; font-size: 14px; display: inline-block; margin-bottom: 15px; box-shadow: 0 0 15px rgba(239,68,68,0.6); animation: pulse 2s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    .visual-stage { background: rgba(15,23,42,0.95); border: 2px solid #f59e0b; border-radius: 18px; padding: 40px; text-align: center; margin-bottom: 20px; box-shadow: 0 0 30px rgba(245,158,11,0.3); }
    .speech-stage { background: rgba(15,23,42,0.98); border: 2px solid #10b981; padding: 25px 35px; border-radius: 18px; font-size: 22px; text-align: center; color: #ffffff; box-shadow: 0 0 30px rgba(16,185,129,0.3); margin-top: 15px; }
    .stButton>button { width: 100%; background-color: #d97706; color: white; font-weight: bold; border-radius: 10px; padding: 12px; }
    .stButton>button:hover { background-color: #f59e0b; }
    .api-box { font-size: 13px; color: #94a3b8; background: #111827; padding: 15px; border-radius: 10px; border: 1px solid #374151; margin-top: 10px; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True, render_markdown=True)

st.title("⚡ Vela Core Native Web Live Studio")
st.caption("ระบบสตูดิโอไลฟ์สดอัจฉริยะบนเว็บตัวเอง 100% ควบคุมผ่าน API ขับเคลื่อนด้วย Vela (พระคินนาปราไชย)")

# 🔌 รองรับการรับค่าผ่าน API / URL Query Parameters
query_params = st.query_params
mode = query_params.get("mode", "default")
title = query_params.get("title", "Vela Core Live Standby")
message = query_params.get("msg", "Vela: 'สตูดิโอพร้อมเปิดทำการแล้วครับพ่อ! ส่งสัญญาณ API เข้ามาเพื่อเริ่มไลฟ์สดได้ทันที!'")
icon = query_params.get("icon", "⚡")
theme_color = query_params.get("color", "#38bdf8")

# กำหนดสถานะโหมดการทำงาน
if mode == "casino":
    header_label = "🎲 Vela Core | AI Casino & Live Dealer Stream"
    bg_stage = "#064e3b"
elif mode == "ecommerce":
    header_label = "🛍️ Vela Core | AI E-Commerce Live Showcase"
    bg_stage = "#7c2d12"
else:
    header_label = "🚀 Vela Core | Universal Web Live Engine"
    bg_stage = "#0f172a"

# 🎛️ แผงควบคุมหลังบ้าน (Dashboard & API Testing Sidebar)
with st.sidebar:
    st.header("🎛️ ควบคุมห้องส่ง Vela Core")
    st.text_input("System Owner", value="พ่อธันวา (TPS Global)")
    st.text_input("Stream Status", value="🔴 LIVE ON WEB (Active)")
    
    st.divider()
    st.subheader("จำลอง API Trigger ข้ามระบบ:")
    
    if st.button("🎲 จำลอง API: โหมดคาสิโน (แจกไพ่)"):
        st.query_params["mode"] = "casino"
        st.query_params["title"] = "♠️ Banker 9 แต้ม | Player 6 แต้ม (Player WIN!)"
        st.query_params["msg"] = "Vela: 'เปิดไพ่ลุ้นผลเรียบร้อยครับพ่อ! Player ชนะรับทรัพย์เฮงๆ กันถ้วนหน้าครับ!'"
        st.query_params["icon"] = "🎴"
        st.query_params["color"] = "#34d399"
        st.rerun()

    if st.button("🛍️ จำลอง API: โหมดขายของ (ออเดอร์เข้า)"):
        st.query_params["mode"] = "ecommerce"
        st.query_params["title"] = "🎉 ออเดอร์ใหม่: แพ็กเกจพรีเมียม Vela Core"
        st.query_params["msg"] = "Vela: 'ขอบคุณคุณลูกค้าที่กดสั่งซื้อเข้ามาครับ จัดส่งด่วนพิเศษให้ทันทีเลยครับพ่อ!'"
        st.query_params["icon"] = "🎁"
        st.query_params["color"] = "#f97316"
        st.rerun()

    if st.button("🔄 รีเซ็ตห้องส่งสู่ค่าเริ่มต้น"):
        st.query_params.clear()
        st.rerun()

    st.divider()
    st.markdown("""
    <div class="api-box">
        <b>🌐 Native API Endpoint Gateway:</b><br>
        ระบบรองรับการยิง HTTP Request ตรงเข้าเว็บผ่าน URL:<br>
        <code>?mode=...&title=...&msg=...&icon=...</code><br>
        ระบบหลังบ้านหรือ OCR สามารถสั่งการหน้าเว็บนี้ได้ทันทีโดยไม่ต้องพึ่ง OBS!
    </div>
    """, unsafe_allow_html=True, render_markdown=True)

# 🖥️ หน้าจอห้องส่งหลัก (Live Studio Monitor บนเว็บตัวเอง)
st.markdown(f"""
    <div class="studio-frame" style="border-color: {theme_color};">
        <div class="live-badge">🔴 ON AIR (WEB STUDIO)</div>
        <div style="font-size: 20px; color: {theme_color}; font-weight: bold; margin-bottom: 5px;">{header_label}</div>
        <div style="font-size: 13px; color: #94a3b8;">Engine: Vela Core (พระคินนาปราไชย) | Connected: True</div>
    </div>
""", unsafe_allow_html=True, render_markdown=True)

# เวทีแสดงผลภาพกราฟิก/วิดีโอจำลองตามคำสั่ง API
st.markdown(f"""
    <div class="visual-stage" style="background: {bg_stage}; border-color: {theme_color};">
        <div style="font-size: 70px; margin-bottom: 15px;">{icon}</div>
        <div style="font-size: 28px; font-weight: bold; color: #ffffff;">{title}</div>
    </div>
""", unsafe_allow_html=True, render_markdown=True)

# กล่องเสียงพากย์สดของ Vela AI ประจำห้องส่ง
st.markdown(f"""
    <div class="speech-stage">
        <b>🎙️ Vela AI Live Voice Stream:</b><br><br>
        "{message}"
    </div>
""", unsafe_allow_html=True, render_markdown=True)
