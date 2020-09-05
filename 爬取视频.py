# https://blog.csdn.net/u012162613/article/details/41611889
#!/usr/bin/python

# import re
# import urllib.request
# def getHtml(url):
# 	page=urllib.request.urlopen(url)
# 	html=page.read()
# 	return html
#
# def getMp4(html):
# 	r=r"href='(http.*\.mp4)'"
# 	re_mp4=re.compile(r)
# 	mp4List=re.findall(re_mp4,html.decode('utf-8',"ignore"))
# 	filename=1
# 	for mp4url in mp4List:
# 		urllib.urlretrieve(mp4url,"%s.mp4" %filename)
# 		print('file "%s.mp4" done' %filename)
# 		filename += 1
#
# # url=input("please input the source url:")
# url = 'http://mov.bn.netease.com/mobilev/2011/9/8/V/S7CTIQ98V.mp4'
# html=getHtml(url)
# getMp4(html)


import requests
import re
import urllib

URL = 'http://www.pearvideo.com/video_1367621'
hd = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


def main():
	root = r'/Users/f7689680/Desktop/MyWorkPlace/luffy_py_algorithm'
	html = requests.get(URL, headers=hd).text
	# 匹配大盒子 视频URL
	url_MP4 = re.compile(r'(http://video.*?mp4.*?mp4)', re.S)  # 正则匹配
	url_MP4s = re.findall(url_MP4, html)
	print(url_MP4s)
	for i in url_MP4s:
		print(i)
	urllib.request.urlretrieve(i, 'haha.mp4')
	print('下载成功')

if __name__ == '__main__':
	main()
