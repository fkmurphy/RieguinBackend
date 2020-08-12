#!/bin/sh

pip3 install -r requirements.txt

python3 manage.py runserver 0.0.0.0:8000
