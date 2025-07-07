f12 -> cookies

## Comment ?
On a vu un cookie qui s'appelle 'i_am_admin' avec une valeur md5 qui signifie 'false'. On a donc remplacere sa valeur par 'true' en md5.

## Comment l'éviter ? 
- Utiliser sha256 au lieu de md5.
- Verifier les privilèges de l'utilisateur en back et non pas avec un cookie seul (ne jamais faire confiance à ce qui vient du front).

