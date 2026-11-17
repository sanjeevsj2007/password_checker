"""
Task 1: Cybersecurity Fundamentals
==================================
An educational, runnable study guide covering:
  1. Core principles of cybersecurity & ethical hacking
  2. Types of hackers
  3. The CIA Triad (with small defensive demos)
  4. Common threats: malware, phishing, ransomware and their impact

Usage:
    python task1_cybersecurity_fundamentals.py          # print the full guide
    python task1_cybersecurity_fundamentals.py --demo   # include defensive demos
    python task1_cybersecurity_fundamentals.py --quiz   # take a short quiz

Note: This file is for learning and contains only defensive, harmless demos.
"""

import hashlib
import re
import sys
from urllib.parse import urlparse

LINE = "=" * 70


def header(title: str) -> None:
    print(f"\n{LINE}\n{title.upper()}\n{LINE}")


# ----------------------------------------------------------------------
# 1. Core principles & ethical hacking
# ----------------------------------------------------------------------
CORE_PRINCIPLES = {
    "Defense in depth": "Layer multiple controls so one failure doesn't mean total compromise.",
    "Least privilege": "Give users and programs only the access they need, nothing more.",
    "Zero trust": "Never trust by default; verify every user, device and request.",
    "Fail securely": "When something breaks, default to a safe (denied) state.",
    "Separation of duties": "No single person should control a critical process end to end.",
    "Security by design": "Build security in from the start rather than bolting it on.",
}

ETHICAL_HACKING_PHASES = [
    ("Planning & Authorization", "Get written permission and define scope and rules of engagement."),
    ("Reconnaissance", "Gather information about the target (passive and active)."),
    ("Scanning & Enumeration", "Identify live hosts, open ports, services and versions."),
    ("Gaining Access", "Carefully test whether vulnerabilities can actually be exploited."),
    ("Maintaining Access", "Assess whether an attacker could persist (within scope)."),
    ("Analysis & Reporting", "Document findings, risk ratings and remediation advice."),
    ("Remediation & Retest", "Fix the issues, then verify the fixes work."),
]


def show_principles() -> None:
    header("Core Principles of Cybersecurity")
    for name, desc in CORE_PRINCIPLES.items():
        print(f"- {name}: {desc}")

    header("What Is Ethical Hacking?")
    print(
        "Ethical hacking is the authorized practice of probing systems for\n"
        "weaknesses, using the same techniques as attackers, in order to fix\n"
        "them before malicious actors find them. The key difference is\n"
        "PERMISSION, SCOPE and INTENT TO IMPROVE security.\n"
    )
    for i, (phase, desc) in enumerate(ETHICAL_HACKING_PHASES, 1):
        print(f"{i}. {phase}: {desc}")


# ----------------------------------------------------------------------
# 2. Types of hackers
# ----------------------------------------------------------------------
HACKERS = [
    {
        "type": "White Hat",
        "motive": "Improve security; works with permission",
        "legal": "Legal / authorized",
        "example": "Penetration tester, bug bounty hunter, security researcher",
    },
    {
        "type": "Black Hat",
        "motive": "Financial gain, theft, disruption, espionage",
        "legal": "Illegal",
        "example": "Ransomware operator, credit-card thief, botnet owner",
    },
    {
        "type": "Grey Hat",
        "motive": "Mixed; finds flaws without permission, often discloses them",
        "legal": "Legally ambiguous (still unauthorized)",
        "example": "Researcher who probes a site uninvited, then reports the bug",
    },
    {
        "type": "Script Kiddie",
        "motive": "Curiosity, bragging rights, mischief",
        "legal": "Illegal",
        "example": "Runs pre-made tools with little understanding of how they work",
    },
    {
        "type": "Hacktivist",
        "motive": "Political or social cause",
        "legal": "Illegal",
        "example": "Defacing a website or leaking data to make a statement",
    },
    {
        "type": "State-Sponsored",
        "motive": "Espionage, sabotage, geopolitical advantage",
        "legal": "Backed by a government",
        "example": "Advanced Persistent Threat (APT) groups",
    },
    {
        "type": "Insider Threat",
        "motive": "Revenge, profit, or simple negligence",
        "legal": "Varies",
        "example": "Disgruntled employee, or staff who click a bad link",
    },
]


