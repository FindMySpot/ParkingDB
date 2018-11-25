FROM python:3.6-alpine

ENV FLASK_APP main.py

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD entrypoint.sh .
ADD main.py .
ADD querySensor.py .
ADD reservationChecker.py .

CMD ./entrypoint.sh
