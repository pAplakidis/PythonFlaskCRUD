# Python Flask CRUD Application Test Assignment

## Requirements
- Flask
- Flask-SQLAlchemy
- sqlite3

```
pip install Flask
pip install Flask-SQLAlchemy
sudo apt install sqlite3
```

## Run (Linux/Unix)

In a python shell (if there is not database present in src/instance/):
```python
>>> from app import *
>>> with app.app_context():
...     db.create_all()

```

In a terminal:
```
cd src
chmod +x app.py
./app.py
```

