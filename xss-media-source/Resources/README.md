cliquer sur le logo nsa

je change nsa par :
src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGFja2VkIik8L3NjcmlwdD4=

En base64 cela équivaut a alert("hacked")
Et je lui dis que c'est de type html et cela exécute la balise script.

Comment éviter cela ? 
En validant dans le back on peut limiter les types des paramètre passer dans URL. 
On peut aussi bloquer l'exécution des scripts. Comment résoudre cela ? 
On doit valider les entrer de l'utilisateur et bannir les caractères spéciaux comme '..'
On peut aussi changer les permissions des fichiers ou travailler en chemin absolu.

