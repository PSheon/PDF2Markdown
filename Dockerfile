from python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -e .
CMD ["python", "main.py"]
