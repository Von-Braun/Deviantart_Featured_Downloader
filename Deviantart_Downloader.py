import urllib,os,requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style

init()
os.system('cls')
username=raw_input('Enter Username: ')
uniform_resource_locater="http://"+username+".deviantart.com"

def download_image(url,name):
    if not os.path.exists(os.getcwd()+ '\\'+(name+'.jpg')):
        urllib.urlretrieve(url,name+'.jpg')
        state = Fore.GREEN+'Downloaded'+Fore.WHITE
    else:
        state= Fore.YELLOW+'Already Downloaded'+Fore.WHITE
    return state

def trade_spider(): 
    page = 0
    got_something=True
    newpath = os.getcwd()+ '\\'+'USERS'+ '\\'+username
    if not os.path.exists(newpath): 
        os.makedirs(newpath)
    oldpath = os.getcwd()
    os.chdir(newpath)
    while True:
        if got_something:
            got_something=False
        else:
            print 'Done'
            break
        url = uniform_resource_locater+"/gallery/?offset=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('span', {'class': 'thumb'}):
            href = link.get('data-super-full-img')
            if href!=None: 
                got_something = True
                print 'pg:'+str(page/24)+':'+href.split('/')[-1].split('.')[0],
                state=Fore.RED+'An unknown error occurred: '+Fore.WHITE
                try:
                    state = download_image(href,href.split('/')[-1].split('.')[0])
                except Exception as e:
                    state+=e
                print state
        page+=24
    os.chdir(oldpath)

trade_spider()
