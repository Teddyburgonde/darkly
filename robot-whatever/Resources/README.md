/robots.txt

## Comment ?
Il y a deux chemins "disallow" :
whatever
.hidden

Ici on utilise whatever  
On trouve dans celui-ci le fichier htpasswd.  
Dedans il y a le mot de passe root en md5.  
En le decryptant on obtient qwerty123@.  
On se connecte via la page /admin.

**username** root  
**password** qwerty123@

## Comment l'éviter ?
- Dans le robots.txt on peut disallow tout et allow seulement les pages accessibles à un utilisateur lambda.
