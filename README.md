# Django Projectt

A Django Oauth2 authentication server 

## Run Project

First, activate the virtual enviroment. At root directory run
```
source venv/bin/activate
```

Go to ```src/``` directory and run

```
python3 manege.py runserver
```

## Requests
Now you can perform requests for user and for unicorn. There are three types of user requests, to register(```register```), to login(```token```), to regresh(```refresh_token```) and to logout(```revoke_token```). All types are describe above using ```curl```tool.

### Register request

```
curl -d "username=<username>&password=<password" "local:8000/authentication/register/"
```
The respose will be like

```
{
    "access_token":"<token>",
    "expires_in":36000,
    "token_type":"Bearer",
    "scope":"read write",
    "refresh_token":"<refresh_token>"
}
```


### Login request

```
curl -d "username=<username>&password=<password" "localhost:8000/authentication/token/"
```

The response will be the same as the register response

### Refresh request

```
curl -d "refresh_token=<refresh_token>" "localhost:8000/authentication/token/refresh/"
```

The response will be the same as the register response

### Logout request

```
curl -d "token=<token>" "localhost:8000/authentication/token/revoke/"
```

The response will be

```
{message: 'token revoked'}
```

The last one will be about unicorn

### Crete unicorn request

```
curl -H "Authorization: Bearer <token>" -d "name=<name>&age=<age>" 0.0.0.0:8000/v1/unicorn/
```

The response will be like
``` 
{
    name: "<name>",
    age: "<age>"
}
```
