#encoding:utf-8
import urllib
import urllib2
import cookielib

def get_login_cookie(url):
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({
            'password':'13874615621',
            'username':'6741437'
        })
    # 登录教务系统的URL
    loginUrl = url
    # 模拟登录，并把cookie保存到变量
    result = opener.open(loginUrl,postdata)
    # 保存cookie到cookie.txt中
    #cookie.save(ignore_discard=True, ignore_expires=True)
    # 利用cookie请求访问另一个网址，此网址是成绩查询网址
    #gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
    # 请求访问成绩查询网址
    #result = opener.open(gradeUrl)
   # print result.read()
    return cookie

if __name__ == '__main__':   
    url="http://weibo.com/"
    for item in get_login_cookie(url):
        print 3

print 3