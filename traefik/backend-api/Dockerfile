FROM python:3.10-alpine

WORKDIR /backend-api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY / .backend-api

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["app-api.py"]