import urllib2

def do_check():
    # Instantiate grains dictonary
    grains = {}

    # Instantiate grains key cloud Digital Ocean info
    grains['cloud_info'] = []

    base_url = 'http://169.254.169.254/metadata/v1/'

    id = urllib2.urlopen(base_url + 'id').read()
    region = urllib2.urlopen(base_url + 'region').read()

    grains['cloud_info'].append({'provider': 'Digital Ocean'})
    grains['cloud_info'][0]['droplet_id'] = id
    grains['cloud_info'][0]['droplet_region'] = region

    return grains

if __name__ == '__main__':
    do_check()
