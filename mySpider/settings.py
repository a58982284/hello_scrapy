# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'mySpider.pipelines.SomePipeline': 300,
    "mySpider.pipelines.ItcastPipeline":300,
}