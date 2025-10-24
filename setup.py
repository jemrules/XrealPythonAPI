import os
import sys

match sys.platform:
    case "linux":
        os.system("sudo apt install libhidapi-dev")