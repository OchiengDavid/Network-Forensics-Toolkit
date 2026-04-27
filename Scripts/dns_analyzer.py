from scapy.all import rdpcap, DNSQR

def extract_dns(pcap_path):
    print(f"--- 🔍 Analyzing DarkGate Traffic: {pcap_path} ---")
    try:
        # This loads the packets from your Evidences folder
        packets = rdpcap(pcap_path)
        domains = set()

        for pkt in packets:
            # We are looking for DNS Queries (where the PC went)
            if pkt.haslayer(DNSQR):
                query = pkt[DNSQR].qname.decode('utf-8')
                domains.add(query)

        print(f"[+] Found {len(domains)} unique domains:")
        for d in sorted(domains):
            print(f"  > {d}")

    except Exception as e:
        print(f" [!] Error: {e}. Check if the file is in the 'Evidences' folder.")

if __name__ == "__main__":
    # Pointing to your specific folder structure
    extract_dns("Evidences/darkgate.pcap")