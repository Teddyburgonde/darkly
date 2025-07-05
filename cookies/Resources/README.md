f12 
cookies
On a vu un cookie qui s'appelle 'i_am_admin' avec une valeur md5 qui signifie 'false' et donc on a mis 'true' en md5 à la place.

Comment l'éviter ? 
- Verifier les privilères de l'utilisateur en back et non pas dans le cookie.
- Utiliser sha256 au lieu de md5.
