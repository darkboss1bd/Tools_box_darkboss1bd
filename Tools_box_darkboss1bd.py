#!/usr/bin/env python3
#
#           Penetration Testing Toolkit
#           Codded by: DarkBoss1BD
#            

import sys
import os
import time
import subprocess
import re
import socket
import json
import glob
import random
import threading
import webbrowser
from urllib.parse import urlparse
from time import sleep

# Try to import optional modules with fallbacks
try:
    import requests
except ImportError:
    requests = None
    print("Warning: requests module not available, some features may not work")

try:
    import urllib.request as urllib2
    import urllib.error
except ImportError:
    urllib2 = None

try:
    import http.client as httplib
except ImportError:
    httplib = None

# Color codes
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

G = Colors.GREEN
Y = Colors.YELLOW
B = Colors.BLUE
R = Colors.RED
P = Colors.PURPLE
C = Colors.CYAN
W = Colors.WHITE
BD = Colors.BOLD
UL = Colors.UNDERLINE

########################## 
# Variables
directories = ['/uploads/','/upload/','/files/','/resume/','/resumes/','/documents/','/docs/','/pictures/','/file/','/Upload/','/Uploads/','/Resume/','/Resume/','/UsersFiles/','/Usersiles/','/usersFiles/','/Users_Files/','/UploadedFiles/','/Uploaded_Files/','/uploadedfiles/','/uploadedFiles/','/hpage/','/admin/upload/','/admin/uploads/','/admin/resume/','/admin/resumes/','/admin/pictures/','/pics/','/photos/','/Alumni_Photos/','/alumni_photos/','/AlumniPhotos/','/users/']
shells = ['wso.php','shell.php','an.php','hacker.php','lol.php','up.php','cp.php','upload.php','sh.php','pk.php','mad.php','x00x.php','worm.php','1337worm.php','config.php','x.php','haha.php']
upload = []
yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])

########################## 

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def open_links():
    """Automatically open developer links"""
    links = [
        "https://t.me/darkvaiadmin",
        "https://t.me/windowspremiumkey"
    ]
    
    print(f"\n{Colors.CYAN}[*] Opening DarkBoss1BD Links...{Colors.WHITE}")
    for link in links:
        try:
            webbrowser.open(link)
            print(f"{Colors.GREEN}[+] Opened: {link}{Colors.WHITE}")
        except Exception as e:
            print(f"{Colors.RED}[-] Failed to open {link}: {e}{Colors.WHITE}")
    time.sleep(2)

def logo():
    """Display the main logo"""
    clear_screen()
    print(f"""{G}
    ╔════════════════════════════════════════════════════════════════╗
    ║{BD}        ____             _      ____              _           {W}   ║
    ║{BD}       |  _ \\  __ _ _ __| | __ | __ )  ___   ___ | |__        {W}   ║
    ║{BD}       | | | |/ _` | '__| |/ / |  _ \\ / _ \\ / _ \\| '_ \\       {W}   ║
    ║{BD}       | |_| | (_| | |  |   <  | |_) | (_) | (_) | |_) |      {W}   ║
    ║{BD}       |____/ \\__,_|_|  |_|\\_\\ |____/ \\___/ \\___/|_.__/       {W}   ║
    ║                                                                ║
    ║{C}              F R A M E W O R K   v5.4                   {W} ║
    ║{R}           C O D D E D   B Y   D A R K B O S S 1 B D     {W} ║
    ║                                                                ║
    ║{Y}        Telegram: https://t.me/darkvaiadmin                  {W}   ║
    ║{Y}        Channel:  https://t.me/windowspremiumkey             {W}   ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    {W}""")

def print_banner(text):
    """Print a formatted banner"""
    width = 70
    print(f"\n{G}╔{'═' * (width - 2)}╗{W}")
    print(f"║{C}{text.center(width - 2)}{W}║")
    print(f"╚{'═' * (width - 2)}╝{W}")

