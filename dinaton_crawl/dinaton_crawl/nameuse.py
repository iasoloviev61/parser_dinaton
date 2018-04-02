import csv
with open('./dinaton_crawl/output/product_name.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

your_list = your_list[1:]
list_name = []
for item in your_list:
    item_clean = ''.join(item).split(";")[-1][1:-1]
    list_name.append(item_clean)