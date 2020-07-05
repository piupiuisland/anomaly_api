FROM python:3.6.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7777

ENTRYPOINT [ "python" ] 

CMD ["app.py"]
