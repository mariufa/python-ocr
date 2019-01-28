FROM python:3.6-alpine

WORKDIR /opt/ocr

COPY . /opt/ocr

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

CMD ["venv/bin/python", "./server.py"]