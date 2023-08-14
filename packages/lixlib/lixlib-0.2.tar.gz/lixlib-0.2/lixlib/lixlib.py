import requests
from user_agent import generate_user_agent
import json
from telethon import TelegramClient, sync, errors
from telethon.sessions import StringSession
from telethon.tl.functions.account import CheckUsernameRequest
from datetime import datetime
class info:
    def tiktok(username: str) -> str:
        def user_create_time(url_id):
            binary = "{0:b}".format(url_id)
            i = 0
            bits = ""
            while i < 31:
                bits += binary[i]
                i += 1
            timestamp = int(bits, 2)
            dt_object = datetime.fromtimestamp(timestamp)
            return dt_object

        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        r = requests.get(f"https://www.tiktok.com/@{username}", headers=headers)
        server_log = str(r.text)

        try:
            start_key = '},"UserModule":{"users":{'
            data = server_log.split(start_key)[1]         
            user_info = {}
            user_info['user_id'] = data.split('"id":"')[1].split('",')[0]
            user_info['name'] = data.split(',"nickname":"')[1].split('",')[0]
            user_info['verified'] = "Yes" if data.split('"verified":')[1].split(',')[0] == "true" else "No"
            user_info['secUid'] = data.split(',"secUid":"')[1].split('"')[0]
            user_info['private'] = "Yes" if data.split('"privateAccount":')[1].split(',')[0] == "true" else "No"
            user_info['followers'] = data.split('"followerCount":')[1].split(',')[0]
            user_info['following'] = data.split('"followingCount":')[1].split(',')[0]
            user_info['last_change_name'] = str(user_create_time(int(data.split('"nickNameModifyTime":')[1].split(',')[0])))
            user_info['account_region'] = data.split('"region":"')[1].split('"')[0]
            info = json.dumps(user_info, indent=2)
            return info
        except IndexError:
            return None

    def instagram(username: str) -> str:
        headers1 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar',
            'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-asbd-id': '198387',
            'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
        }
        url1 = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        try:
            re = requests.get(url1, headers=headers1).json()
            state = True
        except:
            state = False
            data = {
                "telegram": "@U_L_W",
                "State": f'{state}'
            }
            info = json.dumps(data)
            return info
            exit()
        re = re['data']['user']
        bio = re["biography"]
        followers = re["edge_followed_by"]["count"]
        following = re["edge_follow"]["count"]
        name = re["full_name"]
        id = re["id"]
        business_phone_number = re['business_phone_number']
        business_email = re['business_email']
        verified = re['is_verified']
        private = re['is_private']
        business = re['is_business_account']
        lite = re['highlight_reel_count']
        pic = re['profile_pic_url_hd']
        pronouns = re['pronouns']
        posts = re["edge_owner_to_timeline_media"]["count"]
        threads_check = requests.get(f'https://www.threads.net/@{username}').text
        if 'og:description' in threads_check:
            threads = True
        else:
            threads = False
        date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]
        data = {
            "telegram": "@U_L_W",
            "State": f'{state}',
            "username": username,
            "name": name,
            "id": int(id),
            "pic": pic,
            "business": bool(business),
            "business_phone_number": bool(business_phone_number),
            "business_email": bool(business_email),
            "pronouns": pronouns,
            "Highlight_count": int(lite),
            "followers": int(followers),
            "following": int(following),
            "posts": int(posts),
            "bio": bio,
            "threads": threads,
            "verified": bool(verified),
            "private": bool(private),
            "date": date,
            "link": f"https://instagram.com/{username}"
        }
        info = json.dumps(data, indent=2)
        return info
 #def threads(username: str) -> str:
