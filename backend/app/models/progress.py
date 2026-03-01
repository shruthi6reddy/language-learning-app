from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db import Base

class UserProgress(Base):
    __tablename__ = "user_progress"

    id          = Column(Integer, primary_key=True, index=True)
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_id   = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    status      = Column(String, default="not_started")  # "not_started", "in_progress", "complete"
    completed_at = Column(DateTime(timezone=True), nullable=True)


class UserItemResult(Base):
    __tablename__ = "user_item_results"

    id             = Column(Integer, primary_key=True, index=True)
    user_id        = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_item_id = Column(Integer, ForeignKey("lesson_items.id"), nullable=False)
    result         = Column(String, nullable=True)   # "pass", "fail", "skipped"
    attempts       = Column(Integer, default=0)
    completed_at   = Column(DateTime(timezone=True), nullable=True)