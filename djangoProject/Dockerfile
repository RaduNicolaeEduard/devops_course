FROM python

WORKDIR /app

COPY . .

EXPOSE 8080

RUN pip3 install -r requirements.txt

CMD [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000" ]