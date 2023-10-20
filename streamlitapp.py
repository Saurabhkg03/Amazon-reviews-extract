import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import base64
from io import BytesIO

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_product_name(url):
    soup = get_soup(url)
    return soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip()

def get_reviews(soup):
    reviewlist = []
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
                'Product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
                'Title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                'Rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                'Body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass
    return reviewlist

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.close()
    output.seek(0)
    return output.getvalue()

def get_table_download_link(df, filename='Amazon_Reviews_Extracted.xlsx'):
    val = to_excel(df)
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}">Download Reviews</a>'

st.title('Amazon Review Scraper📝')

url = st.text_input('Enter the Amazon product URL:')

if st.button('Search for Product'):
    product_name = get_product_name(url)
    st.write(f'Product for review scraping: **{product_name}**')

if st.button('Scrape Reviews'):
    with st.spinner('Scraping reviews...'):
        reviewlist = []
        total_pages = 10  
        total_iterations = total_pages * 5  
        
        progress_bar = st.progress(0)  
        percent_complete = st.empty()  
        
        for star in ['one_star', 'two_star', 'three_star', 'four_star', 'five_star']:
            for x in range(1, total_pages+1):
                soup = get_soup(f'{url}/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&pageNumber={x}&filterByStar={star}')
                reviewlist.extend(get_reviews(soup))
                
                progress = (x + (total_pages * ['one_star', 'two_star', 'three_star', 'four_star', 'five_star'].index(star))) / total_iterations
                progress_bar.progress(progress)  
                percent_complete.text(f"Progress: {int(progress*100)}%")  
                
                if not soup.find('li', {'class': 'a-disabled a-last'}):
                    pass
                else:
                    break
            
        df = pd.DataFrame(reviewlist)
        st.success('Scraping is completed!')
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)
