FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /var/app
COPY . /var/app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "run.py"]