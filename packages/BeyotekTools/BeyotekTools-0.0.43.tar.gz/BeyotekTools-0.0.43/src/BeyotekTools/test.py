import json
import pprint

import scraperutil as ScraperUtil
scraper = ScraperUtil.scraper()

get_url = f"https://www.lowes.com/pd/1000064061/productdetail/2434/Guest/14420?nearByStore=2434&zipState=NY"
page = scraper.get_rendered_page(get_url,'3.95.64.251:8888')


response=json.loads(scraper.find_element_by_attribute_equals(page, 'div', 'id', 'json', True))


pprint.pprint(response)