FROM python:3.8
RUN apt update
RUN apt install python3-pip -y
RUN pip install flask
COPY . .
ENV FLASK_APP=myFlask.py
ENV FLASK_ENV=development
CMD ["flask", "run"]


