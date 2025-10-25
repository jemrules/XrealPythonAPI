import sys
from os.path import join as pjoin, abspath
sys.path.append('.')
from xrealapi import HID_Handler as HDH
def form(x:dict) -> str:
    return f"{x['product_string']} : VID:{x['vendor_id']} PID:{x['product_id']}"
print('\n'.join(map(form,HDH.list_devices())))