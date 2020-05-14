#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv



fileloader = {
    "dialogflow":{
        'filename': 'credential_key.json',
        'name': "GOOGLE_APPLICATION_CREDENTIALS"
    },
    "env":{
        'filename': 'localhost.env',
        'name':"env"
    }
}

# for loading all necessary configuration files
def loadFiles(params):
    FILE_NAME = params['filename']
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, FILE_NAME)
    os.environ[params['name']] = path

loadFiles(fileloader['dialogflow'])
loadFiles(fileloader['env'])
load_dotenv(os.environ['env'])


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
