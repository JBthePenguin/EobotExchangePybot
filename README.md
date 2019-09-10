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
Install all necessary dependencies ([httpx](https://www.encode.io/httpx/)):
``` shell
(env)$ pip install -r requirements.txt
```
## USING
Start application:
```shell
(env)$ python eobot_exchange.py
```
