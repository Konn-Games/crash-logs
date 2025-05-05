FROM python:3
WORKDIR /usr/src/app
COPY app.py app.py
RUN pip install flask Flask-Mail gunicorn 
EXPOSE 80
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
