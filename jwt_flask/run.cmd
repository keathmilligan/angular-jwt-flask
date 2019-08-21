@echo off
set FLASK_APP=jwtapp
set FLASK_DEBUG=1
python -m flask run --reload --debugger --with-threads
