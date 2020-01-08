FROM python:3

RUN pip install flask

COPY three.py ./three.py

ENV FLASK_APP three.py

CMD flask run --host=0.0.0.0

