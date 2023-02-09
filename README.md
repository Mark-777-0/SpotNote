# SpotNote
<a href='https://spotnote.herokuapp.com/' rel='noreferrer' target='_blank' >


<img src="https://raw.githubusercontent.com/Mark-777-0/SpotNote/2c51bfff79976f31fa7f4239d8159b16a6b77013/app/static/SpotNote.svg" alt="SpotNote" width="700"/>
</a>


## Heroku has eliminated free plans and the site is no longer hosted

# Technical/Reflection

SpotNote is a social media site for musicians hosted on Heroku. The framework used for the app was Flask, and SQLAlchemy for the database. 

I have organized the code using prettier formatting

I learned quite a lot about Flask Routes, CSRF, and SQLite while putting this project together. Also learned about proper python Venv usage, making Flask applications scalable via templates (passing in props instead of hard coding every page), inheritance of templates, 

### Future and Things to Improve

The websites elastic search function does not work yet, as Heroku wants me to put a credit card on file, but I did not want to do that.

You cannot upload pictures or sound bytes yet, so some of the functionality is still lacking. Also hyperlinks are not yet allowed, so it's like a lite version of Twitter/Reddit.

There is no delete posts button, or login e-mail verification so moderation is poor.




# Run It Yourself

`git clone`  the repository

## Make a Virtual Environment

`python3 -m venv venv`

`source venv/bin/activate` move your shell into it

## Install Dependencies

`pip install` all of these dependencies!

`flask, flask-sqlalchemy, flask-migrate, flask_login, flask_mail, flask_bootstrap, flask_moment, flask_babel, elasticsearch, redis, rq` if you get an import error that other files are missing just   pip install them as well!

## Initialize the DataBase

`flask db init` in the terminal

`flask db migrate -m 'migration message'`

`flask db upgrade`
