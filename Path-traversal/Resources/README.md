home/ dans la barre d'adresse 
http://10.12.248.97/index.php?page=../../../../../../../../../../../../etc/passwd

Le site est mal sécurisé car le code PHP ne vérifie pas ce que tu demandes dans l'URL.
On peut acceder aux fichiers en dehors des fichiers du server.

Comment résoudre cela ? 
On doit valider les entrer de l'utilisateur et bannir les caractères spéciaux comme '..'
On peut aussi changer les permissions des fichiers ou travailler en chemin absolu.
