FROM centos:6
MAINTAINER "Mike Buzzetti" <michael.buzetti@nytimes.com>
ENV container docker

ADD bin/rabbitmq-start /usr/local/bin/
COPY config /rabbit/config

RUN yum install -y https://www.rabbitmq.com/releases/erlang/erlang-18.2-1.el6.x86_64.rpm && \
    yum install -y https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.0/rabbitmq-server-3.6.0-1.noarch.rpm  && \ 
    yum install -y wget && \
    wget http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_auth_backend_http-3.6.x-3dfe5950.ez -O /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.0/plugins/rabbitmq_auth_backend_http-3.6.x-3dfe5950.ez && \
    rabbitmq-plugins enable rabbitmq_auth_backend_http && \
    rabbitmq-plugins enable rabbitmq_management && \
    rabbitmq-plugins enable rabbitmq_mqtt && \
    rabbitmq-plugins enable rabbitmq_federation && \
    rabbitmq-plugins enable rabbitmq_federation_management

RUN echo "ERLANGCOOKIE" > /var/lib/rabbitmq/.erlang.cookie
RUN chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie
RUN chmod 400 /var/lib/rabbitmq/.erlang.cookie

VOLUME ["/rabbit/config", "/rabbit/data/", "/rabbit/log"]
EXPOSE 15672 5672 1883 4369 
WORKDIR /rabbit/data

ENV RABBITMQ_MNESIA_BASE /rabbit/data/mnesia
ENV RABBITMQ_CONFIG_FILE /rabbit/config/rabbitmq
CMD /usr/local/bin/rabbitmq-start

