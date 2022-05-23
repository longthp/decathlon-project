from requests_html import AsyncHTMLSession
from itertools import chain
import asyncio
import time

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"}

def fltn(i):
	return list(chain.from_iterable(i))

async def product_sitemaps(s, url):
	r = await s.get(url, headers= headers)
	sites = r.html.find("loc")
	return [site.text for site in sites if site.text.startswith("https://www.decathlon.com/sitemap_products")]

async def get_links(s, url):
	r = await s.get(url, headers= headers)
	links = r.html.find("loc")
	
	categories = ["men", "women", "kid", "babies"]
	results = []
	for cat in categories:
		for link in links:
			if link.text.startswith(f"https://www.decathlon.com/products/{cat}"):
				results.append(link.text)
			else:
				pass
	return results

async def main():
	s = AsyncHTMLSession()
	url = "https://www.decathlon.com/sitemap.xml"
	sitemaps = await product_sitemaps(s, url)

	tasks = [get_links(s, site) for site in sitemaps]
	return await asyncio.gather(*tasks)

if __name__ == "__main__":
	t1 = time.perf_counter()
	results = asyncio.run(main())
	t2 = time.perf_counter()
	print(len(fltn(results)))
	print(t2-t1)