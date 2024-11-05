FROM quay.io/centos/centos:stream9

RUN yum -y install httpd mod_wsgi && yum clean all

COPY vhost.conf /etc/httpd/conf.D
COPY myapp.wsgi /var/www/html/myapp.wsgi

VOLUME /var/www/html /var/log/httpd
EXPOSE  80

ENTRYPOINT /usr/sbin/httpd -D FOREGROUND