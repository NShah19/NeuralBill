from key_phrases import get_key_phrases


urls = [
    # 2014 URLS
    'https://www.congress.gov/bill/114th-congress/house-bill/2029/text',
    'https://www.congress.gov/bill/114th-congress/senate-bill/3084/text?format=txt',
    'https://www.congress.gov/bill/114th-congress/house-bill/1321/text',
    'https://www.congress.gov/bill/114th-congress/house-bill/6477/text',
    'https://www.congress.gov/bill/114th-congress/house-bill/6302/text',

    'https://www.congress.gov/bill/114th-congress/house-resolution/569/text?format=txt',
    'https://www.congress.gov/bill/114th-congress/house-bill/6507/text?format=txt',
    'https://www.congress.gov/bill/114th-congress/house-bill/6505/text?format=txt',
    'https://www.congress.gov/bill/114th-congress/house-bill/6501/text?format=txt',
    'https://www.congress.gov/bill/114th-congress/house-bill/6496/text?format=txt',

    # 2016 URLS
    'https://www.congress.gov/bill/115th-congress/senate-bill/442/text?format=txt',
    'https://www.congress.gov/bill/115th-congress/house-bill/255/text',
    'https://www.congress.gov/bill/115th-congress/house-bill/39/text',
    'https://www.congress.gov/bill/115th-congress/house-bill/72/text',
    'https://www.congress.gov/bill/115th-congress/house-joint-resolution/40/text',

    'https://www.congress.gov/bill/115th-congress/house-bill/1431/text?format=txt',
    'https://www.congress.gov/bill/115th-congress/house-bill/1367/text?format=txt',
    'https://www.congress.gov/bill/115th-congress/house-bill/1365/text?format=txt',
    'https://www.congress.gov/bill/115th-congress/house-bill/1628/text?format=txt',
    'https://www.congress.gov/bill/115th-congress/house-bill/274/text?format=txt',
]

get_key_phrases(urls[18])