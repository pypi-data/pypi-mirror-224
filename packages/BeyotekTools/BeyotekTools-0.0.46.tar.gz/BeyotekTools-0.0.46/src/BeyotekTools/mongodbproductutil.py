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
            data = self.get_product_by_upc(upc, limit)
            return data

        elif search:
            data = self.get_product_by_title_search(search, limit)
            return data

        else:
            return 'Please Specify "upc", or "search" parameters'

    def get_product_by_upc(self, upc, limit):
        data = []
        if not limit:
            limit = 1

        response = self.DB.find({'$text': {'$search': f'{upc}'}}, {'Response': 0, '_id': 0}).sort("timestamp",-1).limit(int(limit))

        for info in response:
            data.append(info)

        return data

    def get_product_by_title_search(self, search, limit):

        response = self.DB.find({'$text': {'$search': f'/{search}/'}}, {'Response': 0, '_id': 0,'score': { '$meta': "textScore" }}).sort("timestamp",-1)

        # -----------------Start Filter results to only one of each upc---------------------
        list_upc_already_seen = []
        list_documents = []
        for doc in response:
            upc = doc.get("upc")
            if upc not in list_upc_already_seen:
                list_documents.append(doc)
                list_upc_already_seen.append(upc)
        # -----------------End Filter results to only one of each upc---------------------

        # ----------------Start Format Data To Be Returned---------------------------
        list_documents.sort(reverse=True, key=self.productsearchkey)  # sort results by best search score
        if limit:
            limited_documents = list_documents[slice(int(limit))]
        else:
            limited_documents = list_documents

        # ----------------End Format Data To Be Returned----------------------------

        return limited_documents


    def productsearchkey(e,f):
        return f.get("score")
        #return e.get('score')