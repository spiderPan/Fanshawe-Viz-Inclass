FROM python:3.6
WORKDIR /code
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["scrapyrt", "-i", "0.0.0.0"]

