Exploit:

```html
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
<input type="submit" name="Submit" value= "Submit">
```
J'ai remplacé la value par mon adresse mail.

Comment éviter cela ?

```c
Valider côté serveur que l'adresse e-mail ne peut pas être modifiée par l'utilisateur.
```
