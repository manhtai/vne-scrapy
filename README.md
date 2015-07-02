VnExpress crawler
=================


## Items

[vnexpress.items.VnexpressItem](vnexpress/items.py)


## Spider

[sohoa](vnexpress/spiders/sohoa.py)

- Request content directly, then
- Send GET requests to get comments from another server


## Pipelines

- Requiring certain item fields
- Convert lists to strings for saving to MySQL
- Saving items to MySQL (You have create a table first)


## Alternatives

- To get AJAX content: Selenium+PhantomJS, Splash+ScrapyJS
- To save data: MongoDB, ElasticSearch

