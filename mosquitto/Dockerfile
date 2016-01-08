FROM centos:6
MAINTAINER "Mike Buzzetti" <michael.buzetti@nytimes.com>
ENV container docker

ADD mqtt.repo /etc/yum.repos.d/mqtt.repo
RUN yum install -y mosquitto

ADD bin/mosquitto-start /usr/local/bin/

COPY config /mosquitto/config
VOLUME ["/mosquitto/data", "/mosquitto/log"]
EXPOSE 1883 9001

CMD /usr/local/bin/mosquitto-start 
