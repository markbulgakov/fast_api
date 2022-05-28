from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import Session

from app.database import Base


class Occurrence(Base):
    __tablename__ = 'occurrences'

    id = Column(Integer, primary_key=True)
    keyword = Column(String)
    occurrences = Column(Integer)
    date_time = Column(DateTime, index=True)

    @classmethod
    def get_occurrences(cls, db: Session, date_time: datetime):
        """ Return amount(sum) of occurrences grouped by keyword """
        return db.query(cls.keyword, func.sum(cls.occurrences)).filter(cls.date_time >= date_time).group_by(cls.keyword).all()


    @classmethod
    def create_occurrence(cls, db: Session, keyword: str, occurrences: int, date_time: datetime = datetime.now()):
        occurrence = cls(keyword=keyword, occurrences=occurrences, date_time=date_time)
        db.add(occurrence)
        db.commit()
        db.refresh(occurrence)
        return occurrence
