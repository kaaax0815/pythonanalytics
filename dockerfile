FROM python:3.8
COPY requirements.txt /usr/src/app
WORKDIR /usr/src/app
COPY . .
VOLUME /usr/src/app/database
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "app.py" ]