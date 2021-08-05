---
template:
slug: flask-jwt-login
title: Flask-JWT-Extended × Flask-Login
subtitle: Apparently I do webshit now
date: 2020-06-24
---

For the past few months, I've been working on building a backend for
`$STARTUP`, with a bunch of friends. I'll probably write in detail about
it when we launch our beta. The backend is your bog standard REST API,
built on Flask -- if you didn't guess from the title already.

Our existing codebase heavily relies on
[Flask-Login](https://flask-login.readthedocs.io); it offers some pretty
neat interfaces for dealing with users and their states. However, its
default mode of operation -- sessions -- don't really fit into a Flask
app that's really just an API. It's not optimal. Besides, this is what
[JWTs](https://jwt.io) were built for. 

I won't bother delving deep into JSON web tokens, but the general
flow is like so:

- client logs in via say `/login`
- a unique token is sent in the response
- each subsequent request authenticated request is sent with the token

The neat thing about tokens is you can store stuff in them -- "claims",
as they're called.

## returning an `access_token` to the client

The `access_token` is sent to the client upon login. The idea is simple,
perform your usual checks (username / password etc.) and login the user
via `flask_login.login_user`. Generate an access token using
`flask_jwt_extended.create_access_token`, store your user identity in it
(and other claims) and return it to the user in your `200` response.

Here's the excerpt from our codebase.

```python
access_token = create_access_token(identity=email)
login_user(user, remember=request.json["remember"])
return good("Logged in successfully!", access_token=access_token)
```

But, for `login_user` to work, we need to setup a custom user loader to
pull out the identity from the request and return the user object.

## defining a custom user loader in Flask-Login

By default, Flask-Login handles user loading via the `user_loader`
decorator, which should return a user object. However, since we want to
pull a user object from the incoming request (the token contains it),
we'll have to write a custom user loader via the `request_loader`
decorator.


```python
# Checks the 'Authorization' header by default.
app.config["JWT_TOKEN_LOCATION"] = ["json"]

# Defaults to 'identity', but the spec prefers 'sub'.
app.config["JWT_IDENTITY_CLAIM"] = "sub"

@login.request_loader
def load_person_from_request(request):
    try:
        token = request.json["access_token"]
    except Exception:
        return None
    data = decode_token(token)
    # this can be your 'User' class
    person = PersonSignup.query.filter_by(email=data["sub"]).first()
    if person:
        return person
    return None
```


There's just one mildly annoying thing to deal with, though.
Flask-Login insists on setting a session cookie. We will have to disable
this behaviour ourselves. And the best part? There's no documentation
for this -- well there is, but it's incomplete and points to deprecated
functions.

## disabling Flask-Login's session cookie

To do this, we define a custom session interface, like so:

```python
from flask.sessions import SecureCookieSessionInterface
from flask import g
from flask_login import user_loaded_from_request

@user_loaded_from_request.connect
def user_loaded_from_request(app, user=None):
    g.login_via_request = True


class CustomSessionInterface(SecureCookieSessionInterface):
    def should_set_cookie(self, *args, **kwargs):
        return False

    def save_session(self, *args, **kwargs):
        if g.get("login_via_request"):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)


app.session_interface = CustomSessionInterface()
```

In essence, this checks the global store `g` for `login_via_request` and
and doesn't set a cookie in that case. I've submitted a PR upstream for
this to be included in the docs
([#514](https://github.com/maxcountryman/flask-login/pull/514)).
