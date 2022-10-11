# # import libraries to handle request to api
# import requests
# import json
# import pprint
# # base currency or reference currency
# base = "GBP"

# # required currency for plot
# out_curr = "SEK"

# # exchange data from a date
# start_date = "2022-10-01"

# # exchange data till a date
# end_date = "2022-10-11"

# # api url for request
# url = "https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}".format(
#     base, start_date, end_date, out_curr)

# response = requests.get(url)

# # retrieve response in json format
# data = response.json()

# # print(data["rates"])
# pprint.pprint(data["rates"])


import requests

base = "GBP"

# required currency for plot
out_curr = "SEK"

# exchange data from a date
start_date = "2022-10-05"

# exchange data till a date
end_date = "2022-10-11"

url = "https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}".format(
    base, start_date, end_date, out_curr)

response = requests.get(url)
data = response.json()

print(data)
