import time

from flask import Flask
from win10toast import ToastNotifier

#from huesdk import Hue

heartToast = ToastNotifier()

#hue = Hue(bridge_ip = "#INSERTHUEBRIDGEIPHERE", username = "#INSERTHUEUSERNAMEHERE") #Uncomment if you want to use Hue lights

app = Flask(__name__)

#roomLights = hue.get_group(id_ = 1)

#lights = hue.get_lights()


# class hueLight:
# def __init__(self, id, name, bri, hue, is_on, sat):
#     self.id = id
#     self.name = name
#     self.bri = bri
#     self.hue = hue
#     self.is_on = is_on
#     self.sat = sat


filtered_lights = []


@app.route('/button', methods = ['GET'])
def notify():
    #lights = hue.get_lights()

    # for light in lights:
    #     if 3 <= int(light.id_) <= 7:
    #         new_light = hueLight(light.id_, light.name, light.bri, light.hue, light.is_on, light.sat)
    #         filtered_lights.append(new_light)
    # roomLights.set_brightness(255)
    # roomLights.set_color(hexa = "f91010", transition = 0)
    # time.sleep(1)
    # roomLights.set_brightness(5)
    # time.sleep(1)
    # roomLights.set_brightness(255)
    heartToast.show_toast("#PUTTITLE", "#PUTYOURMESSAGEHERE", duration = 5, icon_path = '#PUTICONPATHHERE')
    # i = 0
    # for light in lights:
    # 
    #     if 3 <= int(light.id_) <= 7:
    #         light.set_brightness(filtered_lights[i].bri)
    #         light.set_color(filtered_lights[i].hue)
    #         light.set_saturation(filtered_lights[i].sat)
    #         i += 1
    # filtered_lights.clear()
    return "Notification received!"


@app.route('/startup', methods = ['GET'])
def show_startup():
    heartToast.show_toast("Connected", "Thoughtbox is connected!", duration = 2)
    return "Server is running!"


if __name__ == '__main__':
    heartToast.show_toast("Thoughtbox", "Thoughtbox server is running", duration = 2)
    app.run(host = '0.0.0.0', port = 5000)  # Change the port if needed
