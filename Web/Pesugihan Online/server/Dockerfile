FROM openjdk:8-jdk-alpine
ARG JAR_FILE=chal.jar
COPY ${JAR_FILE} app.jar
RUN apk add bash curl
RUN addgroup -g 82 -S www-data \
&& adduser -u 82 -D -S -G www-data www-data
RUN echo "gemastik13{g3m4st1k_ad4lah_jal4n_h3kelku_1337}" > /fl4g_g3m4st1k_xixixi_h3kelm4n
USER www-data
ENTRYPOINT ["java", "-jar", "/app.jar"]