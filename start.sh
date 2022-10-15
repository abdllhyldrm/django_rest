#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py makemigrations
python blog/manage.py runserver --host 0.0.0.0