aller sur robots.txt

il y a deux chemins disallow :
whatever
celui nous donne le fichier htpasswd
Dedans il y a un code en md5
En le decryptant on obtient le mot passe de root.
On se connecte via la page /admin
username root
password qwerty123@

Comment l'éviter ?
- Dans le robots.txt on peut disallow tout et allow seulement les pages accessibles à un utilisateur lambda.
