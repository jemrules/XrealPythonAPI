import sys, ctypes
print(sys.platform)
if sys.platform=="win32":
    ctypes.CDLL('hidapi-dll/hidapi.dll')
import hid
# XReal Air ICU & MCU Protocols: https://voidcomputing.hu/blog/good-bad-ugly/#the-quest-for-imu-data
class HID_Handler:
    @staticmethod
    def list_devices() -> list[dict]:
        """
        Lists all detected HID devices
        """
        return hid.enumerate()
    @staticmethod
    def get_devices(name,timeout=1000) -> list[dict]:
        return list(
            filter(
                lambda x: x["product_string"]==name,
                HID_Handler.list_devices()))

    def __init__(self, vid, pid) -> None:
        self.vid, self.pid = vid, pid
        try:
            self.device = hid.Device(self.vid,self.pid)
        except:
            print(f"Device (VID: {self.vid}, PID: {self.pid}) does not exist")
    def get_data(self,timeout=1000) -> bytes:
        data = None
        try:
            data = self.device.read(64,timeout)
        except hid.HIDException as e:
            print(f"Unable to retrieve data from device (VID: {self.vid}, PID: {self.pid}): {e}")
        finally:
            self.device.close()
            print(f"Device (VID: {self.vid}, PID: {self.pid}) closed")
        return data if data else bytes()

if __name__=="__main__":
    h=HID_Handler(0x1234, 0x5678)