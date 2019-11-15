# Coded By Zed-Team
# Please Fork Dont Copy
# And Join My Channel : @Arch_TM
import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    os.system('pip install bs4')
try:
    from colorama import Fore,init
    init(autoreset=False)
except ModuleNotFoundError:
    os.system('pip install colorama')

def main():
    # Quesstion For count Follower
    try:
        count = int(input("Please Enter Follower(just number) : "))
    except TypeError or ValueError:
        print("Please Enter Just Number !")
        exit()
    # Open File Text
    address = str(input('Please Enter Your Name File Text : '))
    if address.endswith('.txt'):
        pass
        print(address)
    else:
        address = address + ".txt"
    user = ""
    try:
        with open(address,'r') as readfile:
            for i in readfile.readlines():
                user += i
            mylists = user.split('\n')
            c = 0
            status = ""
        
            for ii in mylists:
                
                c+=1
                req = requests.get(f"https://www.instagram.com/{ii}/")
                if req.status_code == 200:
                    status = "Checked ! (Not Good)"
                    soup = BeautifulSoup(req.text,'html.parser')
                    vale = str(soup.find('meta',attrs={'property':'og:description'}))
                    values = vale.split(' ')

                    try:
                        Followers = "".join(values[1])
                        Followers = Followers[9:]
                        if Followers.endswith("k"):
                            Followers = Followers + "000"
                            Followers = Followers.replace('.','')
                            Followers = Followers.replace('k','')
                        elif Followers.endswith('m'):
                            Followers = Followers + "000000"
                            Followers = Followers.replace('.','')
                            Followers = Followers.replace('m','')
                        try:
                            Followers= Followers.replace(',','')

                        except Exception:
                            pass
                        if int(Followers) >= count:
                            status = f"Good, username : {ii}"
                            with open('goodacc.txt','a') as writefile:
                                writefile.write(ii)
                                writefile.write('\n')
                    except Exception as e:
                        print(e)
                        continue
                else:
                    if req.status_code == 404:
                        status = Fore.RED + "Username Not Found !"
                    else:
                        status = "Connection Error"
                print(f'User[{c}] : {status}')
    except Exception:
        print("You Are Exit from Script!")
            


if __name__ == "__main__":
    print(Fore.GREEN + "User Checker Instagram V1 (Private)")
    print(Fore.GREEN + "       Coded By Zed-Team !\n")
    try:
        with open('goodacc.txt','x'):
            pass
    except Exception:
        pass
    main()
