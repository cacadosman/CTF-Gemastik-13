FROM python:alpine

RUN apk add --update --no-cache g++ gcc libxslt-dev netcat-openbsd
COPY app /opt/app
COPY flag.txt /opt/app/secret_flag

WORKDIR /opt/app

RUN pip install -r requirements.txt
RUN chown -R root:root /opt/app

ENV USER=ctf
ENV UID=1337
ENV GID=1337

RUN addgroup -S ctf
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

EXPOSE 4444
USER ctf

ENTRYPOINT python /opt/app/main.py
