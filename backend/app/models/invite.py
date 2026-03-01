from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db import Base 

class Invite(Base):
    __tablename__ = "invites"

    id         = Column(Integer, primary_key=True, index=True)
    code       = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    used_at    = Column(DateTime(timezone=True), nullable=True)
    used_by    = Column(Integer, ForeignKey("users.id"), nullable=True)
