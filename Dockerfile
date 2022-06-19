FROM java:8
ADD Main.java .
RUN javac Main.java
CMD ["java", "Main"]
