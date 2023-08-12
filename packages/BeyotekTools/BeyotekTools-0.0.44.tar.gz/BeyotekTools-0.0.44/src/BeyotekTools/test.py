import mongodbproductutil as ProductDataBaseUtil
import pprint


productdb = ProductDataBaseUtil.mongodb("192.168.20.176:27017",'UPCDB', 'UPC')


data = productdb.get_product('011661059825', limit=3)

pprint.pprint(data)