def show_hackers() -> None:
    header("Types of Hackers")
    for h in HACKERS:
        print(f"\n[{h['type']}]")
        print(f"  Motive : {h['motive']}")
        print(f"  Legal  : {h['legal']}")
        print(f"  Example: {h['example']}")


# ----------------------------------------------------------------------
# 3. CIA Triad
# ----------------------------------------------------------------------
CIA = {
    "Confidentiality": {
        "goal": "Only authorized people can view the data.",
        "controls": ["Encryption", "Access control / MFA", "Data classification"],
        "violated_by": "Data breach, eavesdropping, stolen credentials",
    },
    "Integrity": {
        "goal": "Data stays accurate and unaltered by unauthorized parties.",
        "controls": ["Hashing & digital signatures", "Version control", "Input validation"],
        "violated_by": "Tampering, SQL injection, man-in-the-middle modification",
    },
    "Availability": {
        "goal": "Systems and data are accessible when needed.",
        "controls": ["Backups & redundancy", "DDoS protection", "Patching & monitoring"],
        "violated_by": "DDoS attack, ransomware, hardware failure",
    },
}


def show_cia() -> None:
    header("The CIA Triad")
    for name, info in CIA.items():
        print(f"\n{name}")
        print(f"  Goal       : {info['goal']}")
        print(f"  Controls   : {', '.join(info['controls'])}")
        print(f"  Violated by: {info['violated_by']}")


# ----------------------------------------------------------------------
# 4. Common threats and their impact
# ----------------------------------------------------------------------
THREATS = {
    "Malware": {
        "what": "Malicious software built to damage, spy on, or take control of systems.",
        "kinds": "Viruses, worms, trojans, spyware, keyloggers, rootkits, adware",
        "spread": "Infected downloads, email attachments, USB drives, unpatched software",
        "impact": "Data theft, system slowdown/crashes, backdoor access, botnet recruitment",
        "cia": ["Confidentiality", "Integrity", "Availability"],
        "defense": "Antivirus/EDR, patching, least privilege, avoiding untrusted downloads",
    },
    "Phishing": {
        "what": "Social engineering that tricks people into revealing secrets or running malware.",
        "kinds": "Email phishing, spear phishing, whaling, smishing (SMS), vishing (voice)",
        "spread": "Fake emails, texts, calls and cloned login pages",
        "impact": "Stolen credentials, financial fraud, account takeover, initial foothold for ransomware",
        "cia": ["Confidentiality", "Integrity"],
        "defense": "User awareness training, MFA, email filtering, verify requests out-of-band",
    },
    "Ransomware": {
        "what": "Malware that encrypts files (and often steals them) and demands payment.",
        "kinds": "Crypto-ransomware, locker ransomware, double/triple extortion",
        "spread": "Phishing, exposed remote desktop, unpatched vulnerabilities",
        "impact": "Operations halted, data loss or leak, recovery costs, reputational damage",
        "cia": ["Availability", "Confidentiality"],
        "defense": "Offline/immutable backups, patching, network segmentation, incident response plan",
    },
}


def show_threats() -> None:
    header("Common Threats and Their Impact")
    for name, t in THREATS.items():
        print(f"\n[{name}]")
        print(f"  What    : {t['what']}")
        print(f"  Kinds   : {t['kinds']}")
        print(f"  Spread  : {t['spread']}")
        print(f"  Impact  : {t['impact']}")
        print(f"  CIA hit : {', '.join(t['cia'])}")
        print(f"  Defense : {t['defense']}")

    header("Threat vs. CIA Triad Matrix")
    cols = ["Confidentiality", "Integrity", "Availability"]
    print(f"{'Threat':<12}" + "".join(f"{c:<18}" for c in cols))
    for name, t in THREATS.items():
        row = "".join(f"{('X' if c in t['cia'] else '-'):<18}" for c in cols)
        print(f"{name:<12}{row}")


