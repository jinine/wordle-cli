import http.client

conn = http.client.HTTPSConnection("wordle-game-api1.p.rapidapi.com")

payload = '{"timezone":"UTC + 0"}'

headers = {
    'x-rapidapi-host': "wordle-game-api1.p.rapidapi.com",
    'Content-Type': "application/json"
}

def daily_word():
    conn.request("POST", "/word", payload, headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    return data.decode("utf-8")