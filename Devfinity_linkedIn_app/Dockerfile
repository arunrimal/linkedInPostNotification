FROM python:3.9.5

WORKDIR /app

COPY . .

COPY requirements.txt ./
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt