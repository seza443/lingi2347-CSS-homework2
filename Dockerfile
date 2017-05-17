FROM ubuntu:16.04

# Install Apache2
RUN apt-get update && apt-get -y install \
    apache2 \
    && apt-get clean

# Authorize CGI
RUN  a2enmod cgi

# Copy and chmod +x CGI scripts
COPY ./cgi-scripts/ /usr/lib/cgi-bin/
RUN chmod +x /usr/lib/cgi-bin/test.cgi

# Copy website
COPY ./secu.com/ /var/www/html/

# Command to run
CMD /usr/sbin/apache2ctl -D FOREGROUND
