# HustAuth

![HustPassLogo](https://pass.hust.edu.cn/cas/comm/image/logo-inside.png)

This project provides HustPass support for [Requests](https://requests.readthedocs.io/)

Variation of [HustLogin](https://github.com/MarvinTerry/HustLogin)

## Installation

- Step1: install the lib
    ```
    pip install requests-hustauth
    ```

- Step2: install Tesseract-OCR back-end
    ```
    sudo apt install tesseract-ocr
    ```
    P.S. For Windows users [download binary here](https://digi.bib.uni-mannheim.de/tesseract/) (5.0.0+)

## Usage

example.py
```python
import requests
from requests_hustauth import HustAuth

session = requests.Session()
hust_auth = HustAuth('USERID','PASSWORD')

resp = session.get('http://m.hust.edu.cn/wechat/apps_center.jsp',auth=hust_auth)
print(resp.text)
```

