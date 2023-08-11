from datetime import datetime
import pymongo
import pytz


class mongodb:
    def __init__(self, host, DB, collection):

        # ----------------Start Setup Data Base -------------------------------------------------------------------------------
        self.myclient = pymongo.MongoClient(f"mongodb://{host}/")
        self.dblist = self.myclient.list_database_names()

        if DB in self.dblist:
            print("The Database Exists.")
            self.mydb = self.myclient[DB]
            self.DB = self.mydb[collection]
        else:
            raise Exception(f"{DB} Database or collection {collection} Does Not Exist")

        # ----------------End Setup Data Base ----------------------------------------------------------------------------------

    def UpdateProduct(self, upc, name, available, price, url, timestamp, response):
        try:
            dict = {
                "upc": upc, "name": name, "saleprice": price, "available": available, "timestamp": timestamp,
                "vendor_url": url, "Response": response
            }
            x = self.DB.insert_one(dict)

            print(f"Added UPC: {upc} to database")
        except Exception as e:
            print(f"Update Product Error: {e} UPC: {upc}")

    def GetTimeStamp(self):
        format = "%Y-%m-%d %H:%M:%S %Z%z"
        timezone = pytz.timezone("America/New_York")
        now = datetime.now()
        time = now.astimezone(timezone)
        return time.strftime(format)

    def get_product(self, upc=None, limit=None, search=None):



        if upc:
            if not limit:
                limit = 1
            data = self.get_product_by_upc(upc,limit)
            return data

        if search:
            data = self.get_product_by_title_search(search, limit)
            return data


    def get_product_by_upc(self, upc, limit):
        data = []
        if not limit:
            limit=1

        response = self.DB.find({ "upc": upc }, {'Response':0,'_id':0}).sort("timestamp", -1).limit(int(limit))
        for info in response:
            data.append(info)

        return data

    def get_product_by_title_search(self, search, limit):
        data = []
        if not limit:
            response = self.DB.find({'$text': {'$search': f'/{search}/'}}, {'Response': 0, '_id': 0}).sort("timestamp", -1)
        else:
            response = self.DB.find({'$text': {'$search': f'/{search}/'}}, {'Response': 0, '_id': 0}).sort("timestamp", -1).limit(int(limit))

        for info in response:
            data.append(info)

        return data