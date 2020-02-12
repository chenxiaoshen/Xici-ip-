from bs4 import BeautifulSoup
import requests

def get_ip(url, headers):

	web = requests.get(url, headers=headers)
	#print(web_data.status_code)
	soup = BeautifulSoup(web.text, 'lxml')
	ips = soup.find_all('tr')
	f = open('IP.txt', 'a+', encoding='utf-8')

	for ip in ips[1:]:
		ip_ = ip.find_all('td')
		#print(ip_)
		ipadd = ip_[1].text
		ipport = ip_[2].text
		ipty = ip_[5].text
		f.write(str(ipty))
		f.write(':')
		f.write(str(ipadd))
		f.write(':')
		f.write(str(ipport))
		f.write('\n')
	f.close()

if __name__ == '__main__':
	for i in range(1,10):
		url = 'https://www.xicidaili.com/nn/{}'.format(i)
		headers = {
			'Host': 'www.xicidaili.com',
			'Referer': 'https://www.xicidaili.com/nn/',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
		}
		ip_pool = get_ip(url, headers=headers)


