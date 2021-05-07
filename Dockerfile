FROM python:3.9-slim-buster 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
USER 1000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]