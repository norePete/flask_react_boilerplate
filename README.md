### install dependencies from boilerplate/
npm i

### build static files from boilerplate/
npm run build

### enter python virtual env from ./
source flask/bin/activate

### start flask server from ./
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app

