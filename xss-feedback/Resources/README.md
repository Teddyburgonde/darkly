home/ leave feedback


## Comment ?

C’est une faille car le site réaffiche directement ce qu'on tape sans le vérifier, ce qui permet d’y injecter du code.
C’est une XSS (Cross-Site Scripting) car on peut y mettre du JavaScript malveillant qui s’exécutera dans le navigateur.

On a tapé 'error'. Cela suffit car l'exercice est mal codé. On pense qu'il cherche à matcher une balise ```<script>```.

## Comment l'éviter ?

- Valider les entrées utilisateur.
- Bloquer les caractères spéciaux comme les <>
