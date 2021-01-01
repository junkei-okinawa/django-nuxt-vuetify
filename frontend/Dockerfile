FROM ubuntu:20.04

EXPOSE ${CONTAINER_PORT}
CMD ["bash"]

ENV DEBIAN_FRONTEND=noninteractive

ARG WORKDIR=/frontend/frontend
ARG CONTAINER_PORT=$FRONT_PORT
ARG API_URL=http://project:$APP_PORT

ENV HOME=/${WORKDIR} \
    LANG=C.UTF-8 \
    TZ=Asia/Tokyo \
    HOST=0.0.0.0 \
    API_URL=${API_URL} \
    NPM_CONFIG_PRODUCTION=false

# ENV check
RUN echo ${HOME}
RUN echo ${CONTAINER_PORT}
RUN echo ${API_URL}

# install vim & curl & setting TIMEZONE
RUN apt update && apt-get update && \
    apt install vim -y && \
    apt-get -y --no-install-recommends install curl zsh sudo wget g++ build-essential net-tools && \
    apt-get install --no-install-recommends tzdata && dpkg-reconfigure tzdata && dpkg-reconfigure tzdata && \
    apt-get clean

# install git & pip
RUN printf '6\n79\n' | apt install software-properties-common dirmngr gnupg-agent -y && \
    printf '\n' | add-apt-repository ppa:git-core/ppa && \
    apt update && \
    apt install git -y && \
    rm -rf /var/lib/apt/lists/*

# install nodejs
ENV NODE_VERSION 14.15.1
RUN curl --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" > /tmp/node.tar.xz && \
    tar -xJf /tmp/node.tar.xz -C /usr/local --strip-components=1 && \
    ln -s /usr/local/bin/node /usr/local/bin/nodejs && \
    rm /tmp/node.tar.xz

# install yarn
ENV YARN_VERSION 1.22.5
RUN curl -L --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" > /tmp/yarn.tar.gz && \
    tar -xzf /tmp/yarn.tar.gz -C /opt && \
    ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn && \
    ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg && \
    rm /tmp/yarn.tar.gz

COPY . .

WORKDIR ${HOME}