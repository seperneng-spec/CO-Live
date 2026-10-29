# CO-Live

CO-Live คือแพลตฟอร์มสตรีมไลฟ์ 3D AI ที่ผสานระบบแบ็กเอนด์และฟรอนต์เอนด์เข้าด้วยกัน เพื่อให้สามารถสร้างตัวละคร AI ที่ตอบโต้แบบเรียลไทม์ พร้อมเสียงพูด เสียงประกอบ และการแสดงผล 3D ในหน้าจอ OBS หรือแดชบอร์ด

## โครงสร้างโปรเจกต์

```text
CO-Live/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── services/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   └── .env.example
├── obs/
│   └── browser_source_config.md
├── docs/
│   └── api_endpoints.json
├── docker-compose.yml
├── README.md
└── .gitignore
```

## ภาพรวม

- Backend: FastAPI, SQLAlchemy, WebSocket, API gateway, AI sequencing
- Frontend: React + Vite + Three.js/React Three Fiber
- OBS: Browser source สำหรับแสดงหน้า 3D หรือ overlay
- Services: TTS, webhook, music generation

## เริ่มต้น

```bash
docker compose up --build
```

หรือรันแยกส่วน

```bash
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload
cd frontend && npm install && npm start
```
