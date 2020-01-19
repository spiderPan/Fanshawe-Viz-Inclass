
# Init the project
```
scrapy startproject movies_cms
```

# Run Spider
```
cd movies_cms
scrapy crawl movie -o items.json -t json
```