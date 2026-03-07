FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install pandas matplotlib openpyxl

CMD ["python", "main.py"]