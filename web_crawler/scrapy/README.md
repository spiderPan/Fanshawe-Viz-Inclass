# Install dependencies
```
pip3 install -r requirements.txt
```

# Common CLs

### Init a new project
```
scrapy startproject movies_cms
```

### Run Spider for the project `movies_cms`
```
cd movies_cms
scrapy crawl movie -t json -o - > items.json 
```