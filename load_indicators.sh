#!/usr/bin/env bash
source ~/.virtualenvs/aristotle-cloud/bin/activate
rm logicaloutcomes/migrations/*
rm site/db.sqlite3
./manage.py makemigrations logicaloutcomes
./manage.py migrate
# python ./loadindicator_sheet.py "logicaloutcomes.settings" "resources/PC-Indicators NKS - June30.xlsx"
python ./loadindicator_sheet.py "logicaloutcomes.settings" "resources/ARISTOTLE-indicatorSPREADSHEET - MASTER - July182016.xlsx"
