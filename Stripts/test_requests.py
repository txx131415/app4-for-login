import requests

# get
# res = requests.get("http://192.168.45.37:5000/query_user_random")
# # 返回状态码
# print(res.status_code)
# # 返回text文本内容
# print(res.text)
# # 返回json格式
# print(res.json().get("data"))

res = requests.get("http://www.baidu.com")
print(res)
print(res.status_code)
# print(res.text)
