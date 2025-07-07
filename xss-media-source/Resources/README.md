cliquer sur le logo nsa

## Comment ?

On change nsa par :
src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGFja2VkIik8L3NjcmlwdD4=

En base64 cela équivaut a ```<script>alert("hacked")</script>```.  
On précise que c'est de type html en base64 et cela exécute la balise script.

## Comment éviter cela ? 
- En validant dans le back. On peut limiter les types des paramètre passer dans URL. 
- On peut bloquer l'exécution des scripts.

