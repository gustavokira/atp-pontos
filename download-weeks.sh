URL=http://www.atpworldtour.com/en/rankings/singles
wget -qO- $URL > der.html
python parser-week.py < der.html > week-all.csv
rm der.html
