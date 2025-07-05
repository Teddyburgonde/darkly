
home/ Cliquer sur le : 
© BornToSec (celui avec le son et albatros)
Commentaires trouvés dans l'inspect.

You must come from : "https://www.nsa.gov/" to go to the next step

Let's use this browser : "ft_bornToSec". It will help you a lot.

"Tu dois venir du site de la NSA et utiliser un navigateur spécial."

Du coup, on fait croire au site qu’on vient de là et qu’on a ce navigateur.


curl "http://10.12.248.97/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" \
  -H "Referer: https://www.nsa.gov/" \
  -H "User-Agent: ft_bornToSec" | grep -i "flag"
  
  
 Comment l'éviter ? 
 -Ne pas faire confiance au header http.
