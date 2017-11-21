### How to run the flask application.

http://flask.pocoo.org/docs/0.12/

```shell
$ . venv/bin/activate
```

Use `flask`

```shell
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```
Use `python -m flask`

```shell
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```

#### Kill port 5000 on Mac

```shell
$ sudo lsof -i:5000
$ kill -9 <PID>
```

