FROM python:3.5
RUN pip install Scrapy transliterate Pillow
WORKDIR /dinaton_crawl
COPY dinaton_crawl /dinaton_crawl
COPY cmd.sh /
CMD ["/cmd.sh"]