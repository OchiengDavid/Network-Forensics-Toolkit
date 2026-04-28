#  Incident Report: DarkGate Infection Analysis
**Date:** May 2024
**Tool Used:** custom `dns_analyzer.py`

##  Executive Summary
Using the automated DNS extraction tool, I analyzed the network traffic from the 2023-11-20 DarkGate lab. The tool successfully isolated 5 unique domains from the packet capture in under 1 second.

## High-Risk Findings
The most significant finding is the contact with **`Analysis_output.png`**. 
- **Type:** Malicious C2 (Command & Control)
- **Function:** Used by DarkGate for data exfiltration and command retrieval.

## Tool Performance
By using Python and Scapy, I avoided the need to manually scroll through 1,000+ packets in Wireshark, demonstrating a scalable approach to network triage.

###  Phase 2: HTTP Payload Analysis
Using the custom `http_hunter.py` module, I reconstructed the infection timeline:

1.  **Initial Lure:** The host requested `unsupported-version.pdf`.
2.  **Payload Delivery:** A malicious executable, `Seed.exe`, was downloaded via HTTP Port 80.
3.  **Advanced Evasion:** The tool identified a `leaf.au3` (AutoIt) script download, a signature characteristic of DarkGate's evasion strategy.
4.  **Anomaly Detection:** Request #3 captured encrypted binary data (Shellcode), indicating an attempted memory injection.

