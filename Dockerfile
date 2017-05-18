FROM ubuntu:16.04
LABEL maintainer "Alexandre Hauet & Tanguy Vaessen"

# Install Apache2
RUN apt-get update && apt-get -y install \
    apache2 \
    postgresql-client \
    && apt-get clean

# Authorize CGI
RUN  a2enmod cgi

# Copy and chmod +x CGI scripts
COPY ./cgi-scripts/ /usr/lib/cgi-bin/
RUN chmod +x /usr/lib/cgi-bin/login.cgi
RUN chmod +x /usr/lib/cgi-bin/root.cgi


# Copy website
COPY ./secu.com/ /var/www/html/

ENV PGPASSWORD mysecretpassword

# Command to run Apache
CMD /usr/sbin/apache2ctl -D FOREGROUND
