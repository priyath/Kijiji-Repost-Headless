# TODO: Actual error handling

import json
import os
from collections import OrderedDict
import requests
import yaml
from get_ids import get_location_and_area_ids

ad_file_name = 'item.yml'
ad_type = ['OFFER', 'WANTED']
price_type = ['FIXED', 'GIVE_AWAY', 'CONTACT', 'SWAP_TRADE']

def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

yaml.add_representer(OrderedDict, represent_ordereddict)


def run_program(path_to_yml):
    print('Enter the number corresponding to the location you wish to post this advertisement in:')

    location_id, location_area = get_location_and_area_ids()  # Returns a tuple containing location ID and area ID

    details = OrderedDict()

    details['postAdForm.locationId'] = location_id
    details['locationLevel0'] = location_area

    f = open(path_to_yml, 'a')
    f.write(yaml.dump(details))
    f.close()

    print("\"{}\" file updated. This file will be used to post your ad.".format(ad_file_name))


if __name__ == "__main__":
    run_program()
