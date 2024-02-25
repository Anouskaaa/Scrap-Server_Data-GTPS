import requests
import sys
from time import sleep


def httpResp(ip):
    http_server_dat_url = f"http://{ip}/growtopia/server_data.php"
    resp = requests.get(http_server_dat_url)
    sleep(2)

    if "server|" in resp.text:
        print(f"Get Data Succed: \n\n {resp.text}")
    elif "server|" != resp.text:
        print(f"No Server_data at http://{ip}/growtopia/server_data.php")
    

def httpsResp(ip):
    sleep(2)
    print("Fail to get http data, trying https")
    https_server_dat_url = f"https://{ip}/growtopia/server_data.php"
    resp = requests.get(https_server_dat_url,verify= False)
    if "server|" in resp.text:
        print(f"Getting https data : \n\n{resp.text}")
    else:
        print("No Server Data Here? Only These")
        print(f"\n\n{resp.text}")

def main():
    requests.packages.urllib3.disable_warnings()

    
    if len(sys.argv) != 2:
        print("Only 1 arguments can be inputed")
    arg1 = sys.argv[1]
    
    http_server_dat_url = f"http://{arg1}/growtopia/server_data.php"
    resp = requests.get(http_server_dat_url)        
    
    #Check if the site is blocked/Error
    #Status Code 200 == Is OK
    if resp.status_code == 200:
        try:
            httpResp(arg1)

        except:
            httpsResp(arg1)
    else:
        sleep(2)
        print(f"\nError Status Code : {resp.status_code}")
        print(resp.text)







if __name__ == "__main__":
    
    print("\nThis Scrapper Create By Sann\n")
    main()