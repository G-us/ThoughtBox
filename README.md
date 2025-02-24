# ThoughtBox
Plans to make a 3D-printed box with a Raspberry Pi inside. When the button is pressed it sends a notification to chosen computer, running a Python script through Tailscale

## Requirements
- A computer able to run both Tailscale and a Python script. This is the reciever
- Some sort of small computer with Tailscale and Python capabilities, along with GPIO pins and internet access. This is the sender. I used a Raspberry Pi
- A Tailscale account (Free for up to 100 users)
- Access to 3D Printer to create parts

### Python libraries on reciever:
- Flask
- HueSDK
- Win10Toast

### Python libraries on sender:
- RPiGPIO

## Communication
The computer in your ThoughtBox (A Raspberry Pi in my case), the sender, will be connected to Wi-Fi along with the Tailscale VPN service. On the computer you want to get the notifications on, the reciever, there will be a Python script running. It will also be connected to the Tailscale VPN service. Included in the repo is a .vbs file that you can run on start up. This will start the Python script on the reciever along with serving the web server.

When the button connected to the Raspberry Pi is pushed it sends a GET request through the Tailscale VPN service and to the Flask webserver running on the reciever. This will then do or display whatever you want it to.

## Setup
Setting up sender involves installing the Tailscale VPN service (https://tailscale.com/kb/1347/installation) and ensuring that on start up it starts the Python script. In the ```SenderThoughtBox.py``` file. Change the requests.get addresses to the correct machine IP which you get from Tailscale.
