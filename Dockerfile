FROM python:3.11-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip setuptools wheel

RUN pip install -e .
RUN pip install pytest cryptography certifi

CMD ["pytest", "-q"]
