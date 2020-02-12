# Xici-ip-pool
爬取xici代理ip

考研结束，距离上次写代码已经过去了大半年。
重温爬虫知识
1.分析网页结构
www.xicidaili.com

使用python的request.get并不能得到网页的信息，返回代码503，说明网站服务器拒绝了我们的访问，需要设置伪装头，即Headers，打开浏览器的开发者工具，找到
Network这一项，即可看到访问网页时，浏览器的Request Headers，说明用python访问时，只用将我们伪装成浏览器，服务器就会接受我们的访问。在设置相应的请求头后，成功访问了www.xicidaili.com

2.使用beautifulsoup4
使用beautifulsoup4，将网页信息爬下来，在分析网页代码的时候，发现每一项ip 都是用<tr><td>标签记录的，那么我们只需要找到所有的<tr><td>标签，即刻找到所有的代理ip。
	
3.成功找到后，将每一条逐项写入txt文本中，在以后需要代理ip时，便可以使用代理ip，在request.get中，加入ip参数，即刻使用代理ip访问网站了。
