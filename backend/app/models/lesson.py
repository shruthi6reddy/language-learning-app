from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id          = Column(Integer, primary_key=True, index=True)
    day_number  = Column(Integer, unique=True, nullable=False, index=True)
    phase       = Column(Integer, nullable=False)   # 1 or 2 for MVP
    title       = Column(String, nullable=False)
    description = Column(String, nullable=True)


class LessonItem(Base):
    __tablename__ = "lesson_items"

    id           = Column(Integer, primary_key=True, index=True)
    lesson_id    = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    order        = Column(Integer, nullable=False)  # sequence within the lesson
    item_type    = Column(String, nullable=False)   # "learn_card", "trace", "flashcard"
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)