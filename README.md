# flaskblog

Test account : `admin@example.com` / `testroot`

You have to set up environment variables before using the app.

* `SECRET_KEY`: a key to avoid CSRF errors with WTForms. Can be generated with Python's `scerets` module
* `SQLALCHEMY_DATABASE_URI`: a link to your database. I personally used SQLite like in the video tutorials
* `USER_MAIL` and `USER_PWD`: your credentials for your mail address so the app can use the mail feature

To set an environment variable:

**Linux**

```shell script
# Set env variable
export ENVVAR=value

# Check variable
echo $ENVVAR
```

**Windows (CMD)**

```cmd
#Set variable
set VAR_NAME="VALUE"

# Set var permanently for user
setx VAR_NAME "VALUE"

# Set a global variable
setx /M VAR_NAME "VALUE"

#See variable
echo %VAR_NAME%
```

**Windows (Powershell)**

```powershell
#Set variable
$env:VAR_NAME="VALUE"

# Set var permanently for user
setx VAR_NAME "VALUE"

# Set a global variable
setx /M VAR_NAME "VALUE"

#See variable
$env:VAR_NAME
```