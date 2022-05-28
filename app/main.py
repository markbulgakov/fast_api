from datetime import timedelta

from fastapi import FastAPI, Depends
from typing import Dict, Any, List, Union
from starlette.requests import Request

from app.models import *
from app.database import SessionLocal, engine
from app.utils import count_occurrences

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db() -> Session:
    """ Return DB Session object """

    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post('/api/events/')
async def post_events(request: Request, db: Session = Depends(get_db)) -> Dict[str, Any]:
    """ Receive a sentence (String) in the request and counts the number of the occurrences of specific keywords """

    request_body: bytes = await request.body()
    sentence: str = request_body.decode("utf-8")
    occurrences: Dict[str, int] = count_occurrences(text=sentence)
    request_date_time: datetime = datetime.now()

    for keyword, keyword_occurrences in occurrences.items():
        Occurrence.create_occurrence(db=db, keyword=keyword, occurrences=keyword_occurrences, date_time=request_date_time)

    return {'sentence': sentence, 'occurrences': occurrences}


@app.get('/api/stats/')
def get_stats(interval: int, db: Session = Depends(get_db)) -> Dict[str, int]:
    """ Return a JSON with the number of occurrence of the above keywords in the received interval time """

    date_time: datetime = datetime.now() - timedelta(seconds=interval)
    grouped_occurrences: List[List[Union[str, int]]] = Occurrence.get_occurrences(db=db, date_time=date_time)
    occurrences: Dict[str, int] = {}

    for group in grouped_occurrences:
        occurrences[group[0]] = group[1]

    return occurrences
