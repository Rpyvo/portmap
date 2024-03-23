import threading
import socket
import time
print("""
  ____                   _                               
 |  _ \    ___    _ __  | |_   _ __ ___     __ _   _ __  
 | |_) |  / _ \  | '__| | __| | '_ ` _ \   / _` | | '_ \ 
 |  __/  | (_) | | |    | |_  | | | | | | | (_| | | |_) |
 |_|      \___/  |_|     \__| |_| |_| |_|  \__,_| | .__/ 
                                                  |_|
                                                  by Rehman. Open source project
""")
# Hizmetleri tanımla
SERVICES = {
    80: "HTTP",
    22: "SSH",
    530: "RPC",
    21: "FTP",
    23: "Telenet",
    53: "DNS",
    25: "SMTP",
    194: "IRC",
    443: "HTTPS",
    3389: "WSH"
}

def port_scan(target_ip, port):
    """
    Belirtilen IP adresindeki belirli bir portu tarar ve durumu ve hizmet tipini yazdırır.

    Args:
        target_ip (str): Hedef IP adresi.
        port (int): Tarama yapılacak port numarası.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((target_ip, port))
            sock.send(b'\x19')  # SYN bayrağı ayarlanmış paket gönderilir.
            response = sock.recv(1024)

            if b'RST' in response:  # RST yanıtı, portun kapalı olduğunu gösterir
                pass
            else:
                service = SERVICES.get(port)  # Hizmeti belirle, bilinmeyen ise "Unknown" olarak ayarla
                print(f"Port {port}: Açık - {service}")

    except Exception as e:
        pass

if __name__ == "__main__":
    target_ip = input("[$] Hedef IP adresi girin: ")
    port_start = int(input("[$] Başlangıç ​​portunu girin: "))
    port_end = int(input("[$] Bitiş portunu girin: "))
    thread = int(input("[$] Threads sayini girin: "))
    port_say = port_end - port_start
    print("  ")
    time.sleep(2)
    print("[$] ----------------------")
    time.sleep(3)
    print('[$] Hedef ip: {}'.format(target_ip))
    time.sleep(3)
    print('[$] Scanning {}'.format(port_say),"ports...")
    time.sleep(2)
    print("[$] ----------------------")

    # İş parçacığı sayısını belirleyin (isteğe göre ayarlayın)
    num_threads = thread

    start_time = time.time()  # Başlama zamanını kaydedin

    threads = []
    for port in range(port_start, port_end + 1):
        # Yeni bir iş parçacığı oluşturun ve başlatın
        thread = threading.Thread(target=port_scan, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    # Tüm iş parçacıklarının bitmesini bekleyin
    for thread in threads:
        thread.join()

    # Tarama süresini hesaplayın ve yazdırın
    end_time = time.time()
    total_time = end_time - start_time
    print("[$] ----------------------")
    print(f"Tarama {total_time:.2f} saniyede tamamlandı.")
    print("[$] ----------------------")
