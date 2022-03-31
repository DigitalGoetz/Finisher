FROM python:3.9

COPY run_random.py /app/run_random.py

CMD ["python3", "/app/run_random.py"]