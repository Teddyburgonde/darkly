home/sign in/i forgot my password

## Comment ?

On voit :
```html
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
<input type="submit" name="Submit" value= "Submit">
```

On a remplacé "value" par une autre adresse mail.

## Comment l'éviter ?

Définir l'adresse e-mail côté serveur afin qu'elle ne puisse pas être modifiée par l'utilisateur.
Ne pas faire confiance à ce qui vient du front. 


