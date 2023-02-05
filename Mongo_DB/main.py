from Mongo_DB.collections.shoes_collection import ShoesCollection

shoes = ShoesCollection()
# shoes.insert_shoes(brand='Nike', model="Space Hippie", price=160)
# shoes_list = [{'brand': 'New Balance', 'model': '1500', 'price': 190},
#               {'brand': 'Adidas', 'model': 'NMD R1', 'price': 210},
#               {'brand': 'Asics', 'model': 'Gel Lyte V', 'price': 175},
#               {'brand': 'Nike', 'model': 'Jordan XI', 'price': 240}]
# shoes.insert_many_shoes(shoes_list)
# shoes.update(condition={'model': 'Air Force 1'}, set_value={"price": 155})
# print(shoes.find_first_by('brand', 'Nike'))
# shoes.delete_one_by('price', 240)
results = shoes.get_all_shoes()
for result in results:
    print(result)
