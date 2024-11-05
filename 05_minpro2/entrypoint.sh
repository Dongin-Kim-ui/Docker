#!/bin/bash

mkdir /run/php-fpm
/usr/sbin/php-fpm

/usr/sbin/httpd -D FOREGROUND