import tkinter as tk
from tkinter import messagebox
import socket

# Create the GUI window
root = tk.Tk()
root.title("Port Scanner v.1")
root.geometry("400x200")

# Change the background color of the GUI window to black
root.config(bg='black')

# Create the widgets


ip_label = tk.Label(root, text="IP address:", bg='black', fg='white')
ip_label.pack()

ip_entry = tk.Entry(root)
ip_entry.pack()

start_port_label = tk.Label(root, text="Starting port number:", bg='black', fg='white')
start_port_label.pack()

start_port_entry = tk.Entry(root)
start_port_entry.pack()

end_port_label = tk.Label(root, text="Ending port number:", bg='black', fg='white')
end_port_label.pack()

end_port_entry = tk.Entry(root)
end_port_entry.pack()

result_label = tk.Label(root, bg='black', fg='white')
result_label.pack()

# Define the function to scan ports
def scan_ports():
    # Get the user inputs for IP address and port range
    ip_address = ip_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid port number")
        return

    # Create a list to hold the open ports
    open_ports = []

    # Create a list to hold the closed ports
    closed_ports = []

    # Loop over the range of port numbers to scan
    for port in range(start_port, end_port+1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set the socket timeout to 1 second
            sock.settimeout(1)

            # Attempt to connect to the IP address and port
            result = sock.connect_ex((ip_address, port))

            # If the connection is successful, add the port number to the list of open ports
            if result == 0:
                open_ports.append(port)
            else:
                closed_ports.append(port)

            # Close the socket connection
            sock.close()
        except socket.error:
            pass

    # Display the list of open ports in the GUI
    if open_ports:
        result_label.config(text="Open ports: " + str(open_ports))
    else:
        result_label.config(text="No open ports found")

    # Display the list of closed ports in the GUI
    if closed_ports:
        result_label.config(text=result_label.cget("text") + "\nClosed ports: " + str(closed_ports))

# Create the scan button
scan_button = tk.Button(root, text="Scan", command=scan_ports, bg='white', fg='black')
scan_button.pack()

# Run the GUI window
root.mainloop()

