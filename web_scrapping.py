import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Request was successful!")
    html_content = response.text
    with open('file.txt','w',encoding='utf-8') as f:
        f.write(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    
    quotes = soup.find_all('div',class_="quote")

    for quote in quotes:
        quote_text = quote.find('span', class_='text').get_text()
        
        author = quote.find('small', class_='author').get_text()
        

        tags = [tag.text for tag in quote.findAll('a',class_='tag')]

        # Print out the quote, author, and tags
        print(f"Quote: {quote_text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 50)
    

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
