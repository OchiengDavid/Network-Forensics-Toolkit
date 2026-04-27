# Network Forensics Toolkit
**Automated Traffic Analysis & Malware Triage Suite**

![Python](https://shields.io)
![Security](https://shields.io)
![Status](https://shields.io)

## Project Overview
This toolkit is a collection of Python-based forensic tools designed to automate the manual "grunt work" of network investigations. Instead of manually filtering thousands of packets in Wireshark, these scripts provide instant insights into malicious activity.

---

##  Case Study: DarkGate Infection (Nov 2023)
The current module focuses on the **DarkGate Malware** infection chain. 

###  Featured Tool: DNS Analyzer
Located in `Scripts/dns_analyzer.py`, this tool extracts all unique DNS queries from a PCAP to identify Command & Control (C2) communication.
![Analysis Screenshot](analysis_output.png)

**Key Findings:**
- **Automated Extraction:** Successfully isolated 5 unique domains from the lab evidence.
- **Critical IoC Identified:** Identified communication with `Analysis_ouput.png`, a known DarkGate C2 domain.
- **Efficiency:** Reduced triage time from minutes to milliseconds.

---

##  Repository Structure
- ` Scripts/`: Core Python tools (Scapy-based).
- `Evidences/`: Lab PCAP files (Note: Excluded from Git for safety).
- `REPORT_LAB_01.md`: Detailed forensic breakdown of the DarkGate infection.

##  Getting Started
1. Clone the repo: `git clone https://github.com`
2. Install dependencies: `pip install scapy`
3. Run the analyzer: `python Scripts/dns_analyzer.py`

---

## Roadmap (May 2024)
- [x] Phase 1: DNS Triage & C2 Identification.
- [ ] Phase 2: HTTP Payload Extraction (Detecting malicious .zip/ .exe downloads).
- [ ] Phase 3: Memory Forensics Integration (Volatility 3 correlation).