class email:
 def gmail(email: str) -> str:
  url = 'https://android.clients.google.com/setup/checkavail'
  h = {'Content-Length':'98','Content-Type':'text/plain; charset=UTF-8','Host':'android.clients.google.com','Connection':'Keep-Alive','user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
  d = json.dumps({'username':email,'version':'3','firstName':'ahmed','lastName':'mohammed'})
  res = requests.post(url,data=d,headers=h)
  if res.json()['status'] == 'SUCCESS':
   finish = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "available"}
   r = json.dumps(finish, indent=2)
   return r
  else:
        finish = {
                "telegram": "@U_L_W",
                "email": email,
                "state": "unavailable"}
        rn = json.dumps(finish, indent=2)
        return rn
 def aol(email: str) -> str:
   url = "https://login.aol.com/?src=fp-us&client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&crumb=AH.TAXqWj1R&intl=us&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&pspid=1197803361&activity=default&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DtXznGnGisTTl7nkz3XeJ9Zc42bJaU5ls%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E" 
   headers = {
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate, br',
   'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
   'Content-Length': '1575',
   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
   'Cookie': 'A1=d=AQABBLX0x2QCEEW46iTO8YFwy6gysqqz_WMFEgEBAQFGyWTRZM1n0CMA_eMAAA&S=AQAAAhcrMTDXRe5yt1BDlB9pjos; A3=d=AQABBLX0x2QCEEW46iTO8YFwy6gysqqz_WMFEgEBAQFGyWTRZM1n0CMA_eMAAA&S=AQAAAhcrMTDXRe5yt1BDlB9pjos; A1S=d=AQABBLX0x2QCEEW46iTO8YFwy6gysqqz_WMFEgEBAQFGyWTRZM1n0CMA_eMAAA&S=AQAAAhcrMTDXRe5yt1BDlB9pjos&j=WORLD; cmp=t=1690825910&j=0&u=1---; gpp=DBAA; gpp_sid=-1; weathergeo=%2224.97%7C55.31%7CDubai%7C%7CUnited%20Arab%20Emirates%7C0%7C2347111%22; rxx=285tmss874m.37yvhrbh&v=1; AS=v=1&s=47Gsv2Tr&d=A64c94789|.aI_XiD.2Srrm3fDyO5ZgGHCbkYwIliNXww61Cog7QVbYThA1CQsEwQQaqTWL1cSxIbjlZtkUh1rL5ua8CxwOPRz.kenP_PLcHwAkOZaLIlJyH2_UuqpLfpBzrWOs6Uj63HNnVU1CqegdkkAIeoHmdwQmb6JfQl0V1qE2UVucT4div35Zbd7U44jCJ.kPgzTUH4qZ5qO5OD9t5RhoyENIZu3J_0dzbG360aO3cDY6BS1_fhzHBU42UvNe4Me4lLfVq0B8Y6o8ZH5PdiRP8eVlOJcFkR79bs3TckhVoeW.0L96caP0fciFQHPu.2CdH679A3sgw6UoV.2Bb6marPxwrStY5wPkIYAGB8N7xewh_VWOjhOyxmAluJG4jbmv87Iz3KDlriaLG8fNsQZ0KxL0bno6jufVo9Hc3TT8RSnbD96bgB9fCpkfdkUgI.q09f67rMZ5NDTVYaPzEmvgdD5dBhlGeQ1iXbV7na4I.GKW_BwWJ5wbaZtwngAD7jfwpVeYHJ7rXOcaL5Smdj3D3UgsLMio0pX1.11D8sfDS.qiKwSSCHMHQKvO0BafZ6lAIDBq6.XjoZJKt1b5zYr.nPf7vWnS_cTfXELnuQxQU2v_YE6GYwPktcQnV4MOunK3FSQ3_U9kVaAw9SuqTKmFljVOLlKZYoM0c9h4CW6gpyDNZIfBexyCnTv3X8LKur6EL2ZcOjLoViaVeXUH7..6JIUR.xbKeU_c30bRZ8lLwvBo7VeKy61jBt_BD_NHGRKZL7lbQRe6HlAfpPW4_f0jotBhEF7hXwSLk.Uq3descqLnO8OApfKXrJdOXYWWw--~A',
   'Origin': 'https://login.aol.com',
   'Referer': 'https://login.aol.com/?src=fp-us&client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&crumb=AH.TAXqWj1R&intl=us&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&pspid=1197803361&activity=default&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DtXznGnGisTTl7nkz3XeJ9Zc42bJaU5ls%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E',
   'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
   'Sec-Ch-Ua-Mobile': '?0',
   'Sec-Ch-Ua-Platform': '"Windows"',
   'Sec-Fetch-Dest': 'empty',
   'Sec-Fetch-Mode': 'cors',
   'Sec-Fetch-Site': 'same-origin',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
   'X-Requested-With': 'XMLHttpRequest',}
   data = {
'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":2,"pixelRatio":1.25,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Mobile Intel(R) 4 Series Express Chipset Family (Microsoft Corporation - WDDM 1.1) Direct3D9Ex vs_3_0 ps_3_0, igdumd64.dll)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1093","h":"615"},"availableResolution":{"w":"584","h":"1093"},"ts":{"serve":1690825968030,"render":1690825966448}}',
   'crumb': 'pvFB2XYQRLH',
   'acrumb': '47Gsv2Tr',
   'sessionIndex': 'QQ--',
   'displayName': '',
   'deviceCapability': '{"pa":{"status":false}}',
   'username': email,
   'passwd': 'aa',
   'signin': 'Next',}
   try:
    r = requests.post(url,headers=headers,data=data).json()['errorMsg']
    if "Sorry, we don't recognize this" in r:
       finish = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "available"}
       r = json.dumps(finish, indent=2)
    else:
        finish = {
          "telegram": "@U_L_W",
          "email": email,
          "state": "unavailable"}
        rn = json.dumps(finish, indent=2)
        return rn
   except:
     finish = {
       "telegram": "@U_L_W",
       "email": email,
       "state": "unavailable"}
     rn = json.dumps(finish, indent=2)
     return rn
   return r
