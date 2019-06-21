FROM python:3

WORKDIR /usr/src/mexican_web

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./server.py" ]