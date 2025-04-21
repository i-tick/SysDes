class DisplayDevice:
    def show_temp(self, temp):
        print(f"Current Temp: {temp} C")


class WeatherStation:
    def __init__(self, display_device):
        self.temperature = 0.0
        self.display_device = display_device  # Can be extended to multiple devices later

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify_device()

    def notify_device(self):
        self.display_device.show_temp(self.temperature)


if __name__ == "__main__":
    device = DisplayDevice()
    station = WeatherStation(device)
    # Tight Coupling between station and the device
    station.set_temperature(26)
    station.set_temperature(30)