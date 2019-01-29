FROM ubuntu:18.04

WORKDIR /opt/ocr
RUN mkdir images

COPY src/* ./
COPY requirements.txt .

RUN apt update -y
RUN apt install tesseract-ocr tesseract-ocr-nor python3-pip libsm6 libxext6 -y

RUN pip3 install -r requirements.txt

CMD ["python3", "server.py"]
