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


    def get_time_stamp(self):
        format = "%Y-%m-%d %H:%M:%S %Z%z"
        timezone = pytz.timezone("America/New_York")
        now = datetime.now()
        time = now.astimezone(timezone)
        return time.strftime(format)

    def add_proxy_to_db(self,proxy):
        self.DB.update(proxy)