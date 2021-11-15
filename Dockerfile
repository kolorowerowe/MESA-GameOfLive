FROM python:3.8-slim-buster


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY game game

EXPOSE 8521

CMD [ "python3", "game/main.py"]