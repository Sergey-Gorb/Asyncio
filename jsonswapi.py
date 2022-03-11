from collections import namedtuple
from urllib.parse import urlparse
import aiohttp
import more_itertools

Service = namedtuple('Service', ('name', 'url_part', 'field'))

SERVICES = (
    Service('starships', 'starships', 'name'),
    Service('films', 'films', 'title'),
    Service('planets', 'planets', 'name'),
    Service('species', 'species', 'name'),
    Service('vehicles', 'vehicles', 'name'),
    Service('people', 'people', 'name')
)
URL = 'https://swapi.dev/api'


async def aiohttp_get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service, people_dict, part_dict):
    print('Fetching IP from {}'.format(service.name))
    for person_ids in range(1, 100):
        temp_url = f'{URL}/{service.name}/{person_ids}/'
        json_response = await aiohttp_get_json(temp_url)
        try:
            pd_key = service.name + str(person_ids)
            if service.name == 'people' and 'detail' not in json_response.keys():
                people_dict[person_ids] = json_response
            else:
                part_dict[pd_key] = json_response[service.field]
        except Exception:
            pass


def get_key_from_url(url):
    dirs = urlparse(url).path.strip('/').split('/')
    return ''.join(dirs[-2::1])


def get_list_keys_from_url(dict_part: dict, list_url: list):
    return ', '.join(dict_part[get_key_from_url(url)] for url in list_url)


async def update_sw_fields(people: dict, part_dict: dict):
    val = get_key_from_url(people['homeworld'])
    people['homeworld'] = part_dict[val]
    people['films'] = get_list_keys_from_url(part_dict, people['films'])
    people['starships'] = get_list_keys_from_url(part_dict, people['starships'])
    people['vehicles'] = get_list_keys_from_url(part_dict, people['vehicles'])
    people['species'] = get_list_keys_from_url(part_dict, people['species'])