class linked:
 def tiktok(email: str) -> str:
  url = 'https://api16-va.tiktokv.com/passport/email/send_code/?passport-sdk-version=19&os_api=22&device_type=SM-G975N&ssmix=a&manifest_version_code=2021806060&dpi=240&uoo=0&carrier_region=AR&region=IQ&app_name=musical_ly&version_name=18.6.6&timezone_offset=10800&ts=1660261379&ab_version=18.6. 6&residence=AR&cpu_support64=false&current_region=US&ac2=wifi&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=2021806060&channel=googleplay&_rticket=1660261381871&device_platform=android&iid=7126814077612115718&build_number=18.6.6&locale=ar&op_region=AR&version_code=180606&timezone_name=Europe%2FMoscow&cdid=86654e69-0edf-405a-a5a1-181f0e7aa14f&openudid=1c8a72b315ac7fbf&sys_region=IQ&device_id=6833300910404519430&app_language=ar&resolution=1280*720&os_version=5.1.1&language=en&device_brand=samsung&aid=1233&mcc_mnc=310410'
  headers = {
        'Host': 'api16-va.tiktokv.com', 'x-ss-stub': '04465DFECBF3ED2D56AF61B7DE2921AB','accept-encoding': 'gzip','passport-sdk-version': '19','sdk-version': '2','x-ss-req-ticket': '1660261382504','cookie': 'odin_tt=7a321b6667e2ada3027155e053cc1e681ac076f643fbe4861f283fe2ecbc80c1260f1371bb96c8a4812ba32df7d22d49b785a5ba640289e1913e674bd3ffd6b52e8e38d3ade7f3d2d3e41f79931cfb1d4; passport_csrf_token_default=f7bdb605ee9f55f0186b3f0da6cc71e4; store-idc=alisg; store-country-code=cn; install_id=7126814077612115718; ttreq=1$065fc339e22f7da8844faf9adc4f19e5f267c6eb','x-gorgon': '04048032500189a229bdf66e04feefcf47d5ccc94e336871888b','x-khronos': '1660261382','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','content-length': '131','user-agent': 'okhttp/3.10.0.1',}
  data = f'email={email}&account_sdk_source=app&rules_version=v2&mix_mode=1&multi_login=1&type=31'
  rr = requests.post(url, headers=headers, data=data).text
  if 'success' in rr or ':"أنت ترسل عدداً كبيراً' in rr:
   link = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "Linked"}
   r = json.dumps(link, indent=2)
   return r
  else:
   error = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "UnLinked"}
   r = json.dumps(error, indent=2)
   return r
 def instagram(email: str) -> str:
  url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/" 
  headers = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
  'Content-Length': '300',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'csrftoken=hKY4T4Jn92sGMV5G1C4l5aLHFJCj8nlw; mid=ZMeYlwABAAGELM-9LSO1zrF5u8Cp; ig_did=C7D3C191-6CF5-4B33-87D3-3AF684749058; ig_nrcb=1; datr=l5jHZM5UonCRvcRXLh7oAHu8; dpr=3.0234789848327637',
  'Origin': 'https://www.instagram.com',
  'Referer': 'https://www.instagram.com/',
  'Sec-Ch-Prefers-Color-Scheme': 'dark',
  'Sec-Ch-Ua': '"Not)A;Brand";v="24","Chromium";v="116"',
  'Sec-Ch-Ua-Full-Version-List': '"Not)A;Brand";v="24.0.0.0","Chromium";v="116.0.5845.57"',
  'Sec-Ch-Ua-Mobile': '?0',
  'Sec-Ch-Ua-Platform': '"Linux"',
  'Sec-Ch-Ua-Platform-Version': '""',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
  'Viewport-Width': '891',
  'X-Asbd-Id': '129477',
  'X-Csrftoken': 'hKY4T4Jn92sGMV5G1C4l5aLHFJCj8nlw',
  'X-Ig-App-Id': '936619743392459',
  'X-Ig-Www-Claim': '0',
  'X-Instagram-Ajax': '1007930322',
  'X-Requested-With': 'XMLHttpRequest',} 
  data = {
  'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1690802386:AbFQALEEQgklqFeMg7cu0pgYsQU6h6w9vqXxAOoityr78RcirYB4uix/eXL4WeWUgNUFC5X+96z7qFuazy6OSp9r3FZacPWuEY2tV96P22ONLNN9avW+WZH3bfMME7yIZhzZhIVyIZtFvz/t2g==',
  'optIntoOneTap': 'false',
  'queryParams': '{}',
  'trustedDeviceRecords': '{}',
  'username': email,}
  r=requests.post(url,headers=headers,data=data).json()
  try:
   r=r['authenticated']
   if r == False:
    link = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "Linked"}
    r = json.dumps(link, indent=2)
    return r
   else:
    error = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "UnLinked"}
    r = json.dumps(error, indent=2)
    return r
  except:
   error = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "UnLinked"}
   r = json.dumps(error, indent=2)
   return r
 def facebook(email: str) -> str:
  url = "https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0"
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Content-Length': '86',
    'Content-Type': 'application/x-www-form-urlencoded',
     'Cookie': 'datr=tpjHZGUZdPrTrLAwHgR3YM5g; sb=tpjHZHLgQ7llmsxsMKEws_SW; m_pixel_ratio=3.0234789848327637; locale=ar_AR; wl_cbv=v2%3Bclient_version%3A2296%3Btimestamp%3A1690803637; vpd=v1%3B772x393x2.75; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcmVmPXdpemFyZCZwYWlwdj0wJmVhdj1BZmJBOUo0YjJSVXBUUDQwdTgzV1E5Sjloc3I4bFBIYTNfRnE2Nm5IeHZUQzYxOUt3S0pvUDZ1bDdGZFpIVDcxQ2hJIiwiaCI6Ii9ib29rbWFya3MvP3JlZj13aXphcmQmcGFpcHY9MCZlYXY9QWZiQTlKNGIyUlVwVFA0MHU4M1dROUo5aHNyOGxQSGEzX0ZxNjZuSHh2VEM2MTlLd0tKb1A2dWw3RmRaSFQ3MUNoSSIsInMiOiJtIn0%3D;sfiu=AYhuSuoPTb6V9sYVr7GgJeXso3hIbrq0WljP4XhWF3UrI7Jt14M3NOq4JIINkBMOQtVXuBYx3Wha-7G9Tk1rwjvQ7vK3nRGjQQdj1j9jWFQ4xltSy-pSXN3GH3UPhAF4j3JxN8ZNCSZNJx5_EUle29uMu41vyP84IZnsgFAjQvqLmS60qHJ3N4NkDmpqmt9VVmwGFuDTI9DJRAA1lyKyznN--ep_wua1HhDzhrsMgXW82H5cnCbigUYv_cYiu7pFXYM; wd=891x1750; fr=0ACEo2bBAyMlODmBv.AWU2EbpneQ6rGcVRE3JYBatI_6w.Bkx5i2._m.AAA.0.0.Bkx59M.AWUN6c-LXDs',
  'Origin': 'https://m.facebook.com',
  'Referer': 'https://m.facebook.com/login/identify',
  'Sec-Ch-Prefers-Color-Scheme': 'dark',
  'Sec-Ch-Ua': '"Not)A;Brand";v="24","Chromium";v="116"',
  'Sec-Ch-Ua-Full-Version-List': '"Not)A;Brand";v="24.0.0.0","Chromium";v="116.0.5845.57"',
  'Sec-Ch-Ua-Mobile': '?0',
  'Sec-Ch-Ua-Platform': '"Linux"',
  'Sec-Ch-Ua-Platform-Version': '""',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
  'Viewport-Width': '980',} 
  data = {
    'lsd': 'AVonPLm6YCY',
    'jazoest': '2936',
    'email': email,
    'did_submit': 'بحث',}
  r = requests.post(url, headers=headers, data=data)
  if "sfiu" in r.cookies:
   link = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "Linked"}
   r = json.dumps(link, indent=2)
   return r
  else:
   error = {
        "telegram": "@U_L_W",
        "email": email,
        "state": "UnLinked"}
   r = json.dumps(error, indent=2)
   return r
