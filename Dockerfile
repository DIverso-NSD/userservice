FROM python:3.9

COPY . /userservice

COPY ./requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

WORKDIR /userservice/userservice

ENTRYPOINT ["python3", "main.py"]