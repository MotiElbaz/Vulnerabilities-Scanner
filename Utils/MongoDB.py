import pymongo
import Utils.CVE_Data as cve_data


def connect_mongodb(ip, port):
    return pymongo.MongoClient(ip, int(port))


def upsert_mongodb(mongo_client, cve, db_name, collection_name):
    db = mongo_client[db_name]
    collection = db[collection_name]
    postid = collection.update_one({'cve.CVE_data_meta.ID' : cve_data.get_cve_id(cve)},
                                   {"$set":{"cve" : cve_data.get_cve(cve), "configurations" : cve_data.get_configurations(cve), "impact" : cve_data.get_impact(cve), "publishedDate": cve_data.get_published_date(cve), "lastModifiedDate": cve_data.get_last_modified_date(cve)}},
                                   upsert=True)
    return postid


def find_by_cve(mongo_client, cve_id, db_name, collection_name):
    db = mongo_client[db_name]
    collection = db[collection_name]
    cve = collection.find_one({"cve.CVE_data_meta.ID": cve_id})
    return cve


def find_by_name(mongo_client, name, version, db_name, collection_name):
    db = mongo_client[db_name]
    collection = db[collection_name]
    cve = collection.find_one({"cve.affects.vendor.vendor_data.product.product_data.product_name": name})
    return cve
