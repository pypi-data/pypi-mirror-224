import pprint

import mongodbproductutil as ProductDataBaseUtil
productdb = ProductDataBaseUtil.mongodb("192.168.20.176:27017",'UPCDB', 'UPC')




pprint.pprint(productdb.get_product(upc='011217993511'))