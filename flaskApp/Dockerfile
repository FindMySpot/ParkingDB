FROM python:3.6-alpine

ENV FLASK_APP main.py

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD main.py .

CMD ["python", "./querySensor.py"]
CMD ["python", "./reservationChecker.py"]

CMD flask run --host=0.0.0.0
EXPOSE 6060
