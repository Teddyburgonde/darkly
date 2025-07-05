home/ leave feedback


C’est une faille car le site réaffiche directement ce que tu tapes sans le vérifier, ce qui permet d’y injecter du code.
C’est une XSS (Cross-Site Scripting) parce que tu peux y mettre du JavaScript malveillant qui s’exécutera dans le navigateur.

On a tapé 'error'.

Comment l'éviter ?

- Valider les entrées utilisateurs.
- Bloquer les caracteres comme les <>
