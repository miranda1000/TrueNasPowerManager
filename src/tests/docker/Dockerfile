FROM python:3.10-bullseye

WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install pytest==8.2.1

WORKDIR /app/src
CMD ["python3", "-m", "pytest", "tests/"]