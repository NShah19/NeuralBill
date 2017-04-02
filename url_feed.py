from key_phrases import get_key_phrases


urls = [
    # 2014 URLS
    # 'https://www.congress.gov/bill/114th-congress/house-bill/2029/text'



    # 2016 URLS

]

for i in range(len(urls)):
    get_key_phrases(urls[i])