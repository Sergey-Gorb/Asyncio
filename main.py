import asyncio
from jsonswapi import fetch_ip, SERVICES, update_sw_fields
from rec import save_people_in_db

URL = 'https://swapi.dev/api'
PART_DICT = {}
PEOPLE_DICT = {}


async def async_main():
    futures = [fetch_ip(service, PEOPLE_DICT, PART_DICT) for service in SERVICES]
    await asyncio.wait(futures)

    trans = [update_sw_fields(people, PART_DICT) for people in PEOPLE_DICT.values()]
    await asyncio.wait(trans)

    save_rec = [save_people_in_db(p_k, people_rec) for p_k, people_rec in PEOPLE_DICT.items()]
    await asyncio.wait(save_rec)


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()