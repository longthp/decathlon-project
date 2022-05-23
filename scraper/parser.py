from requests_html import AsyncHTMLSession
import asyncio
import time
import json

async def parse_data(s, url):
    r1 = await s.get(url)
    r2 = await s.get(url + ".js")

    # Parse JSON output
    # js = json.loads(r2.text)
    js = r2.json()
    # Average rating
    try:
        rating = r1.html.find("span[itemprop=ratingValue]", first= True).text
    except:
        rating= None
    # Total reviews
    try:
        total_rv = r1.html.find("meta[itemprop=reviewCount]", first= True).attrs["content"]
    except:
        total_rv = None
    # Five-star reviews
    try:
        btn = r1.html.find("button[data-star-rating='5']", first= True)
        five_star_rv = btn.find("div div:nth-child(2)", first= True).text.strip()
    except:
        five_star_rv = None
	# Output data
    data = []
    for var in js["variants"]:
        color = var["option1"]
        size = var["option2"]
        item = {
            "product_id": js["id"],
            "variant_id": var["id"],
            "title": js["title"],
            "created_at": js["created_at"],
            "handle": js["handle"],
            "vendor": js["vendor"],
            "type": js["type"],
            "color": color if js["options"][0]["name"] == "Color" else size,
            "size": size if js["options"][1]["name"] == "Size" else color,
            "weight": var["weight"],
            "price": var["price"],
            "compare_at_price": 0 if var["compare_at_price"] is None else var["compare_at_price"],
            "available": var["available"],
            "inventory": var["inventory_quantity"],
            "rating": rating,
            "five_star_reviews": five_star_rv,
            "total_reviews": total_rv
        }
        data.append(item)

    return data

async def main(urls):
	s = AsyncHTMLSession()
	tasks = [parse_data(s, url) for url in urls]
	return await asyncio.gather(*tasks)

if __name__ == "__main__":
	urls = ["https://www.decathlon.com/products/mens-running-half-tights-kiprun",
			"https://www.decathlon.com/products/mens-trail-running-baggy-shorts",
			"https://www.decathlon.com/products/mens-hiking-t-shirt-short-sleeved-techfresh-100"]
	t3 = time.perf_counter()
	data = asyncio.run(main(urls))
	print(data)
	t4 = time.perf_counter()
	print("Gathered all data in {} seconds.".format(t4-t3))