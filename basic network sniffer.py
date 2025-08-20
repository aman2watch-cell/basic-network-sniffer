from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            proto_name = "TCP"
        elif UDP in packet:
            proto_name = "UDP"
        else:
            proto_name = str(proto)

        print(f"[+] Source: {ip_src} --> Destination: {ip_dst} | Protocol: {proto_name}")

def main():
    print("Starting Network Sniffer... Press CTRL+C to stop.")
    sniff(prn=packet_callback, store=0)

if _name_ == "_main_":
    main()