# flask_application

# running the ui on python server
python -m http.server 8008
this will run the html and css code in 127.0.0.1:8008 port
# flask application run
python app.py (in cmd) 
# migrations 
python app.py db init (for creating the migrations folder) or flask db init

# migrations changes
python app.py migrate -m "message"

# applying the changes
python app.py upgrade 


