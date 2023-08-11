import json
import pprint

import BeyotekTools.scraperutil as ScraperUtil
scraper = ScraperUtil.scraper()

get_url = f"https://www.lowes.com/pd/1000064061/productdetail/2434/Guest/14420?nearByStore=2434&zipState=NY"
page = scraper.get_rendered_page_json(get_url)
response = json.loads(scraper.get_contents_of_element_by_tag(page, 'pre')[0])

pprint.pprint(response)