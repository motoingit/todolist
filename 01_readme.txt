python -m pip uninstall virtualenv //for see
python -m pip uninstall virtualenv //for unstall

python -m pip cache info //to see cache
python -m pip cache purge //clear catch


//? pip install virtualenv //installing the virtual

virtualenv env //making an invoirment

this helps to use mulitple verstion of py in one pc vritually without affecting your systym python verstion

//////
if you face error then do run : 
Set-ExecutionPolicy unrestricted
///////


.\env\Scripts\activate.ps1       //for envoirent activation
deactivate                      //to deactivate

pip install flask


////////////////////////////////////all Set

now terminal 1 for pakages
              2  for application run

now create an app.py outside the env
and paste :
/////////////////////////////
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
/////////////////


flask pakage for class of database
/////////////// 
    pip install flask-sqlalchemy
    https://flask-sqlalchemy.readthedocs.io/en/stable/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI
    find here the cjommand - sqlite:///project.db

    AFTER SOME OF THE STEPS OF MIKING THE 

    IF(THIS ERROR)
    onWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead.
. Set it to True or False to suppress this warning.
    THEN DO
///////////////////

now in the class we need date time
pip install datetime



now go to terminal and type to go in compiler inside :

python
from app import db
db.create_all() #dosent work for me but older verstion
 or you can check 01.md
///solution2 is
add this:
@app.cli.command("init-db")
def init_db_command():
    """Clears the existing data and creates new tables."""
    db.create_all()
    print("Initialized the database.")

and


run :
flask init-db
//


//////////////////////4
now jinja2 templating

now adding the app(/show)
and going to /show would print the todo interminal



there are filter in jinja i have explainded in the index,html


jinja inheritence / template inheritence



downloading heroko and herokocli and 
freze our requirements


in vertual
pip install gunicorn
gunicord makes our application runs in mulitple threads

pip freeze > requirements.txt


ctrl shift R removes cachefiles inbrowser

//////////////////////////////////
the down part should not runn inthe vertuaail
adding heroku into the path
C:\Program Files\heroku\bin
restart is must

then type 
heroku
heroku login

{{

    install git
    
PS C:\Users\mohit\OneDrive\Documents\00_CODE\00_05_______FRAME_Work\flask> heroku login 
heroku: Press any key to open up the browser to login or q to exit: 
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/e056d082-00d9-4aef-82a8-fc270f04a1bf?requestor=SFMyNTY.g2gDbQAAAAw0Ny4xNS4xMTUuMTduBgDgUb2OmQFiAAFRgA.n8qLWedfAY6r-s9k40Bp01Yg7JiKy37WL78khK_YYUE
Logging in... done
Logged in as mohitsinghinsecondary@gmail.com

PS C:\Users\mohit\OneDrive\Documents\00_CODE\00_05_______FRAME_Work\flask> git init
PS C:\Users\mohit\OneDrive\Documents\00_CODE\00_05_______FRAME_Work\flask> git add .
PS C:\Users\mohit\OneDrive\Documents\00_CODE\00_05_______FRAME_Work\flask> git commit -m "Initial Commit"
[master (root-commit) b0f7839] Initial Commit
 22 files changed, 846 insertions(+)
 create mode 100644 templates/base.html
 create mode 100644 templates/index.html
 create mode 100644 templates/indexold.html
 create mode 100644 templates/show.html
 create mode 100644 templates/update.html
 create mode 100644 templates/updategpt.html
PS C:\Users\mohit\OneDrive\Documents\00_CODE\00_05_______FRAME_Work\flask> heroku create todo-mohit
Creating ⬢ todo-mohit... !
}}

