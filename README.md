# Eobot Exchange Pybot
A bot that makes exchanges on [Eobot API](https://www.eobot.com/developers).
## INSTALLATION
### Application, virtual environment, requirements
> :exclamation:maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/)
Clone the folder, go inside, create a virtual environment for Python with virtualenv and activate it:
```shell
$ git clone https://github.com/JBthePenguin/EobotExchangePybot.git
$ cd EobotExchangePybot
$ virtualenv -p python3 env
$ source env/bin/activate
```
Install all necessary dependencies ([eobot-py](https://github.com/rickdenhaan/eobot-py)):
``` shell
(env)$ pip install -r requirements.txt
```
### Settings
In *config/config.py*, write your eobot user id, the email that register on eobot and the API Key (you can found it in your profile page on eobot website):
``` python
USER_ID = 1234567  # Your eobot user id
EMAIL = "youremail@example.com"  # Your email
PASSWORD = "aa11aa11aa11aa11aa11"  # Your API Key
```
## USING
Start application:
```shell
(env)$ python eobot_exchange.py
```
