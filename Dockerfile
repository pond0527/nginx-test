FROM openresty/openresty:1.13.6.2-0-centos

ADD conf.d/app.conf /etc/nginx/conf.d/app.conf
ADD ./put.sh /tmp/put.sh
ADD ./validate.py /tmp/validate.py

CMD ["/usr/bin/openresty", "-g", "daemon off;"]
