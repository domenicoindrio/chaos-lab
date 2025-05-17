import scapy.all as scapy 
import argparse
import sys
# Arper, a simple NetDiscover-like python script


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # srp() , is like sr()'send and receive' but for sending packets with a custom ether part
    # for the script we want only the first
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered_list

def print_results(answers_list):
    print("-" * 40)
    print(f"{'IP':<20} {'at MAC Address':<20}")
    print("-" * 40)

    for packet_sent, packet_received in answers_list:
        print(f"{packet_received.psrc:<20} {packet_received.hwsrc:<20}")
    


def main():
    parser = argparse.ArgumentParser(description="Arper, a simple NetDiscover-like python script. Since it works at layer 2, use sudo privileges" 
    " a broadcast/ARP request to discover clients connected to the same LAN network")

    parser.add_argument("--range", required=True, type=str, help="IP Range to search" )
    args = parser.parse_args()
    try:
        print("\n[*] Starting Network scan...\n")
        scan_result = scan(args.range)
        if not scan_result:
            print("[-] No host responded to the ARP request, exiting...")
            sys.exit(1)
        else:
            print_results(scan_result)
            print("\n[+] Network scan finished, exiting...")
            sys.exit(0)
    except KeyboardInterrupt:
        print("[!] Scan interrupted by user, exiting...\n")
        sys.exit(1)

if __name__ == "__main__":
    main()


# scapy useful command:
# scapy.ls() for checking objects fields, eg. scapy.ls(scapy.ARP())    
# .summary() eg. print(answered_list.summary())
# .show() eg. packet.show()
