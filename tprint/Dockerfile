FROM php:7.4-fpm-alpine



RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk add --update --no-cache nginx libxml2-dev libpng-dev curl-dev\
    && docker-php-source extract \
    && docker-php-source delete \
    && docker-php-ext-install gd \
    && docker-php-ext-install curl

COPY files /files/ 

RUN mkdir -p /run/nginx \
    && mv /files/nginx.conf /etc/nginx/nginx.conf \
    && mkdir -p /etc/nginx/conf.d \
    && mv /files/default.conf /etc/nginx/conf.d/default.conf

COPY src /var/www/html/

RUN chown -R www-data:www-data /var/www/html \
    && rm -rf /files/* 

COPY ./flag /flag

RUN chmod 0444 /flag

EXPOSE 80

VOLUME ["/var/log/nginx"]

COPY start.sh /start.sh

CMD ["/bin/sh", "/start.sh"]