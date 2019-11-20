FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install flask gunicorn
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "run:app"]