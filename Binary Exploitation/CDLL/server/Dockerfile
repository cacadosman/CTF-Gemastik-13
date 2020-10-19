FROM ubuntu:20.04

# Open port 5000
EXPOSE 5000

# update
RUN apt-get update -y

# install socat
RUN apt-get install socat -y

# Set WorkDir
RUN mkdir /app
WORKDIR /app

# Copy binary to workdir
COPY flag.txt /app/flag.txt
COPY CDLL /app/CDLL

RUN chown root:root CDLL flag.txt
RUN chmod 755 CDLL flag.txt

# Securing Environment
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls

# Run Program
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./CDLL,su=nobody