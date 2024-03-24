import threading
import socket
import time

print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@@@@@@@@ @@@@@@@@@@@@@@@@@  @@@@@@@@@
                     @@@@@@@@@     @@@@@@@@@@     @@@@@@@@@
                     @@@@@@@@@       @@@@@        @@@@@@@@@
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@@@@@@@@    @@@@    @@@@    @@@@@@@@@                    
                     @@@@@@@@@    @@@@    @@@@    @@@@@@@@@
                     @@@@@@@@@    @@@@    @@@@    @@@@@@@@@
                     @@@@@@@@@    @@@@    @@@@    @@@@@@@@@
  ____                   _                               
 |  _ \    ___    _ __  | |_   _ __ ___     __ _   _ __  
 | |_) |  / _ \  | '__| | __| | '_ ` _ \   / _` | | '_ \ 
 |  __/  | (_) | | |    | |_  | | | | | | | (_| | | |_) |
 |_|      \___/  |_|     \__| |_| |_| |_|  \__,_| | .__/ 
                                                  |_|
                                                  by Rehman. Open source project
""")

def port_servisini_bul(port_numarasi):
    try:
        servis_adi = socket.getservbyport(port_numarasi)
        return servis_adi
    except OSError:
        return "Not result"

def port_scan(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((target_ip, port))
            sock.send(b'\x19') 
            response = sock.recv(1024)

            if b'RST' in response: 
                pass
            else:
                service = port_servisini_bul(port)
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

    num_threads = thread

    start_time = time.time() 

    threads = []
    for port in range(port_start, port_end + 1):
        thread = threading.Thread(target=port_scan, args=(target_ip, port))
        threads.append(thread)
        thread.start()
      
    for thread in threads:
        thread.join() 
      
    end_time = time.time()
    total_time = end_time - start_time
    print("[$] ----------------------")
    print(f"Tarama {total_time:.2f} saniyede tamamlandı.")
    print("[$] ----------------------")
