import requests

bearerId = "MDI5YmQ2MzktYTY5ZC00NGYxLTg5MzMtOTY3NzM1ZTlhNWUwN2E0OTNiNTQtMGQ3"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vZGIzYTZmYjAtMDk0YS0xMWU4LTgzZDYtN2JlMDUzODYyN2Fj"
ngrokURL = TODO
webhookUrl = "https://api.ciscospark.com/v1/webhooks"

def doSparkPost(url):
    payload = "{\n  \"resource\" : \"messages\",\n  \"event\" : \"created\",\n  \"filter\" : \"roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZGIzYTZmYjAtMDk0YS0xMWU4LTgzZDYtN2JlMDUzODYyN2Fj\",\n  \"targetUrl\" : \"https://requestb.in/10a8xh71\",\n  \"name\" : \"Spark Learning Lab Webhook\"\n}\n"
    headers = {
        'Authorization': "Bearer " + bearerId,
        'Content-type': "application/json",
        'Cache-Control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

def getNewMessage(url):
    payload = "{\n\t\"name\": \"Nevermind\",\n\t\"targetUrl\": \""+ ngrokURL + ",\n\t\"resource\": \"messages\",\n\t\"event\": \"created\",\n\t\"filter\": \"roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZGIzYTZmYjAtMDk0YS0xMWU4LTgzZDYtN2JlMDUzODYyN2Fj\"\n}"
    headers = { 
        'Authorization': "Bearer " + bearerId,
        'Content-type': "application/json",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)


print(response.text)