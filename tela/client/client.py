import requests
import time
import random
import socket
import os

def send_data():
    while True:
        try:
            # Add more verbose logging
            print(f"Attempting to resolve server-service hostname...")
            try:
                server_ip = socket.gethostbyname('server-service')
                print(f"Resolved server-service to IP: {server_ip}")
            except socket.gaierror as dns_error:
                print(f"DNS resolution error: {dns_error}")
                time.sleep(5)
                continue

            key = f"key_{random.randint(1,100)}"
            value = f"value_{random.randint(1,1000)}"
            
            print(f"\nTrying to send data: {key}:{value}")
            
            # More comprehensive error handling
            try:
                response = requests.post(
                    'http://server-service:5000/api/data',
                    json={'key': key, 'value': value},
                    timeout=10
                )
                response.raise_for_status()  # Raise an exception for bad status codes
                print(f"Server response: {response.json()}")
                
                # Retrieve the data to confirm
                get_response = requests.get(
                    f'http://server-service:5000/api/data/{key}',
                    timeout=10
                )
                get_response.raise_for_status()
                print(f"Retrieved data: {get_response.json()}")
                
            except requests.exceptions.RequestException as req_error:
                print(f"Request Error: {req_error}")
                print(f"Error Details:")
                print(f"  Type: {type(req_error).__name__}")
                print(f"  Server Service URL: http://server-service:5000")
                
                # Additional network diagnostics
                try:
                    socket.create_connection(('server-service', 5000), timeout=5)
                    print("Socket connection to server-service:5000 successful")
                except (socket.error, socket.timeout) as sock_error:
                    print(f"Socket connection error: {sock_error}")
        
        except Exception as e:
            print(f"Unexpected Error: {e}")
        
        time.sleep(5)

if __name__ == "__main__":
    print("Client starting...")
    print(f"Hostname: {socket.gethostname()}")
    send_data()