import requests
import sys
from time import sleep


requests.packages.urllib3.disable_warnings()
def main():

    if len(sys.argv) != 2:
        print("Only 1 arguments can be inputed")
    arg1 = sys.argv[1]
        
            

    try:
        http_server_dat_url = f"http://{arg1}/growtopia/server_data.php"
        resp = requests.get(http_server_dat_url)
        sleep(2)
        if resp.status_code == 200:
            if "server|" in resp.text:
                print(f"Get Data Succed: \n\n {resp.text}")
            elif "server|" != resp.text:
                print(f"No Server_data at http://{arg1}/growtopia/server_data.php")
    except:
        sleep(2)
        print("Fail to get http data, trying https")
        https_server_dat_url = f"https://{arg1}/growtopia/server_data.php"
        resp = requests.get(https_server_dat_url,verify= False)
        if "server|" in resp.text:
            print(f"Getting https data : \n\n{resp.text}")
        else:
            print("No Server Data Here? Only These")
            print(f"\n\n{resp.text}")






if __name__ == "__main__":
    print("\nThis Scrapper Create By Sann\n")
    main()