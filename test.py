import csv
import json
with open('./dinaton_crawl/output/name_model.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

your_list = your_list[1:]
list_name = []
list_model = []
for item in your_list:
    item_clean = ''.join(item).split(";")[-2][1:-1]
    list_name.append(item_clean)


for model_item in your_list:
    model_clean = ''.join(model_item).split(";")[-1]
    try:
        list_model.append(int(model_clean))
    except ValueError:
        pass

print(min(list_model))

# json_data=open('./dinaton_crawl/output/product.json').read()
# products_all = json.loads(json_data)
# products_filter = []
# # print(products_all[0], list_name[0])
# for product_item in range(len(products_all)):
#     for product_name in list_name:
#         if  product_name == products_all[product_item]['_NAME_']:
#             print('drop duplicate')
#         else:
#             products_filter.append(products_all[product_item])
# # print(len(products_filter))
# print(products_filter[10])


