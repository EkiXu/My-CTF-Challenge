#!/bin/sh

php-fpm &

nginx &

tail -F /var/log/nginx/error.log /var/log/nginx/access.log
