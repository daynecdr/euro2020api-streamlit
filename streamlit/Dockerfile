FROM python:3.9.5

WORKDIR /api

ADD . /api/

RUN pip install -r requirements.txt

CMD streamlit run --server.port $PORT euroapp.py