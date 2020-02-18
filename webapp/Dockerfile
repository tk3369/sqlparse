FROM alpine

RUN apk update \
 && apk add python3 \
 && pip3 install --upgrade pip \
 && pip3 install flask \
 && apk add git

RUN addgroup -S mygroup && adduser -S myuser -G mygroup -h /app

USER myuser

WORKDIR /app

COPY sqlparse sqlparse
COPY webapp/run.sh .
COPY webapp/app.py .

EXPOSE 5000

CMD ["/app/run.sh"]

