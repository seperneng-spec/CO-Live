from sqlalchemy import Boolean, Column, Integer, String, Text

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(200), unique=True, index=True)
    is_active = Column(Boolean, default=True)


class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    key = Column(String(255), unique=True, index=True)
    label = Column(String(100), default="default")


class StreamSession(Base):
    __tablename__ = "stream_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    status = Column(String(50), default="idle")
    title = Column(String(200), default="Live session")
    notes = Column(Text, default="")


class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    action = Column(String(200), default="")
    message = Column(Text, default="")
