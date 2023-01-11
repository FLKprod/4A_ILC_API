FROM Python3
RUN pip3 install flask
ADD file /myFlask.py
RUN export FLASK_APP=myFlask.py
RUN export FLASK_ENV=development
RUN flask run
RUN curl -X GET http://127.0.0.1:5000
RUN curl -X POST http://127.0.0.1:5000/4/Jean
CMD ["Python3","myFlask.py"]