```
scrapy startproject movie_cms

scrapy crawl movie -t json -o - > ../items.json
```