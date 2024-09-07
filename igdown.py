import requests
import argparse

parse = argparse.ArgumentParser(description='instagramtools',usage="program.py [MODE]")

parse.add_argument('-U','--url')
parse.add_argument('-C','--code')
parse.add_argument('-S','--save')
parse.add_argument('mode')
# parse.add_argument('value',type=str,help=' - ')
arg = parse.parse_args()

# print(arg)

def DownloadReels(code,saveas=False):
    
    url = "https://www.instagram.com/api/graphql"

    payload = '__csr=g8O6PMgtlstaTROFrirqcLGHyWIyQGiyqp9ahkq9GqtRAz92eAHl4ypUG-QOVGAlWJyp9mi8heUCV8hA8cKozKqvyVbiABCBx11y8xeESUpxB004NODw90w0lBx22d0CzU0nUw1ZG0Bh4FsM9u1Sg0gswdeOm1fwxBwhU14poeU2_c0pa0hicxh045w0amy&lsd=2rW6RSUw1Z2nlKhvaIITDn&variables=%7B%22shortcode%22%3A%22'+code+'%22%7D&doc_id=6588824391221552'

    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 9; SM-S901N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'x-ig-app-id': "936619743392459",
    'Referer': "https://www.instagram.com",
    'Sec-Fetch-Site': "same-origin",
    'X-Fb-Lsd': "2rW6RSUw1Z2nlKhvaIITDn",
    'Sec-Fetch-Mode': "cors",
    'Cookie': ""
    }

    response = requests.post(url, data=payload, headers=headers).json()
    item = response['data']['xdt_api__v1__media__shortcode__web_info']['items']
    for x in item:
        judul = x['caption']['text']
        url = x['video_versions'][0]['url']
        print(url)
        if saveas:
            response = requests.get(url,stream=True)
            with open(saveas,'wb') as file:
                for x in response.iter_content(chunk_size=1000):
                    file.write(x)
                file.close()

if arg.mode in ['down','download']:
    if arg.code:
        DownloadReels(arg.code,saveas=arg.save) 