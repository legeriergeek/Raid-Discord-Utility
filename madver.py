import requests
channel = input("Your Channel Number :")
url = f"https://discord.com/api/v9/channels/{channel}/messages"

server = input("put your server number or just @me for the DMs")
auth = input("your authorization thing")
xsp = input("your X-Super-Properties thing")
cookie  = input("Your cookie")

headers = {
    "Host": "discord.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Authorization": auth,
    "X-Super-Properties": xsp,
    "X-Discord-Locale": "fr",
    "X-Discord-Timezone": "Europe/Paris",
    "X-Debug-Options": "bugReporterEnabled",
    "Content-Length": "26",  # Ajustement de la longueur du contenu
    "Origin": "https://discord.com",
    "Alt-Used": "discord.com",
    "Connection": "keep-alive",
    "Referer": f"https://discord.com/channels/{server}/{channel}",
    "Cookie": cookie,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}
message  = input("What do u want to send: ")
data = {
    "content": message
}

howmanytimes = input("How many messages to sent? ")
x = int(howmanytimes)
y = 0
while(x>y):
    response = requests.post(url, headers=headers, json=data)
    #making it better
    if response.status_code == 200:
        print(response.text)
        y+1
        sleep(0.2)
    else:
        print(f"Error {response.status_code}: {response.text}")
