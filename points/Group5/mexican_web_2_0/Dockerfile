FROM python:3

WORKDIR /usr/src/mexican_web_2_0

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./server.py" ]