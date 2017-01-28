while IFS= read -r line; do
  URL=http://www.atpworldtour.com/en/rankings/singles?rankDate=$line
  wget -qO- $URL > $line.html
  python parser-points.py < $line.html > csv/$line.csv
  rm $line.html
done