# ----------------------------------------------------------------------
# Defensive demos (harmless)
# ----------------------------------------------------------------------
def demo_integrity() -> None:
    """Integrity: a hash changes if even one character changes."""
    print("\n[Demo 1] Integrity with SHA-256 hashing")
    original = "Transfer $100 to Alice"
    tampered = "Transfer $900 to Alice"
    h1 = hashlib.sha256(original.encode()).hexdigest()
    h2 = hashlib.sha256(tampered.encode()).hexdigest()
    print(f"  Original : {original!r}\n    hash = {h1[:32]}...")
    print(f"  Tampered : {tampered!r}\n    hash = {h2[:32]}...")
    print(f"  Hashes match? {h1 == h2}  -> tampering detected!" if h1 != h2 else "  Match")


def password_strength(pw: str) -> str:
    """Confidentiality: stronger passwords resist guessing."""
    score = 0
    score += len(pw) >= 12
    score += bool(re.search(r"[a-z]", pw)) and bool(re.search(r"[A-Z]", pw))
    score += bool(re.search(r"\d", pw))
    score += bool(re.search(r"[^\w\s]", pw))
    return ["Very weak", "Weak", "Fair", "Good", "Strong"][score]


def demo_confidentiality() -> None:
    print("\n[Demo 2] Password strength (Confidentiality)")
    for pw in ["password", "Summer2024", "c0rrect-Horse-battery!"]:
        print(f"  {pw:<25} -> {password_strength(pw)}")


SUSPICIOUS_WORDS = ["urgent", "verify", "suspended", "password", "login", "bank", "update", "prize"]


def phishing_red_flags(url: str, text: str = "") -> list:
    """Very simple educational phishing heuristic (not a real filter)."""
    flags = []
    parsed = urlparse(url)
    host = parsed.hostname or ""
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", host):
        flags.append("URL uses a raw IP address")
    if parsed.scheme != "https":
        flags.append("Connection is not HTTPS")
    if host.count(".") >= 3:
        flags.append("Many subdomains (possible look-alike domain)")
    if "@" in url:
        flags.append("'@' in URL can hide the real destination")
    if "xn--" in host:
        flags.append("Punycode domain (possible look-alike characters)")
    hits = [w for w in SUSPICIOUS_WORDS if w in (url + " " + text).lower()]
    if hits:
        flags.append("Pressure/credential words: " + ", ".join(hits))
    return flags


def demo_phishing() -> None:
    print("\n[Demo 3] Phishing red-flag checker")
    samples = [
        ("https://www.example.com/about", "Our company history"),
        ("http://192.168.4.7/secure.login.bank.verify.example.net", "URGENT: verify your password now"),
    ]
    for url, text in samples:
        flags = phishing_red_flags(url, text)
        print(f"  {url}")
        print("    " + ("No obvious flags" if not flags else "\n    ".join("! " + f for f in flags)))


def run_demos() -> None:
    header("Defensive Demos")
    demo_integrity()
    demo_confidentiality()
    demo_phishing()


# ----------------------------------------------------------------------
# Quiz
# ----------------------------------------------------------------------
QUIZ = [
    ("Which CIA element does ransomware attack most directly? (C/I/A)", "a"),
    ("Which hacker type works with permission to improve security? (white/black/grey)", "white"),
    ("Phishing is a form of what kind of attack? (social engineering/brute force)", "social engineering"),
    ("Hashing helps verify which CIA element? (C/I/A)", "i"),
    ("Giving users only the access they need is called least ____?", "privilege"),
]


def run_quiz() -> None:
    header("Quick Quiz")
    score = 0
    for q, ans in QUIZ:
        if input(q + "\n> ").strip().lower() == ans:
            print("Correct!\n")
            score += 1
        else:
            print(f"Not quite. Answer: {ans}\n")
    print(f"Score: {score}/{len(QUIZ)}")


# ----------------------------------------------------------------------
def main() -> None:
    args = sys.argv[1:]
    if "--quiz" in args:
        run_quiz()
        return
    print("CYBERSECURITY FUNDAMENTALS - Study Guide (task1)")
    show_principles()
    show_hackers()
    show_cia()
    show_threats()
    if "--demo" in args:
        run_demos()
    print("\nTip: run with --demo for defensive demos or --quiz to test yourself.")


if __name__ == "__main__":
    main()
