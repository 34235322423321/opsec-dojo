import os
import time

GREEN = "\033[92m"
RESET = "\033[0m"

def slow(text, speed=0.01):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ==========================
# PAGE 1 — THE DOJO ENTRANCE
# ==========================
def page_1():
    clear()
    slow(GREEN + r"""
====================================================
           █▀▄▀█ █▀█ █▀ █▀▀ █▀█   █▀▄▀█ █▀█
           █ ▀ █ █▄█ ▄█ ██▄ █▄█   █ ▀ █ █▄█
====================================================
   WELCOME TO THE 90s OPSEC DOJO TERMINAL, OPERATIVE
====================================================

[01] YOUR MISSION:
     THIS DOJO TEACHES YOU HOW TO BECOME INVISIBLE.
     MINDSET • DEVICE SAFETY • NETWORK STEALTH • IDENTITY CONTROL

[02] RULES OF THE DOJO:
     - NO ILLEGAL MOVES
     - NO HARM TO PEOPLE
     - NO MALWARE
     - ONLY ETHICAL CYBERNINJA TRAINING

[03] DOJO CODE:
     - MOVE IN SHADOWS
     - LEAVE NO FOOTPRINTS
     - PROTECT THE WEAK
     - MASTER YOURSELF

====================================================
 Press [ENTER] to proceed to PAGE 2...
====================================================
""" + RESET)
    input()
    page_2()

# ==========================
# PAGE 2 — SHADOW ARMOR
# ==========================
def page_2():
    clear()
    slow(GREEN + r"""
========================================================
     >> PAGE 2: SHADOW ARMOR PROTOCOL <<
        PERSONAL OPSEC • STEALTH MODE
========================================================

[01] DIGITAL FOOTPRINT NULLIFICATION
     - No real name, no location, no pictures.
     - Separate emails for each identity.
     - Delete EXIF metadata from every image.
     - Never reuse usernames.

[02] DEVICE HARDENING
     - Turn off Bluetooth & NFC.
     - Use local accounts, not cloud.
     - Keep updates on.
     - No random extensions.

[03] BROWSER STEALTH GUARD
     - Use Firefox/Brave.
     - Add uBlock, Privacy Badger, NoScript.
     - Disable WebRTC (stops IP leaks).
     - Keep OPSEC identity in a separate browser.

[04] PASSWORD MASTER TECHNIQUE
     - Password manager recommended.
     - Use passphrases.
     - No reusing passwords.
     - Use authenticator apps for 2FA.

[05] IDENTITY COMPARTMENTALIZATION
     - Split PERSONAL / GAME / HACKER / SCHOOL.
     - Never mix identities.

========================================================
 Press [ENTER] to proceed to PAGE 3...
========================================================
""" + RESET)
    input()
    page_3()


# ==========================
# PAGE 3 — NETWORK STEALTH
# ==========================
def page_3():
    clear()
    slow(GREEN + r"""
========================================================
         >> PAGE 3: NETWORK SHADOW TECHNIQUES <<
    WI-FI SECURITY • TRAFFIC PROTECTION • SAFE ROUTING
========================================================

[01] WI-FI SAFETY BASIC TRAINING
     - Change router password.
     - Disable WPS.
     - Use WPA3 if possible.
     - Don’t use public WiFi for logins.

[02] TRAFFIC CAMOUFLAGE (LEGAL)
     - HTTPS everywhere.
     - DNS over HTTPS (DoH).
     - Avoid old apps that leak your IP.

[03] VPN BASICS (ETHICAL)
     - Use trusted ones only.
     - Avoid free VPNs (they steal data).
     - Never stack VPN + sketchy tools.

[04] TOR BASICS (ETHICAL)
     - Great for privacy, not hacking.
     - Don’t log into personal accounts on Tor.
     - Disable scripts inside Tor Browser.

[05] HOME NETWORK HARDENING
     - Separate “guest” WiFi.
     - Router firmware updates.
     - Block unknown devices.
     - Change DNS to privacy DNS.

========================================================
 Press [ENTER] for PAGE 4 (DEVICE CLEANLINESS)...
========================================================
""" + RESET)
    input()
    page_4()


# ==========================
# PAGE 4 — DEVICE CLEANLINESS
# ==========================
def page_4():
    clear()
    slow(GREEN + r"""
========================================================
        >> PAGE 4: DEVICE CLEANLINESS PROTOCOL <<
     NO VIRUSES • NO TRACKERS • NO SUSPICIOUS FILES
========================================================

[01] DIGITAL HYGIENE
     - Don’t install random .exe files.
     - Scan USB drives before opening.
     - Run antivirus weekly.

[02] APP PERMISSION CONTROL
     - Remove camera/mic access from apps.
     - Turn off location for everything.

[03] ANTI-TRACKING
     - Block ads.
     - Disable telemetry.
     - Keep background apps minimal.

[04] STORAGE PURIFICATION
     - Remove old logs.
     - Delete download folder.
     - Clear browser data.

========================================================
    END OF CURRENT DOJO LEVELS
  More pages will unlock soon...
========================================================
""" + RESET)
    input()
    clear()
    slow(GREEN + "DOJO SESSION CLOSED. RETURN SOON, OPERATIVE." + RESET)


page_1()
