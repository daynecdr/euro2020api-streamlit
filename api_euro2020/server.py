from app import app
from config import PORT
from controllers.fetch import first_page

app.run("0.0.0.0",'8080',debug=True)