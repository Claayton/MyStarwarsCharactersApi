python3 -m venv venv;
source venv/bin/activate;
pip3 install -r requirements.txt;
pre-commit install;
echo "SEARCH_URL=https://swapi.dev/api/people/
CONNECTION_STRING=sqlite:///storage.db
SECRET_KEY=mecontratapiazada123" > .env;
python3 run.py;
