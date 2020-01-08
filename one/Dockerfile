FROM python:3

RUN pip install flask

COPY one.py ./one.py

ENV FLASK_APP one.py

CMD flask run --host=0.0.0.0

