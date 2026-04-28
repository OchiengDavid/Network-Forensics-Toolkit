from scapy.all import rdpcap, TCP, Raw

def analyze_http_pcap(file_path):
    print(f"--- Extracting HTTP Payloads from: {file_path} ---")
    try:
        packets = rdpcap(file_path)
        found_payloads = 0

        for pkt in packets:
            if pkt.haslayer(Raw):
                payload = pkt[Raw].load.decode('utf-8', errors='ignore')
                
                if "GET" in payload:
                    found_payloads += 1
                    lines = payload.split('\r\n')
                    print(f"\n[!] Request #{found_payloads} Identified")
                    print(f"    {lines[0]}") # Shows "GET /path/file.zip HTTP/1.1"
                    
                    # Look for the User-Agent
                    for line in lines:
                        if "User-Agent:" in line:
                            print(f"    {line}")

        if found_payloads == 0:
            print("[-] No HTTP GET requests found in this sample.")

    except Exception as e:
        print(f" [!] Error reading file: {e}")

if __name__ == "__main__":
    # Should match the filename in the Evidences folder and the one used in dns_analyzer.py for consistency
    analyze_http_pcap("Evidences/darkgate.pcap")
