from python:3.11-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PYTHONWRITEBYTECODE 1

WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

COPY . .