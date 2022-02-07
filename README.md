CHECK HERE FOR EXPLANATION OF RECOMMITTING CHAPTERS 3-6:

For these chapters, I was using the wrong Django version (4.0.2), so the code would break when tested in the correct version of 2.2.26. To rectify this, one line of code had to be changed (in settings.py), changing: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

to:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

Which made the code, and by extension tests, work. Hence all of the rapid recommits. :D