class username:
  def telegram(api_hash, api_id, username: str) -> str:
    client = TelegramClient('new_session', api_id, api_hash)
    client.start()
    try:
       requ = requests.get("https://fragment.com/username/" + username)
       if '<span class="tm-section-header-status tm-status-avail">Available</span>' in requ.text:
          buy = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "For sale"}
          sale = json.dumps(buy, indent=2)
          return sale
       result = client(CheckUsernameRequest(username=username))
       if result:
            good = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Available"}
            available = json.dumps(good, indent=2)
            return available
       else:
            bad = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Taken"}
            taken = json.dumps(bad, indent=2)
            return taken
    except errors.FloodWaitError as timb:
       block = {
        "telegram": "@U_L_W",
        "username": username,
        "state": f"Api_id , Api_hash has been blocked {timb.seconds} seconds"}
       soryy = json.dumps(block, indent=2)
       return soryy
    except errors.UsernameInvalidError:
       error = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Invalid"}
       kal = json.dumps(error, indent=2)
       return kal
    except errors.rpcbaseerrors.BadRequestError:
       ban = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Banned"}
       band = json.dumps(ban, indent=2)
       return band
  def instagram(username: str) -> str:
     error1 = '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}'
     error2 = '"errors": {"username":'
     error3 = '"code": "username_is_taken"'
     url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/" 
     headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,ar;q=0.8','Content-Length': '355','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'ig_did=66DD6740-1268-4A76-A2C6-92D61BC45F04; ig_nrcb=1; mid=ZEgT-AALAAG2b7smB_uP7Jz7IUWS; datr=9hNIZACGTQ-tVRYq4CICPxf3; shbid="19719\05446742327148\0541722535031:01f7b60c8f0042f9a16eb313c8dba10f30a180f327245ce9f7adbebeba7c2c7d71ad43e4"; shbts="1690999031\05446742327148\0541722535031:01f7ffdc1636ee3dd0c7d3fb9a03ce388560f9c4b5ce10ec0218cfd09da256d53ef384ff"; rur="RVA\05446742327148\0541722535119:01f797c6e602673917fcbac91543ad9215624fe741e3c7a8b61c3455278e9b411e87a15e"; dpr=0.8333333730697632; csrftoken=Ynep5hgYgjuIORIY2zaavXOvqMVxOe1Z','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/accounts/emailsignup/','Sec-Ch-Prefers-Color-Scheme': 'dark','Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"','Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.110", "Chromium";v="115.0.5790.110"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': '"Windows"','Sec-Ch-Ua-Platform-Version': '"10.0.0"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Viewport-Width': '963','X-Asbd-Id': '129477','X-Csrftoken': 'Ynep5hgYgjuIORIY2zaavXOvqMVxOe1Z','X-Ig-App-Id': '936619743392459','X-Ig-Www-Claim': 'hmac.AR1OWJkZTrxBHfaWEoLxPVuf8VUPLg0Ar6TOELbdIAtr9XIL','X-Instagram-Ajax': '1007955772','X-Requested-With': 'XMLHttpRequest',} 
     data = {'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1690999230:ARRQAG8T1iGFAA1WUH8DliVgYp0KFlyds01Li3k+DV/r89N3NNdjcqD5YyEwdOHAXUoJr6ZaEq7IvUxnI0Ij9SSzpvmpmO6nQ3eBTpTQ1r4svu708EaTgqalVFDMBYaO74DZWdZcdkWJA/Br','email': 'iam982933@gmail.com','first_name': 'ahmed','username': username,'client_id': 'ZEgT-AALAAG2b7smB_uP7Jz7IUWS','seamless_login_enabled': '1','opt_into_one_tap': 'false',}
     r = requests.post(url,headers=headers,data=data).text
     if error1 in r or error2 in r:
        ban = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Banned"}
        band = json.dumps(ban, indent=2)
        return band
     elif error3 in r:
        bad = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Taken"}
        taken = json.dumps(bad, indent=2)
        return taken
     else:
        good = {
        "telegram": "@U_L_W",
        "username": username,
        "state": "Available"}
        available = json.dumps(good, indent=2)
        return available
#def tiktok(username: str) -> str:
     