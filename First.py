import requests


response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print response.status_code
print len(response.text)
# print response.text[:500]

#badResponse = requests.get('https://assddffgghh.com/gfdfdffg')
# badResponse.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in response.iter_content(100000):
    playFile.write(chunk)
playFile.close()
