from datetime import datetime
import pymongo
import pytz

class mongodb:
    def __init__(self, host, DB, Collection):

        # ----------------Start Setup Data Base -------------------------------------------------------------------------------
        self.myclient = pymongo.MongoClient(f"mongodb://{host}/")
        self.dblist = self.myclient.list_database_names()

        if DB in self.dblist:
            print("The Database Exists.")
            self.mydb = self.myclient[DB]
            self.DB = self.mydb[Collection]
        else:
            raise Exception(f"{DB} Database or collection {collection} Does Not Exist")

        self.mydb = self.myclient["UPCDB"]
        self.DB = self.mydb["UPC"]



        # ----------------End Setup Data Base ----------------------------------------------------------------------------------


    def GetTimeStamp(self):
        format = "%Y-%m-%d %H:%M:%S %Z%z"
        timezone = pytz.timezone("America/New_York")
        now = datetime.now()
        time = now.astimezone(timezone)
        return time.strftime(format)
