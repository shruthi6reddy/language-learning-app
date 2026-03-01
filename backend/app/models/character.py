from sqlalchemy import Column, Integer, String
from app.db import Base

class Character(Base):
    __tablename__ = "characters"

    id             = Column(Integer, primary_key=True, index=True)
    telugu         = Column(String, nullable=False)       # e.g. అ
    romanisation   = Column(String, nullable=False)       # e.g. "a"
    ipa            = Column(String, nullable=True)        # e.g. "ə"
    character_type = Column(String, nullable=False)       # "vowel" or "consonant"
    phonetic_group = Column(String, nullable=True)        # e.g. "velar", "retroflex"
    day_introduced = Column(Integer, nullable=False)      # which lesson day introduces this
    audio_url      = Column(String, nullable=True)        # empty for now, ready for v2