import asyncio
import time
import pandas as pd
from scraper.sitemap import fltn
from scraper.sitemap import main as sm
from scraper.parser import main as pm

def work():
    t1 = time.perf_counter()
    sites = asyncio.run(sm())
    urls = fltn(sites)
    t2 = time.perf_counter()
    print(f"Gathered {len(urls)} links in {t2-t1} seconds.")

    t3 = time.perf_counter()
    data = asyncio.run(pm(urls))
    t4 = time.perf_counter()

    df = pd.DataFrame(fltn(data))
    df.to_csv("output.csv", index= False)
    print("Saved to csv.")
    print(f"Gathered {len(df)} records in {t4-t3} seconds.")

if __name__ == "__main__":
	work()