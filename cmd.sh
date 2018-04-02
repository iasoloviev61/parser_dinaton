#!/bin/bash
cd dinaton_crawl
scrapy crawl basic -o ./dinaton_crawl/output/product.json
ls -ltr ./output/product.json
