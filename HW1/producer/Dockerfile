FROM python:3.7-alpine

COPY requirements.txt /requirements.txt
COPY produce.py /produce.py
RUN pip install -r requirements.txt
CMD ["python", "-u", "/produce.py"]
