import mongodbproductutil as ProductDataBaseUtil
import pprint


productdb = ProductDataBaseUtil.mongodb("192.168.20.176:27017",'UPCDB', 'UPC')


data = productdb.get_product(search='tiffany window', limit='3')

pprint.pprint(data)