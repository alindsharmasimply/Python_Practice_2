import bs4
import requests

def AmazonPrice():
	response = requests.get('https://www.amazon.in/Automate-Boring-Python-Albert-Sweigart/dp/1593275994')
	print response.raise_for_status()

	soup = bs4.BeautifulSoup(response.text, 'html.parser')
	s = soup.select('#soldByThirdParty > span ')
	print s[0].text

AmazonPrice()