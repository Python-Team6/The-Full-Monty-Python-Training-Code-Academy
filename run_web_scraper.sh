#!/bin/bash
option="-link"
url="https://igicheva.wordpress.com/all-posts/"

python main.py $option $url
READ=$?
if [ "$READ" -eq "0" ]
then
	export FLASK_APP=scraper_app/web_interface/json_to_html.py
	flask run
else
	echo "Web Scraper error"
fi
