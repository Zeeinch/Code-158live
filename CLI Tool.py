import socket

def get_ip_from_website(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✔] IP address dari {domain} adalah: {ip}")
    except socket.gaierror:
        print(f"[✘] Gagal menemukan IP untuk: {domain}")

if __name__ == "__main__":
    website = input("Masukkan alamat website (contoh: google.com): ")
    get_ip_from_website(website)
