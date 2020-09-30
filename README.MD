Parser file. It Drop db ,if db exist. After create db and parsing csv to db:
    
    cd parsing
    
    python parser.py 

test_put_request.py makes a test put request to api and create 1 row in table Reviews:

    python test_put_request.py

    

to run the application you need to run :
    
    export FLASK_APP=app.py
    
    flask run


all required libraries in the requirements.txt
