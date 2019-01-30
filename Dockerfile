FROM ubuntu:18.04

WORKDIR /opt/ocr
RUN mkdir images

COPY src/* ./
COPY requirements.txt .

RUN apt update && apt install -y \
    tesseract-ocr \
    tesseract-ocr-nor \
    python3-pip \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
ENV PORT 5000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT server:app"]
