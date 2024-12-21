#!/bin/bash

cd /var/www/html/

echo "Waiting for db to ready :)"
sleep 15

wp-cli --allow-root core download --path=/var/www/html/ 

echo "⚙️ Configuring Wordpress database..."
dockerize -wait tcp://once_0_day_db:3306 -timeout 180s 2> /dev/null #2>&1
rm -f wp-config.php

wp-cli --allow-root wp config create

wp-cli --allow-root core config \
    --dbhost=${WORDPRESS_DB_HOST} \
    --dbname=${WORDPRESS_DB_NAME} \
    --dbuser=${WORDPRESS_DB_USER} \
    --dbpass=${WORDPRESS_DB_PASSWORD} \
    --locale=${WORDPRESS_LOCALE}


wp-cli --allow-root core install \
    --url="${CHALL_SERVER_IP}:${CHALL_SERVER_PORT}" \
    --title="${WORDPRESS_WEBSITE_TITLE}" \
    --admin_user=${WORDPRESS_ADMIN_USER} \
    --admin_password=${WORDPRESS_ADMIN_PASSWORD} \
    --admin_email=${WORDPRESS_ADMIN_EMAIL}

wp-cli --allow-root option update siteurl "http://${CHALL_SERVER_IP}:${CHALL_SERVER_PORT}"
wp-cli --allow-root rewrite structure ${WORDPRESS_WEBSITE_POST_URL_STRUCTURE}
wp-cli --allow-root option update users_can_register 1
wp-cli --allow-root plugin install woocommerce --activate
wp-cli --allow-root plugin activate woocommerce-products-filter
wp-cli --allow-root plugin install mstore-api --version="4.15.3" --activate

chown -R www-data:www-data /var/www/html

a2enmod rewrite
service apache2 start
sleep infinity
