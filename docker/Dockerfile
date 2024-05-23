FROM python:3.10-bullseye

WORKDIR /app
COPY requirements.txt requirements.txt
COPY ./src ./src

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "-u", "src/__main__.py"]