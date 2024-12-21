FROM wordpress:php8.1-apache

RUN apt update && \
    apt install curl mariadb-client openssl -y

# Install WP-CLI in the toolbox
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar  
RUN chmod +x wp-cli.phar  
RUN mv wp-cli.phar /usr/local/bin/wp-cli

COPY --chown=www-data:www-data challenge-custom/woocommerce-products-filter/ /var/www/html/wp-content/plugins/woocommerce-products-filter/
COPY ./.htaccess /var/www/html/.htaccess
COPY challenge-custom/flag.txt /flag-beluga-is-here.txt
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN chown -R www-data:www-data /var/www/html/

CMD [ "/bin/bash", "/entrypoint.sh" ]  