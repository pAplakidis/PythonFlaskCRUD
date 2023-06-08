#Python Flask CRUD Application Test Assignment

##Requirements
- Flask
- Flask-SQLAlchemy
- sqlite3

##Run (Linux/Unix)

In a python shell:
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

