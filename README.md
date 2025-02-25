# ThoughtBox
Plans to make a 3D-printed box with a Raspberry Pi inside. When the button is pressed it sends a notification to chosen computer, running a Python script through Tailscale

## Requirements
- A computer able to run both Tailscale and a Python script. This is the reciever
- Some sort of small computer with Tailscale and Python capabilities, along with GPIO pins and internet access. This is the sender. I used a Raspberry Pi
- A Tailscale account (Free for up to 100 users)
- Access to 3D Printer to create parts

### Python libraries on reciever:
- Flask
- HueSDK (optional)
- Win10Toast

### Python libraries on sender:
- RPiGPIO

## Communication
The computer in your ThoughtBox (A Raspberry Pi in my case), the sender, will be connected to Wi-Fi along with the Tailscale VPN service. On the computer you want to get the notifications on, the reciever, there will be a Python script running. It will also be connected to the Tailscale VPN service. Included in the repo is a .vbs file that you can run on start up. This will start the Python script on the reciever along with serving the web server.

When the button connected to the Raspberry Pi is pushed it sends a GET request through the Tailscale VPN service and to the Flask webserver running on the reciever. This will then do or display whatever you want it to.

## Setup
**On the sender side**

Setting up sender involves installing the Tailscale VPN service (https://tailscale.com/kb/1347/installation) and ensuring that on start up it starts the Python script. In the ```SenderThoughtBox.py``` file. Change the requests.get addresses to the correct machine IP which you get from Tailscale.

**On the reciever side**

You have to set up a Flask app along with the Tailscale VPN service. I do not know how to set up a Flask app as I just made PyCharm do it for me but if anyone knows, please post. If you happen to have Hue lights you can uncomment the lines regarding the hue lights, otherwise those can be ignored. To get the IP your sender has to send the GET request you will have run tailscale serve "port your flask app is running on" in the command line and copy the address given to you.

## 3D Printed Box

In the "Hardware" folder in the repo are all the files you need to print to make this box. Do your normal settings and it should turn out fine. The holes in the main box are for heatset inserts, along with the 3 ones close to the thing sticking out on the lid and the 4 inner holes. Three rods screw into the 3 holes close to the thing sticking out because that's what I had on hand but I will supply the STEP files so you can modify however you want.
