from threading import Lock
import Utils.Json as json_loader
import Utils.File as file
import Utils.MongoDB as mongo
import Utils.CVE_Data as cve_data
import Utils.Downloader as downloader
import logging

logging.basicConfig(filename='LOG.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
# settings_file = "Utils//Settings.json"
settings_file = "..//Utils//Settings.json"
settings = json_loader.load_from_file(settings_file)
settings_mongo = settings['mongo_settings']


class DAL(object):
    _instance = None

    def downloadNVD(self):
        """
        Downloading NVD Data feeds.
        """
        if settings['download_files']:
            # Load List of targets to download
             download_urls = '..//Utils//URLs.json'
             # download_urls = 'Utils//URLs.json'
             urls = json_loader.load_from_file(download_urls)
            # Download all the JSON files first
             downloader.download_definitions(settings['json_folder'], urls)
             settings['download_files'] = False
        json_loader.save_file(settings, settings_file)

    def createDB(self):
        """
        Create the db from the data feeds.
        """
        if settings['setup_db'] is False:
            return
        mongo_client = mongo.connect_mongodb(settings_mongo['ip'], settings_mongo['port'])
        logging.info("Connected to MongoDB at {}".format(settings_mongo['ip']))
        # Read from every JSON in the path and insert into MONGODB
        count = 0
        for json_filepath in file.iterate_directory(settings['json_folder'], '.json'):
            # Read nvd CVE JSON file
            data = json_loader.load_from_file(json_filepath)
            logging.info("Loaded JSON data from {}".format(json_filepath))
            # Iterate throughout the CVEs
            for cve in data['CVE_Items']:
                cve_id = cve_data.get_cve_id(cve)

                # For each CVE, insert into MONGODB
                post_id = mongo.upsert_mongodb(mongo_client, cve, settings['application_name'], settings['collection_name'])
                if post_id is not None:
                    logging.info("Adding data {}".format(cve_id))
                    count += 1
        logging.info("Done... {} records added".format(count))
        settings['setup_db'] = False
        json_loader.save_file(settings, settings_file)

    def getVulnerabilityByName(self, name, version):
        """
        Searching vulnerability by name.
        """
        mongo_client = mongo.connect_mongodb(settings_mongo['ip'], settings_mongo['port'])
        logging.info("Searching Vulnerability by Name ... ".format())
        cve = mongo.find_by_name(mongo_client, name, version, settings['application_name'], settings['collection_name'])
        if cve == None:
            logging.info("Vulnerability Not Found ... ".format())
        else:
            logging.info("Vulnerability Found ... ".format())
        return cve

    def getVulnerabilityByCVE(self, cve_id):
        """
        Searching vulnerability by CVE.
        """
        mongo_client = mongo.connect_mongodb(settings_mongo['ip'], settings_mongo['port'])
        logging.info("Searching Vulnerability by CVE ... ".format())
        cve = mongo.find_by_cve(mongo_client, cve_id, settings['application_name'], settings['collection_name'])
        if cve == None:
            logging.info("Vulnerability Not Found ... ".format())
        else:
            logging.info("Vulnerability Found ... ".format())
        return cve

    def __new__(cls, *args, **kwargs):
        if DAL._instance is None:
            with Lock():
                if DAL._instance is None:
                    DAL._instance = super().__new__(cls, *args, **kwargs)

        return DAL._instance


