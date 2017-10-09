import pymongo as Mongo

DB_NAME = 'localhost'
DB_PORT = 27017


TEST_JSON = {'url':'http://hello.com','content':'Lemon Tree'}

class DB():

    def __init__(self,db,port):
        self.client = Mongo.MongoClient(db,port)
        self.db = self.client.test
        self.collect = self.db.test_collect

    def insert(self,c):
        self.collect.insert_one(c)

    def find(self,k):
        return self.collect.find(k)

    def delete(self,k):
        return self.collect.delete_many(k)

    def close(self):
        self.client.close()


if __name__ == '__main__':
    # Client = Mongo.MongoClient(DB,PORT)
    # db = Client.test
    # collect = db.test_collect
    # collect.insert(TEST_JSON)
    # for x in collect.find({'content':'Lemon Tree'}):
    #     print x
    # Client.close()
    print 'mongodb test start:'
    db = DB(DB_NAME,DB_PORT)
    db.insert(TEST_JSON)
    result = db.find({'content':'Lemon Tree'})
    for x in result:
        print x
    db.delete({'content':'Lemon Tree'})
    db.close()
    print 'mongodb test complete!'