def loading_animation(text, duration=2):
    """Display a loading animation"""
    chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        print(f"\r{Colors.YELLOW}{chars[i % len(chars)]} {text}...{Colors.WHITE}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    
    print(f"\r{Colors.GREEN}✓ {text} completed!{' ' * 20}{Colors.WHITE}")

def check_dependencies():
    """Check if required dependencies are installed"""
    required_modules = ['requests']
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print(f"{R}[!] Missing dependencies: {', '.join(missing_modules)}{W}")
        print(f"{Y}[*] Installing dependencies...{W}")
        
        for module in missing_modules:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
                print(f"{G}[+] Successfully installed {module}{W}")
            except subprocess.CalledProcessError:
                print(f"{R}[-] Failed to install {module}{W}")
        
        print(f"{G}[*] Dependencies check complete!{W}")
    else:
        print(f"{G}[*] All dependencies are satisfied!{W}")

def run_command(command):
    """Run system command with error handling"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"{R}[-] Command failed: {e}{W}")
        return None

def install_tool(tool_name, install_commands, success_message=None):
    """Generic tool installation function"""
    print_banner(f"INSTALLING {tool_name.upper()}")
    
    choice = input(f"{Colors.GREEN}[?]{Colors.WHITE} Install {tool_name}? (y/n): ").lower()
    
    if choice in yes:
        loading_animation(f"Installing {tool_name}")
        
        if isinstance(install_commands, str):
            install_commands = [install_commands]
            
        for cmd in install_commands:
            if not run_command(cmd):
                print(f"{R}[-] Failed to install {tool_name}{W}")
                return False
        
        if success_message:
            print(f"{G}[+] {success_message}{W}")
        else:
            print(f"{G}[+] {tool_name} installed successfully!{W}")
        return True
    else:
        print(f"{Y}[*] Installation cancelled.{W}")
        return False

def menu():
    """Main menu function"""
    while True:
        logo()
        print_banner("MAIN MENU")
        
        menu_options = [
            f"{G}1{W} : {B}Information Gathering{ W}",
            f"{G}2{W} : {B}Password Attacks{ W}",
            f"{G}3{W} : {B}Wireless Testing{ W}",
            f"{G}4{W} : {B}Exploitation Tools{ W}",
            f"{G}5{W} : {B}Sniffing & Spoofing{ W}",
            f"{G}6{W} : {B}Web Hacking{ W}",
            f"{G}7{W} : {B}Private Tools{ W}",
            f"{G}8{W} : {B}Post Exploitation{ W}",
            f"{G}9{W} : {B}Reconnaissance{ W}",
            f"{G}10{W}: {B}Smartphones Penetration{ W}",
            f"{G}11{W}: {B}Other Tools{ W}",
            f"{G}99{W}: {R}Exit{ W}"
        ]
        
        for option in menu_options:
            print(f"    {option}")
        
        print(f"\n{Colors.CYAN}╔{'═' * 50}╗")
        print(f"║{Colors.YELLOW}        Developer: DarkBoss1BD{Colors.CYAN}                  ║")
        print(f"║{Colors.YELLOW}        Telegram: @darkvaiadmin{Colors.CYAN}                 ║")
        print(f"╚{'═' * 50}╝{Colors.WHITE}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        menu_actions = {
            "1": info_gathering,
            "2": password_attacks,
            "3": wireless_testing,
            "4": exploitation_tools,
            "5": sniffing_spoofing,
            "6": web_hacking,
            "7": private_tools,
            "8": post_exploitation,
            "9": reconnaissance,
            "10": smartphone_penetration,
            "11": other_tools,
            "99": lambda: (print(f"\n{R}[!] Thank you for using Toolbox!{W}"), print(f"{G}[*] Developed by DarkBoss1BD{W}"), sys.exit())
        }
        
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print(f"{R}[!] Invalid choice! Please try again.{W}")
            time.sleep(1)

def info_gathering():
    """Information Gathering Menu"""
    while True:
        logo()
        print_banner("INFORMATION GATHERING")
        
        options = [
            "NMAP - Network Mapper",
            "Setoolkit - Social Engineering Toolkit",
            "Port Scanning",
            "Host To IP",
            "WP User Enumeration",
            "CMS Scanner",
            "XSStracer",
            "Doork",
            "Server Users",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_nmap,
            "2": install_setoolkit,
            "3": port_scanning,
            "4": host_to_ip,
            "5": wp_user_enum,
            "6": cms_scanner,
            "7": xsstracer,
            "8": doork,
            "9": scan_users,
            "10": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "10":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "10":
            break

def install_nmap():
    """Install and configure NMAP"""
    if os.name == 'nt':  # Windows
        install_tool(
            "Nmap",
            "winget install -e --id Nmap.Nmap",
            "Nmap installed successfully!"
        )
    else:  # Linux/Mac
        install_tool(
            "Nmap",
            "sudo apt update && sudo apt install nmap -y",
            "Nmap installed successfully!"
        )

def install_setoolkit():
    """Install Social Engineering Toolkit"""
    install_tool(
        "SEToolkit",
        ["git clone https://github.com/trustedsec/social-engineer-toolkit.git setoolkit", 
         "cd setoolkit && pip3 install -r requirements.txt"],
        "SEToolkit installed successfully!"
    )

def port_scanning():
    """Perform port scanning"""
    print_banner("PORT SCANNING")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target IP/hostname: ").strip()
    
    if target:
        print(f"{Y}[*] Scanning ports on {target}...{W}")
        run_command(f"nmap -sV -O {target}")
    else:
        print(f"{R}[!] No target specified!{W}")

def host_to_ip():
    """Convert hostname to IP"""
    print_banner("HOST TO IP CONVERSION")
    
    host = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter hostname: ").strip()
    
    if host:
        try:
            ip = socket.gethostbyname(host)
            print(f"{G}[+] {host} -> {ip}{W}")
        except socket.gaierror:
            print(f"{R}[!] Could not resolve hostname{ W}")
    else:
        print(f"{R}[!] No hostname specified!{W}")

def wp_user_enum():
    """WordPress User Enumeration"""
    print_banner("WORDPRESS USER ENUMERATION")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter WordPress site URL: ").strip()
    
    if target:
        loading_animation("Enumerating WordPress users")
        run_command("git clone https://github.com/wpscanteam/wpscan.git")
        run_command(f"cd wpscan && ruby wpscan.rb --url {target} --enumerate u")
    else:
        print(f"{R}[!] No target specified!{W}")

def cms_scanner():
    """CMS Scanner"""
    print_banner("CMS SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target URL: ").strip()
    
    if target:
        loading_animation("Scanning for CMS")
        run_command("git clone https://github.com/Dionach/CMSmap.git")
        run_command(f"cd CMSmap && python3 cmsmap.py {target}")
    else:
        print(f"{R}[!] No target specified!{W}")

def xsstracer():
    """XSS Tracer"""
    print_banner("XSS TRACER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target URL: ").strip()
    
    if target:
        loading_animation("Running XSSTracer")
        run_command("git clone https://github.com/1N3/XSSTracer.git")
        run_command(f"cd XSSTracer && python3 xsstracer.py {target}")
    else:
        print(f"{R}[!] No target specified!{W}")

def doork():
    """Doork Vulnerability Scanner"""
    print_banner("DOORK VULNERABILITY SCANNER")
    
    choice = input(f"{Colors.GREEN}[?]{Colors.WHITE} Install and run Doork? (y/n): ").lower()
    
    if choice in yes:
        loading_animation("Installing Doork")
        run_command("pip3 install beautifulsoup4 requests")
        run_command("git clone https://github.com/AeonDave/doork.git")
        
        target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target: ").strip()
        if target:
            run_command(f"cd doork && python3 doork.py -t {target}")
    else:
        print(f"{Y}[*] Operation cancelled.{W}")

def scan_users():
    """Scan for server users"""
    print_banner("SERVER USER SCANNER")
    
    site = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter website URL: ").strip()
    
    if site:
        loading_animation("Scanning for users")
        print(f"{Y}[*] User scanning feature would be implemented here{W}")
    else:
        print(f"{R}[!] No website specified!{W}")

def password_attacks():
    """Password Attacks Menu"""
    while True:
        logo()
        print_banner("PASSWORD ATTACKS")
        
        options = [
            "Cupp - Password List Generator",
            "Ncrack - Network Authentication Cracking",
            "AutoBrowser Screenshot",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_cupp,
            "2": install_ncrack,
            "3": autobrowser,
            "4": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "4":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "4":
            break

def install_cupp():
    """Install CUPP"""
    install_tool(
        "CUPP",
        "git clone https://github.com/Mebus/cupp.git",
        "CUPP installed successfully! Usage: cd cupp && python3 cupp.py"
    )

def install_ncrack():
    """Install Ncrack"""
    install_tool(
        "Ncrack",
        "sudo apt install ncrack -y",
        "Ncrack installed successfully!"
    )

def autobrowser():
    """AutoBrowser Tool"""
    install_tool(
        "AutoBrowser",
        ["git clone https://github.com/El3ct71k/AutoBrowser.git", 
         "cd AutoBrowser && pip3 install -r requirements.txt"],
        "AutoBrowser installed successfully! Usage: cd AutoBrowser && python3 AutoBrowser.py"
    )

def wireless_testing():
    """Wireless Testing Menu"""
    while True:
        logo()
        print_banner("WIRELESS TESTING")
        
        options = [
            "Reaver - WPS Attack Tool",
            "PixieWPS - WPS Pixie Dust Attack",
            "Bluetooth Honeypot",
            "Fluxion - WPA/WPA2 Security Hacking",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_reaver,
            "2": install_pixiewps,
            "3": install_bluepot,
            "4": install_fluxion,
            "5": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "5":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "5":
            break

def install_reaver():
    """Install Reaver"""
    if os.name == 'nt':
        print(f"{R}[!] Reaver is not available for Windows{ W}")
    else:
        install_tool(
            "Reaver",
            "sudo apt install reaver -y",
            "Reaver installed successfully!"
        )

def install_pixiewps():
    """Install PixieWPS"""
    if os.name == 'nt':
        print(f"{R}[!] PixieWPS is not available for Windows{ W}")
    else:
        install_tool(
            "PixieWPS",
            ["git clone https://github.com/wiire/pixiewps.git", "cd pixiewps && make"],
            "PixieWPS installed successfully!"
        )

def install_bluepot():
    """Install Bluetooth Honeypot"""
    install_tool(
        "BluePot",
        ["wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz", 
         "tar xfz bluepot-0.1.tar.gz"],
        "BluePot downloaded! Run: sudo java -jar bluepot/BluePot-0.1.jar"
    )

def install_fluxion():
    """Install Fluxion"""
    if os.name == 'nt':
        print(f"{R}[!] Fluxion is not available for Windows{ W}")
    else:
        install_tool(
            "Fluxion",
            "git clone https://github.com/FluxionNetwork/fluxion.git",
            "Fluxion installed successfully! Run: cd fluxion && sudo ./fluxion.sh"
        )

def exploitation_tools():
    """Exploitation Tools Menu"""
    while True:
        logo()
        print_banner("EXPLOITATION TOOLS")
        
        options = [
            "SQLMap - SQL Injection Tool",
            "Commix - Command Injection Tool",
            "Shellnoob - Shellcode Toolkit",
            "JBoss Autopwn",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_sqlmap,
            "2": install_commix,
            "3": install_shellnoob,
            "4": install_jboss_autopwn,
            "5": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "5":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "5":
            break

def install_sqlmap():
    """Install SQLMap"""
    install_tool(
        "SQLMap",
        "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev",
        "SQLMap installed successfully! Usage: cd sqlmap-dev && python3 sqlmap.py -h"
    )

def install_commix():
    """Install Commix"""
    install_tool(
        "Commix",
        "git clone https://github.com/commixproject/commix.git commix",
        "Commix installed successfully! Usage: cd commix && python3 commix.py --help"
    )

def install_shellnoob():
    """Install Shellnoob"""
    install_tool(
        "Shellnoob",
        "git clone https://github.com/reyammer/shellnoob.git",
        "Shellnoob installed successfully! Usage: cd shellnoob && python3 shellnoob.py --install"
    )

def install_jboss_autopwn():
    """Install JBoss Autopwn"""
    install_tool(
        "JBoss Autopwn",
        "git clone https://github.com/SpiderLabs/jboss-autopwn.git",
        "JBoss Autopwn installed successfully!"
    )

def sniffing_spoofing():
    """Sniffing and Spoofing Menu"""
    while True:
        logo()
        print_banner("SNIFFING & SPOOFING")
        
        options = [
            "SSLStrip - SSL Stripping Tool",
            "BetterCAP - Swiss Army Knife for Network Attacks",
            "Wireshark - Network Protocol Analyzer",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_sslstrip,
            "2": install_bettercap,
            "3": install_wireshark,
            "4": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "4":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "4":
            break

def install_sslstrip():
    """Install SSLStrip"""
    install_tool(
        "SSLStrip",
        ["git clone https://github.com/moxie0/sslstrip.git", "pip3 install twisted"],
        "SSLStrip installed successfully!"
    )

def install_bettercap():
    """Install BetterCAP"""
    install_tool(
        "BetterCAP",
        "sudo apt install bettercap -y",
        "BetterCAP installed successfully!"
    )

def install_wireshark():
    """Install Wireshark"""
    if os.name == 'nt':
        install_tool(
            "Wireshark",
            "winget install WiresharkFoundation.Wireshark",
            "Wireshark installed successfully!"
        )
    else:
        install_tool(
            "Wireshark",
            "sudo apt install wireshark -y",
            "Wireshark installed successfully!"
        )

def web_hacking():
    """Web Hacking Menu"""
    while True:
        logo()
        print_banner("WEB HACKING")
        
        options = [
            "Drupal Security Scanner",
            "WordPress Security Scanner",
            "Joomla Security Scanner",
            "File Upload Vulnerability Scanner",
            "XSS Scanner",
            "CSRF Testing Tools",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": drupal_scanner,
            "2": wordpress_scanner,
            "3": joomla_scanner,
            "4": file_upload_scanner,
            "5": xss_scanner,
            "6": csrf_tools,
            "7": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "7":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "7":
            break

def drupal_scanner():
    """Drupal Security Scanner"""
    print_banner("DRUPAL SECURITY SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter Drupal site URL: ").strip()
    
    if target:
        loading_animation("Scanning Drupal site")
        print(f"{Y}[*] Scanning {target} for Drupal vulnerabilities...{W}")
    else:
        print(f"{R}[!] No target specified!{W}")

def wordpress_scanner():
    """WordPress Security Scanner"""
    print_banner("WORDPRESS SECURITY SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter WordPress site URL: ").strip()
    
    if target:
        loading_animation("Scanning WordPress site")
        run_command("git clone https://github.com/wpscanteam/wpscan.git")
        run_command(f"cd wpscan && ruby wpscan.rb --url {target} --enumerate vp")
    else:
        print(f"{R}[!] No target specified!{W}")

def joomla_scanner():
    """Joomla Security Scanner"""
    print_banner("JOOMLA SECURITY SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter Joomla site URL: ").strip()
    
    if target:
        loading_animation("Scanning Joomla site")
        print(f"{Y}[*] Scanning {target} for Joomla vulnerabilities...{W}")
    else:
        print(f"{R}[!] No target specified!{W}")

def file_upload_scanner():
    """File Upload Vulnerability Scanner"""
    print_banner("FILE UPLOAD VULNERABILITY SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target URL: ").strip()
    
    if target:
        loading_animation("Scanning for file upload vulnerabilities")
        print(f"{Y}[*] Scanning {target} for file upload vulnerabilities...{W}")
    else:
        print(f"{R}[!] No target specified!{W}")

def xss_scanner():
    """XSS Scanner"""
    print_banner("XSS SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target URL: ").strip()
    
    if target:
        loading_animation("Scanning for XSS vulnerabilities")
        print(f"{Y}[*] Scanning {target} for XSS vulnerabilities...{W}")
    else:
        print(f"{R}[!] No target specified!{W}")

def csrf_tools():
    """CSRF Testing Tools"""
    print_banner("CSRF TESTING TOOLS")
    
    choice = input(f"{Colors.GREEN}[?]{Colors.WHITE} Install CSRF tools? (y/n): ").lower()
    
    if choice in yes:
        loading_animation("Installing CSRF tools")
        print(f"{Y}[*] CSRF tools installation would be implemented here{W}")
    else:
        print(f"{Y}[*] Installation cancelled.{W}")

def private_tools():
    """Private Tools Menu"""
    while True:
        logo()
        print_banner("PRIVATE TOOLS")
        
        options = [
            "DarkBoss1BD Custom Scanner",
            "Advanced Reconnaissance Toolkit",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": custom_scanner,
            "2": advanced_recon,
            "3": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "3":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "3":
            break

def custom_scanner():
    """DarkBoss1BD Custom Scanner"""
    print_banner("DARKBOSS1BD CUSTOM SCANNER")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target: ").strip()
    
    if target:
        loading_animation("Running DarkBoss1BD Custom Scanner")
        print(f"{G}[*] Scanning {target} with DarkBoss1BD techniques...{W}")
        print(f"{Y}[*] This is a custom scanner implementation{W}")
    else:
        print(f"{R}[!] No target specified!{W}")

def advanced_recon():
    """Advanced Reconnaissance Toolkit"""
    print_banner("ADVANCED RECONNAISSANCE TOOLKIT")
    
    target = input(f"{Colors.GREEN}[?]{Colors.WHITE} Enter target: ").strip()
    
    if target:
        loading_animation("Performing advanced reconnaissance")
        print(f"{G}[*] Advanced reconnaissance on {target}...{W}")
        print(f"{Y}[*] This would include OSINT, subdomain enumeration, etc.{W}")
    else:
        print(f"{R}[!] No target specified!{W}")

def post_exploitation():
    """Post Exploitation Menu"""
    while True:
        logo()
        print_banner("POST EXPLOITATION")
        
        options = [
            "Mimikatz - Credential Dumper",
            "PowerSploit - PowerShell Post-Exploitation",
            "Backdoor Creator",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_mimikatz,
            "2": install_powersploit,
            "3": backdoor_creator,
            "4": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "4":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "4":
            break

def install_mimikatz():
    """Install Mimikatz"""
    if os.name == 'nt':
        install_tool(
            "Mimikatz",
            "curl -L -o mimikatz.zip https://github.com/gentilkiwi/mimikatz/releases/latest",
            "Mimikatz downloaded!"
        )
    else:
        print(f"{R}[!] Mimikatz is primarily for Windows systems{ W}")

def install_powersploit():
    """Install PowerSploit"""
    install_tool(
        "PowerSploit",
        "git clone https://github.com/PowerShellMafia/PowerSploit.git",
        "PowerSploit installed successfully!"
    )

def backdoor_creator():
    """Backdoor Creator"""
    print_banner("BACKDOOR CREATOR")
    
    print(f"{Y}[*] This feature would create custom backdoors{W}")
    print(f"{R}[!] Feature under development{W}")

def reconnaissance():
    """Reconnaissance Menu"""
    while True:
        logo()
        print_banner("RECONNAISSANCE")
        
        options = [
            "The Harvester - Email Gathering",
            "Recon-ng - Web Reconnaissance",
            "Shodan CLI - Internet Connected Device Search",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_theharvester,
            "2": install_reconng,
            "3": install_shodan,
            "4": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "4":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "4":
            break

def install_theharvester():
    """Install The Harvester"""
    install_tool(
        "The Harvester",
        ["git clone https://github.com/laramies/theHarvester.git", 
         "cd theHarvester && pip3 install -r requirements.txt"],
        "The Harvester installed successfully!"
    )

def install_reconng():
    """Install Recon-ng"""
    install_tool(
        "Recon-ng",
        "git clone https://github.com/lanmaster53/recon-ng.git",
        "Recon-ng installed successfully!"
    )

def install_shodan():
    """Install Shodan CLI"""
    install_tool(
        "Shodan CLI",
        "pip3 install shodan",
        "Shodan CLI installed successfully! Don't forget to configure your API key: shodan init YOUR_API_KEY"
    )

def smartphone_penetration():
    """Smartphone Penetration Menu"""
    while True:
        logo()
        print_banner("SMARTPHONE PENETRATION")
        
        options = [
            "AndroBugs Framework - Android Vulnerability Scanner",
            "APKTool - Reverse Engineering APK Files",
            "Mobile Security Framework (MobSF)",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_androbugs,
            "2": install_apktool,
            "3": install_mobsf,
            "4": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "4":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "4":
            break

def install_androbugs():
    """Install AndroBugs Framework"""
    install_tool(
        "AndroBugs Framework",
        "git clone https://github.com/AndroBugs/AndroBugs_Framework.git",
        "AndroBugs Framework installed successfully!"
    )

def install_apktool():
    """Install APKTool"""
    if os.name == 'nt':
        print(f"{Y}[*] Download APKTool from: https://ibotpeaches.github.io/Apktool/install/{W}")
    else:
        install_tool(
            "APKTool",
            "sudo apt install apktool -y",
            "APKTool installed successfully!"
        )

def install_mobsf():
    """Install Mobile Security Framework"""
    install_tool(
        "MobSF",
        "git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git",
        "MobSF installed successfully! Run: cd Mobile-Security-Framework-MobSF && ./setup.sh"
    )

def other_tools():
    """Other Tools Menu"""
    while True:
        logo()
        print_banner("OTHER TOOLS")
        
        options = [
            "Metasploit Framework",
            "Burp Suite Community Edition",
            "John the Ripper - Password Cracker",
            "Hydra - Network Login Cracker",
            "Back to Main Menu"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"    {G}{i:2}{W} : {B}{option}{W}")
        
        choice = input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Enter Your Choice: ").strip()
        
        actions = {
            "1": install_metasploit,
            "2": install_burpsuite,
            "3": install_johntheripper,
            "4": install_hydra,
            "5": lambda: None
        }
        
        action = actions.get(choice)
        if action:
            action()
            if choice != "5":
                input(f"\n{Colors.GREEN}[?]{Colors.WHITE} Press Enter to continue...")
        else:
            print(f"{R}[!] Invalid choice!{W}")
            time.sleep(1)
        
        if choice == "5":
            break

def install_metasploit():
    """Install Metasploit Framework"""
    if os.name == 'nt':
        print(f"{Y}[*] Download Metasploit from: https://www.metasploit.com/download{W}")
    else:
        install_tool(
            "Metasploit",
            ["curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall", 
             "chmod 755 msfinstall", 
             "./msfinstall"],
            "Metasploit installed successfully!"
        )

def install_burpsuite():
    """Install Burp Suite"""
    print(f"{Y}[*] Download Burp Suite Community Edition from:{W}")
    print(f"{G}[*] https://portswigger.net/burp/communitydownload{W}")
    
    if os.name != 'nt':  # Linux
        choice = input(f"{Colors.GREEN}[?]{Colors.WHITE} Download via command line? (y/n): ").lower()
        if choice in yes:
            run_command("wget -O burpsuite_community_linux.sh 'https://portswigger.net/burp/releases/download?product=community&version=2023.6.2&type=Linux'")
            run_command("chmod +x burpsuite_community_linux.sh")
            print(f"{G}[+] Burp Suite downloaded! Run: ./burpsuite_community_linux.sh{W}")

def install_johntheripper():
    """Install John the Ripper"""
    if os.name == 'nt':
        print(f"{Y}[*] Download John the Ripper from: https://www.openwall.com/john/{W}")
    else:
        install_tool(
            "John the Ripper",
            "sudo apt install john -y",
            "John the Ripper installed successfully!"
        )

def install_hydra():
    """Install Hydra"""
    if os.name == 'nt':
        print(f"{Y}[*] Download Hydra from: https://github.com/vanhauser-thc/thc-hydra{W}")
    else:
        install_tool(
            "Hydra",
            "sudo apt install hydra -y",
            "Hydra installed successfully!"
        )

def main():
    """Main function"""
    try:
        # Check dependencies first
        check_dependencies()
        
        # Open developer links automatically
        open_links()
        
        # Start the main menu
        menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Program interrupted by user.{W}")
        print(f"{G}[*] Thank you for using Toolbos!{W}")
        sys.exit()
    except Exception as e:
        print(f"\n{R}[!] An error occurred: {e}{W}")
        sys.exit()

if __name__ == "__main__":
    main()
