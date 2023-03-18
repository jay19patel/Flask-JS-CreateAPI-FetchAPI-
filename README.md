# Flask-JS-CreateAPI-FetchAPI-

# create API Using Flak and Mongo Db
# fetch apis using fetch api Java script

# crud Using Fetch api 

# baisc notes 
________________________________________________
- create venv 
- pip install flask

- import flask 
- set flask in  variabe  app
    app = Flask(__name__)

- create route for navigae urls 
    @app.route('/')

- create function for logic and page rendering 
    def hellow():
        return 'hellow'

- run the site :
    if __name__ =='__main__':
        app.run(debug=True)

        debug means if have any error than degub true is for display error in brouser 

- if you need render html page then import render_template from flask
 - add the render in rentern and add file path using static 
    ex:
    @app.route('/')
    def hellow():
        return render_template('index.html')

- create own html page (like bootstrap to do list )

----create model in flask(database tables)-----
- create connecttion with data base:
    ```
    install pymongo
        pip install Flask pymongo
        import : from pymongo import MongoClient
        

- client= MongoClient('localhost', 27017)
- create document :
    db = client.FileName # create table
    dbdata = db.Collectioname # triger

        
        

