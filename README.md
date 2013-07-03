Peace Corps Coverdell World Wise Schools matcher
==============================

This is a Django application to link teachers and Peace Corps volunteers through classroom-targetted country-georeferenced blog posting that get tagged and categorized by grade level, home state of volunteer and sector of volunteer.

The early version of the app is live at [peacecorps.herokuapp.com](https://peacecorps.herokuapp.com)

This app was first developed at the ID 2013 Harvard Developers for I. Development hackathon in Cambridge, 

Development was then continued at the Random Hacks of Kindness Boston Hackathon on June 1st and 2nd for the National Day of Civic Hacking.
* Reference site: http://hackforchange.org/challenge/peace-corps-matchmap
* Hackpad: https://hackforchange.hackpad.com/CHALLENGE-Peace-Corps-MatchMap-julyNLxkEGy

To get started:
===============

Set up a virtualenv:

    virtualenv --no-site-packages <PATH_TO_YOUR_VENV>

Activate your virtualenv:

    <PATH_TO_YOUR_VENV>/bin/activate

Install requirements:

    pip install -r requirements.txt

Customize ``settings/localenv.py.sample`` and copy it to ``settings/localenv.py``

Migrate the database:

    python manage.py migrate

Load in sample blog posts:

    python manage.py loaddata fixtures.json

To run the app in production you will need to set an environment variable to 
point django to the production settings module:

    export DJANGO_SETTINGS_MODULE=peacecorps.settings.production

To get started on Mac OS X:
===========================
```sh
virtualenv --no-site-packages your-environment-name # create a virtual environment
source environment/bin/activate # activate your virtual environment
pip install django-taggit # install taggit manually, because problems
pip install -r requirements.txt # install all dependencies
python manage.py syncdb # sync database
python manage.py migrate # migrate the database
python manage.py loaddata fixtures # load sample blog posts into database
python manage.py loaddata tags # load tags into database
python manage.py runserver # run the server
```

Then navigate to localhost:8000.

If you get a braces error, run:

```sh
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
pip install django-braces
```

Then re-run the server

[Team debating a feature]
(https://www.dropbox.com/s/4se43p1wmagflbz/2013-06-04%2020.00.18.jpg)

Happy Peacecorping!
