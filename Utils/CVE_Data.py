def get_cve_id(cve):
    return cve['cve']['CVE_data_meta']['ID']


def get_cve(cve):
    return cve['cve']

def get_configurations(cve):
    return cve['configurations']


def get_impact(cve):
    return cve['impact']


def get_published_date(cve):
    return cve['publishedDate']


def get_last_modified_date(cve):
    return cve['lastModifiedDate']
