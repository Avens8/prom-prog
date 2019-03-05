FROM python:3.7-alpine

COPY requirements.txt /requirements.txt
COPY consume.py /consume.py
RUN pip install -r requirements.txt
CMD ["python", "-u", "/consume.py"]
