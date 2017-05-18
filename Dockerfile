FROM python:2.7.13
MAINTAINER Your Name "tanayr03@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python”, "app.py"]
CMD [“https://github.com/tanayr03/cmpe273-assignment1”]
