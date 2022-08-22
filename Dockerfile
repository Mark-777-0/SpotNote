FROM python:slim

RUN useradd spotnote

WORKDIR /home/spotnote

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY spotnote.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP spotnote.py

RUN chown -R spotnote:spotnote ./
USER spotnote

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
