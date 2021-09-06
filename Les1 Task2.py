#взял пример из одного своего практического кейса где надо было мониторить расписание и сообщать если есть удобное место для записи
import requests

url = 'https://....ru'
s = requests.session()
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"})
r = s.get(url)

cookies = r.cookies.get_dict()


cookies = {
    'AspxAutoDetectCookieSupport': '1',
    'ASP.NET_SessionId': 'go1hshhve54bncte2a1sne0t',
    '.AutorealAuth': '0AFA88FB334C9920E7CEEFC9CAE94634A1FA6242ABFDB4E5E434C9966427691F1147F67DCDFB7DEFA6AF347',
}

headers = {
    'authority': '....ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not\\"A\\\\Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'upgrade-insecure-requests': '1',
    'origin': 'https://avtoreal-record.ru',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'script',
    'referer': 'https://avtoreal-record.ru/Users/Default.aspx',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
  '__LASTFOCUS': '',
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': 'oyr6gGw61fPVvUq2+3Jb++7Pxj5OD0SHrqCKAyXYr0qUW1qYRg7lHlWyfhLQi6FlpZHo5EfADcC1MmtAWmBqx0shbcCvfzkQ758iU9uGsqcFCRIzZu+L5xs/NOY2W8cUzKa6B65kQo9gBL06+dFrfn8qbLRg/0qos8K+awrsa8ydyZgu9eoG5isDdLKA6kCvs/cq13B/CmvB5nktam44TXInjPSwDppbzob4NS/pBLN9lxtwVMWZXABPkEfTfeoBPYi5W5wRfLj92koP1FClC1S4AYZHkxWzNDCaRpn2budK3hC8Wbnb6D35gDU9w8mAYIbU9MbR6El3/T1CHu5M0OZ5EgAMY7RJml4EW0u8jV8=',
  '__VIEWSTATEGENERATOR': 'CB4E55BE',
  '__PREVIOUSPAGE': 'kHfhgwAyL4DlaZcVknTgRtpxhfn5kNisKQcPN-7iw9LpLHppOlrBTBKEjYR8q_-r_G5hEryCsiKkI24_ge_U-w2',
  '__EVENTVALIDATION': 'MNMla5J6unmUtRr0fklWpUwcLwIs9QvVH+5+QLA0McDFxqB3Hjk93KmbdFGfAyOg9Jbpf9Gszg5aAcuzZbR8Vk2ihTorK4ZXlBI6M+BnBp9exZp42H0C9lNr2gr4ei1QXCjWR88GdA/O5qcUw4o5zMAEjIUOBpTKaQ1mfduWSW35SNVIKDW44FZW1uT2Oa8N9wsUqBIYS7ftU/KaYhUHMg==',
  'LoginTextBox': 'login',
  'PasswdTextBox': 'passwd',
  'OkButton': '\u0412\u0445\u043E\u0434'
}

response = requests.post('https://avtoreal-record.ru/Auth.aspx', headers=headers, cookies=cookies, data=data)

#soup = BeautifulSoup(response.content, "html.parser")
#дальше был анализ ответных данных
