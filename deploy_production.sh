#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "You need root privileges to run this script." 1>&2
else
    BASE_DIR=/webapps/drife
    ENV_DIR=$BASE_DIR/env
    PROJECT_DIR=$BASE_DIR/drife
    SETTINGS_DIR=$PROJECT_DIR/drife
    MANAGE_SCRIPT=$PROJECT_DIR/manage_production.py
    BRANCH=master

    USER_DIR=$(pwd)

    . $ENV_DIR/bin/activate
    cd $PROJECT_DIR
    git reset --hard HEAD
    git checkout $BRANCH
    git pull origin $BRANCH --rebase
    python $MANAGE_SCRIPT collectstatic
    python $MANAGE_SCRIPT showmigrations

    read -r -p "Do you want to makemigrations? [y/N] " response
    response=${response,,}
    if [[ $response =~ ^(y|yes)$ ]]
    then
        python $MANAGE_SCRIPT migrate
    fi

    pkill gunicorn
    $ENV_DIR/bin/gunicorn -c $SETTINGS_DIR/gunicorn_prod.conf.py drife.wsgi_production &

    cd $USER_DIR
fi
