import os
import json
f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'monita_icons', 'vendor_map.json'))
vendor_map = json.load(f)
f.close()
