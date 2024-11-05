FROM quay.io/centos/centos:stream9

RUN yum -yq update && yum -yq install vsftpd && yum clean all
COPY vsftpd.conf.centos9.template /etc/vsftpd/vsftpd.conf

VOLUME /var/ftp/pub
COPY WelcomeToMYFTPServer.txt /var/ftp/pub/WelcomeToMYFTPServer

EXPOSE 21 20

ENTRYPOINT /usr/sbin/vsftpd

