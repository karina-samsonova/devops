FROM openjdk:17
COPY . .
WORKDIR /app
ENTRYPOINT ["java","Main"]
