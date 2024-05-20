from django.http import JsonResponse
from django.shortcuts import render
from .models import Answer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
  answer = Answer()

  if request.method == "POST":
    post_data = json.loads(request.body.decode("utf-8"))
    answer.fio = post_data.get("fio")
    answer.come = post_data.get("come")
    answer.numberPeople = post_data.get("numberPeople")
    answer.beverages = post_data.get("beverages")

    answer.save()



  return render(request, "questionnaire/index.html", {"title": "пргилашение"})

def info(request):
  dataForFront = {
  "fio":[],
  "come":[],
  "numberPeople":[],
  "beverages":[],
  "comeInfo": 
    {
      "IWillCome": 0,
      "ICantCome": 0,
      "IWillInformYouLater": 0
    },
  "numberPeopleCount": 0,
  "beveragesInfo": 
    {
      "redWine": 0,
      "whiteWine": 0,
      "champagne": 0,
      "cognac": 0,
      "whiskey": 0,
      "vodka": 0,
      "I don't drink alcohol": 0
    },
  }
  fio = Answer.objects.values("fio")
  for i in range(0, len(fio)):
    dataForFront["fio"].append(fio[i]["fio"])

  come = Answer.objects.values("come")
  for i in range(0, len(fio)):
    dataForFront["come"].append(come[i]["come"])
    if come[i]["come"] == "I will come":
      dataForFront["comeInfo"]["IWillCome"] += 1
    elif come[i]["come"] == "I can't come":
      dataForFront["comeInfo"]["ICantCome"] += 1
    else:
      dataForFront["comeInfo"]["IWillInformYouLater"] += 1

  numberPeople = Answer.objects.values("numberPeople")
  numberPeopleCount = 0
  for i in range(0, len(fio)):
    numberPeopleCount += numberPeople[i]["numberPeople"]
    dataForFront["numberPeopleCount"] = numberPeopleCount

    dataForFront["numberPeople"].append(numberPeople[i]["numberPeople"])

  beverages = Answer.objects.values("beverages")
  numberPeople = Answer.objects.values("numberPeople")
  come = Answer.objects.values("come")
  for i in range(0, len(fio)):
    dataForFront["beverages"].append(beverages[i]["beverages"])
    
    if beverages[i]["beverages"] == "red wine":
      dataForFront["beveragesInfo"]["redWine"] += 1
    elif beverages[i]["beverages"] == "white wine":
      dataForFront["beveragesInfo"]["whiteWine"] += 1
    elif beverages[i]["beverages"] == "champagne":
      dataForFront["beveragesInfo"]["champagne"] += 1
    elif beverages[i]["beverages"] == "cognac":
      dataForFront["beveragesInfo"]["cognac"] += 1
    elif beverages[i]["beverages"] == "whiskey":
      dataForFront["beveragesInfo"]["whiskey"] += 1
    elif beverages[i]["beverages"] == "vodka":
      dataForFront["beveragesInfo"]["vodka"] += 1
    elif beverages[i]["beverages"] == "I don't drink alcohol":
      dataForFront["beveragesInfo"]["I don't drink alcohol"] += 1
  
  jsonData = json.dumps(dataForFront)

  if request.method == "GET":
    return render(request, "result/result.html", {"title": "итоги опросника",
                                                  "dataForFront": jsonData})
  
  return render(request, "result/result.html", {"title": "итоги опросника"})

