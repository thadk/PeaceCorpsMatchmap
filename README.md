Peace Corps Coverdell World Wise Schools matcher
==============================

This is a Django application to link teachers and Peace Corps volunteers through classroom-targetted country-georeferenced blog posting that get tagged and categorized by grade level, home state of volunteer and sector of volunteer.

It uses the Zinnia weblog framework for Django and Mapbox for the tile service.

This app was first developed at the ID 2013 Harvard Developers for I. Development hackathon in Cambridge, MA


To get started:
===============

Set up a virtualenv:

    virtualenv --no-site-packages <PATH_TO_YOUR_VENV>

Activate your virtualenv:

    <PATH_TO_YOUR_VENV>/bin/activate

Install requirements:

    pip install -r requirements.txt

Customize ``settings/localenv.py.sample`` and copy it to ``settings/localenv.py``

To run the app in production you will need to set an environment variable to 
point django to the production settings module:

    export DJANGO_SETTINGS_MODULE=peacecorps.settings.production

Happy Peacecorping!