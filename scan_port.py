import socket
import requests
import json
from tabulate import tabulate
from colorama import Fore, Style, init
print(r"""
                                                                                                        
                                                                                                        
YYYYYYY       YYYYYYYUUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS UUUUUUUU     UUUUUUUUFFFFFFFFFFFFFFFFFFFFFF
Y:::::Y       Y:::::YU::::::U     U::::::U SS:::::::::::::::SU::::::U     U::::::UF::::::::::::::::::::F
Y:::::Y       Y:::::YU::::::U     U::::::US:::::SSSSSS::::::SU::::::U     U::::::UF::::::::::::::::::::F
Y::::::Y     Y::::::YUU:::::U     U:::::UUS:::::S     SSSSSSSUU:::::U     U:::::UUFF::::::FFFFFFFFF::::F
YYY:::::Y   Y:::::YYY U:::::U     U:::::U S:::::S             U:::::U     U:::::U   F:::::F       FFFFFF
   Y:::::Y Y:::::Y    U:::::D     D:::::U S:::::S             U:::::D     D:::::U   F:::::F             
    Y:::::Y:::::Y     U:::::D     D:::::U  S::::SSSS          U:::::D     D:::::U   F::::::FFFFFFFFFF   
     Y:::::::::Y      U:::::D     D:::::U   SS::::::SSSSS     U:::::D     D:::::U   F:::::::::::::::F   
      Y:::::::Y       U:::::D     D:::::U     SSS::::::::SS   U:::::D     D:::::U   F:::::::::::::::F   
       Y:::::Y        U:::::D     D:::::U        SSSSSS::::S  U:::::D     D:::::U   F::::::FFFFFFFFFF   
       Y:::::Y        U:::::D     D:::::U             S:::::S U:::::D     D:::::U   F:::::F             
       Y:::::Y        U::::::U   U::::::U             S:::::S U::::::U   U::::::U   F:::::F             
       Y:::::Y        U:::::::UUU:::::::U SSSSSSS     S:::::S U:::::::UUU:::::::U FF:::::::FF           
    YYYY:::::YYYY      UU:::::::::::::UU  S::::::SSSSSS:::::S  UU:::::::::::::UU  F::::::::FF           
    Y:::::::::::Y        UU:::::::::UU    S:::::::::::::::SS     UU:::::::::UU    F::::::::FF           
    YYYYYYYYYYYYY          UUUUUUUUU       SSSSSSSSSSSSSSS         UUUUUUUUU      FFFFFFFFFFF   """)

print("\n****************************************************************")
print("\n* Copyright of Muh Yusuf, 2024                              *")
print("\n****************************************************************")

# Initialize colorama for colored output
init(autoreset=True)

def get_ip_info(ip_address):
    try:
        url = f'https://ipapi.co/{ip_address}/json/'
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching IP information: {e}")
        return None

def print_ip_info(ip_info):
    if ip_info:
        headers = ["Field", "Value"]
        table_data = [[k, v] for k, v in ip_info.items()]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print(f"{Fore.YELLOW}No IP information available.")

def main():
    while True:
        print(f"\n{Fore.CYAN}=== IP Geolocation Tool ===")
        choice = input("Enter 1 for hostname, 2 for IP address, or 'q' to quit: ").lower()

        if choice == 'q':
            print(f"{Fore.GREEN}Thank you for using the IP Geolocation Tool. Goodbye!")
            break

        if choice not in ['1', '2']:
            print(f"{Fore.RED}Invalid choice. Please try again.")
            continue

        try:
            if choice == '1':
                hostname = input("Enter hostname: ")
                ip_address = socket.gethostbyname(hostname)
                print(f"{Fore.GREEN}Resolved IP address: {ip_address}")
            else:
                ip_address = input("Enter IP address: ")

            ip_info = get_ip_info(ip_address)
            print_ip_info(ip_info)

            if ip_info and 'latitude' in ip_info and 'longitude' in ip_info:
                map_url = f"https://www.google.com/maps?q={ip_info['latitude']},{ip_info['longitude']}"
                print(f"\n{Fore.CYAN}View location on Google Maps: {map_url}")

        except socket.gaierror:
            print(f"{Fore.RED}Error: Unable to resolve hostname. Please check and try again.")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
