import random, ArabicNames, string
import urllib.request, time
from termcolor import colored


proxyURL = '' # Put your proxy url & credentials from brightdata here 

from anticaptchaofficial.recaptchav3proxyless import recaptchaV3Proxyless


def getCaptchaKey():
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1)
    solver.set_key("") # Put your anticaptchaofficial key here 
    solver.set_website_url("https://nightflix.fun/")
    solver.set_website_key("6LcWUpAmAAAAAF8zeyYRwRUFxW2FWS-TVaIptGV5")
    solver.set_min_score(0.3)

    # Specify softId to earn 10% commission with your app.
    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
    solver.set_soft_id(0)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print ("Captcha OK")
        return g_response

def send_p_request(url, payload):
    global proxyURL
    '''
    headers = {
        'authority': 'nightflix.fun',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        'cookie': 'amp_a0683b=m_EmCk82rgR4absA3ZxTZo.MmZteWd2Mnh3ZG8yeQ==..1h2rg8jqi.1h2rg8qhi.0.0.0',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    headers = {
    "Authority": "nightflix.fun",
    "Method": "POST",
    "Path": "/api/reserve",
    "Scheme": "https",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,ar;q=0.5",
    "Content-Length": "1850",
    "Content-Type": "application/json",
    "Cookie": "amp_a0683b=m_EmCk82rgR4absA3ZxTZo.MmZteWd2Mnh3ZG8yeQ==..1h2rg8jqi.1h2rg8qhi.0.0.0",
    "Origin": "https://nightflix.fun",
    "Referer": "https://nightflix.fun/",
    "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Kl-Saas-Ajax-Request": "Ajax_Request"
    }

    '''
    headers = {
    'Host': 'nightflix.fun',
    'Connection': 'keep-alive',
    'Content-Length': '1868',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://nightflix.fun',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://nightflix.fun/?Name=test+test&Age=21&Email=testtesttest%40gmail.com&Number=25836914&Link=https%3A%2F%2F&Ville=Manzel+Cheker',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
    }

    headers["referer"] = url

    opener = urllib.request.build_opener(
    urllib.request.ProxyHandler(
        {'http': str(proxyURL),
        'https': str(proxyURL)}))
    opener.addheaders = headers.items()

    
    encoded_data = urllib.parse.urlencode(payload).encode()
    response = opener.open(url, data=encoded_data)
    # IP CHECK
    #r2 = opener.open('https://api.ipify.org')
    #print(r2.read().decode())
    
    '''
    r2 = opener.open('https://api.ipify.org')
    print(r2.read().decode())

    r2 = opener.open('https://api.ipify.org')
    print(r2.read().decode())
    '''
    return response.read().decode()

def lambda_handler(event, context):
    
    name = ArabicNames.get_full_name()

    name_trimmed = name.replace(' ', '').lower()

    def generate_random_phone_number():
        prefix = random.choice([2, 5, 9])
        suffix = random.randint(1000000, 9999999)
        phone_number = f"{prefix}{suffix}"
        return phone_number

    def get_random_ville():
        options = ["Manzel Cheker", "El Ayn", "Lafrane", "Matar", "Tanyour", "Bouzayene", "Gremda", "Trik tounes", "Kaid Mhammed"]
        get_random_ville = random.choice(options)
        return get_random_ville

    def generate_random_social_media_url(name):
        platforms = ["facebook", "instagram"]
        random_platform = random.choice(platforms)

        if random_platform == "facebook":
            base_url = "https://www.facebook.com/"
        elif random_platform == "instagram":
            base_url = "https://www.instagram.com/"
        url = base_url + name
        return url

    def generate_captcha_token():
        random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        token = f"{random_chars}-{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))}-{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))}-{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))}-{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))}"
        return token

    payload = {
        "Name": name,
        "Age": str(random.randint(18, 28)),
        "Email": f"{name_trimmed}@gmail.com",
        "Number": str(generate_random_phone_number()),
        "Link": "https://" + "Send_500_USD_to_this_wallet_12v2HaqT5FQ6Dq4N24tSePy4u7eNcv7EzD" ,  #generate_random_social_media_url(name_trimmed), #
        "Ville": get_random_ville(),
        "gReCaptchaToken": getCaptchaKey()
        }
    
    time.sleep(0.5)
    print(payload)

    # Brightdata Request
    r = send_p_request('https://nightflix.fun/api/reserve', payload)
    if r == "Your reservation request is saved, please check your mail for more information":
        print(colored(str(r), "green"))
    else:
        print(colored(str(r), "red"))

    ''' Normal Request
    r = requests.post('https://nightflix.fun/api/reserve', data=payload)
    print(r.text)
    '''
    return r


while True:
    try:
        response = lambda_handler(None, None)
    except:
        print('ERROR')
        pass