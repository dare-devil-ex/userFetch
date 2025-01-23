from requests import get, exceptions
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    if get("https://google.com").status_code == 200:
        print("Internet connected!")
        sl(0.6)
        s("cls")
except:
    s("cls")
    print("Connect to the internet :/")

valid = 0
invalid = 0

def wkaie(url):
    global valid, invalid
    try:
        resp = get(url, timeout=10).status_code
        if resp == 200:
            valid += 1
            print(f"{valid}: {url}")
            with open(f"{uName}.txt", "a+") as wkaie:
                wkaie.write(f"{url}\n")
        else:
            invalid += 1
    except exceptions.Timeout:
        pass
    except Exception as e:
        pass

urls = []
try:
    uName = input("Enter the username: ")
    with open("./garage/links.txt", "r") as f:
        with open("./garage/links.txt", "r") as f:
            for line in f:
                line = line.strip()
                if "github.com" in line:
                    url = line.replace("$username", uName.replace("_", "-"))
                elif "facebook.com" in line:
                    url = line.replace("$username", uName.replace("_", "."))
                elif "instagram.com" in line:
                    url = line.replace("$username", uName.replace("_", ""))
                else:
                    url = line.replace("$username", uName)
                urls.append(url)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(wkaie, url) for url in urls]
        for future in as_completed(futures):
            pass
    print("Scanning completed")
    print(f"{valid} valid URLs found!\n{invalid} invalid URLs found.")
    
except:
    print("OOPS! something went wrong..")
