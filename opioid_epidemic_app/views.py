from django.shortcuts import render, render_to_response
import requests

def index(request):
    url = "https://data.cdc.gov/resource/tenp-43rk.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    counties = []
    for item in data:
        counties.append(item['county'])
    countyList = set(counties)
    countyList = sorted(countyList)
    return render_to_response("index.html", {'counties': countyList, 'allData': data})
