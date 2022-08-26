FROM python:3.8.10-alpine

WORKDIR /botQ-poll
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy project
COPY . .
CMD python3 /botQ-poll/botQ.py
#ENTRYPOINT ["python3", '/botQ-poll/botQ.py']