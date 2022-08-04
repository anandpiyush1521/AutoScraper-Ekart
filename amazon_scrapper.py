from autoscraper import AutoScraper

amazon_url = "https://www.amazon.in/s?k=iphones"
wantedlist = ["₹49,900","Apple iPhone 11 (128GB) - Yellow"]

scraper = AutoScraper()
result = scraper.build(amazon_url, wantedlist)

print(scraper.get_result_similar(amazon_url, grouped=True))

scraper.set_rule_aliases({'rule_taod':'Title','rule_v0gn':'Price'})
scraper.keep_rules(['rule_taod','rule_v0gn'])
scraper.save('amazon-search')