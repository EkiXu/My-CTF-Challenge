FROM openjdk:8
WORKDIR /app
COPY "jrasp.jar" /app/jrasp.jar
COPY "springcoffee-0.0.1-SNAPSHOT.jar" /app/springcoffee.jar
COPY flag /flag
COPY readflag /readflag
RUN chmod 0400 /flag
RUN chmod 4555 /readflag

RUN groupadd -r web && useradd -r -g web web

USER web

CMD [ "java","-javaagent:jrasp.jar","-jar","springcoffee.jar" ]