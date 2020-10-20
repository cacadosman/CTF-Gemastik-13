FROM python:alpine

ENV USER=ctf
ENV UID=1337
ENV GID=1337

WORKDIR /opt/app
COPY app /opt/app
COPY flag.txt /opt/app/secret_flag

RUN apk add --update --no-cache g++ gcc libxslt-dev netcat-openbsd
RUN pip install -r requirements.txt
RUN chown -R root:root /opt/app
RUN rm /usr/bin/wget /usr/bin/nc
RUN addgroup -S ctf
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

USER ctf
EXPOSE 4444

ENTRYPOINT python main.py