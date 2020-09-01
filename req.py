import requests
r=requests.get("https://financialmodelingprep.com/api/v3/discounted-cash-flow/AAPL?apikey=demo")
print(r.text)
print(r.status_code)



# in post request function, there is an API end point and need to send date with it.

# url="www.something.com"
#
# data={
#     "p1":4,
#     "p2":8
# }
#
# r2=requests.post(url=url,data=data)