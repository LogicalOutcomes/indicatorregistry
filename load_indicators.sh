#!/usr/bin/env bash
workon aristotle-cloud
rm logicaloutcomes/migrations/*
rm site/db.sqlite3
./manage.py makemigrations logicaloutcomes
./manage.py migrate
# python ./loadindicator_sheet.py "logicaloutcomes.settings" "resources/PC-Indicators NKS - June30.xlsx"
python ./loadindicator_sheet2.py "logicaloutcomes.settings" resources/Prosper\ Canada\ Indicator\ import\ sheet\ 2016-10-26.xlsx
