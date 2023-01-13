FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
RUN pip install flask
COPY . .
ENV FLASK_APP=td_flask.py
ENV FLASK_ENV=development
CMD ["flask", "run"]


