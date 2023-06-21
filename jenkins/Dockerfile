FROM jenkins/jenkins:lts
ARG DOCKER_GID
USER root
RUN apt-get update && \
    apt-get install -y curl vim build-essential libssl-dev libpcre3 libpcre3-dev libxml-parser-perl expat libexpat1-dev unzip xvfb maven 
ENV DOCKERVERSION=18.03.1-ce
ENV DOCKERCOMPOSEVERSION=1.23.2
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz && \
    tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 -C /usr/local/bin docker/docker && \
    rm docker-${DOCKERVERSION}.tgz 
RUN touch /var/run/docker.sock && \
    chown jenkins /var/run/docker.sock
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKERCOMPOSEVERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
RUN groupadd -g ${DOCKER_GID:-999} docker && gpasswd -a jenkins docker