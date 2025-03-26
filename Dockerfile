FROM python:3.12-slim

WORKDIR /ai-mmodel-api

COPY ./requirements.txt /ai-mmodel-api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ai-mmodel-api/requirements.txt

COPY . /ai-mmodel-api

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]