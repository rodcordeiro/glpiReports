# GlpiReports

## `GET` /initSession
Initialize a new session providing a session token to use the API.

## __Parameters__


`app_token` The app token provided by GLPI

`login` The username to creates the session

`password` The user password to creates the session. It must be URLEncoded if your not using a Lib.

```sh
curl --request GET \
  --url 'http://192.168.3.28/glpi/apirest.php/initSession?app_token=APP_TOKEN&login=USERNAME&password=PASSWORD'
```
---

## `GET` /killSession
 Destroy the session with the session_token provided
## __Parameters__
`app_token` The app token provided by GLPI

`session_token` The session token

`password` The user password to creates the session. It must be URLEncoded if your not using a Lib.

```sh
curl --request GET \
  --url 'http://192.168.3.28/glpi/apirest.php/killSession?app_token=APP_TOKEN&session_token=SESSION_TOKEN'
```
---

[Documentação GLPI](http://glpi.beltis.com.br/glpi/apirest.php/)
