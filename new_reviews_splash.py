import requests
from bs4 import BeautifulSoup
import pandas as pd

reviewlist = []

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2}) #The webpage to where the website is rendered.
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
                'Product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
                'Title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                'Rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                'Body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review) 
    except:
        pass

for x in range(1, 999):
    soup = get_soup(f'https://www.amazon.co.uk/product-reviews/B07WD58H6R/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}') #Remember to replace the https link with the second page of product link you want and keep the ={x} as it is by removing =2.
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_excel('Amazon_Reviews_Extracted.xlsx', index=False) #Name of the Excel file this will create.
print('Finished.')
