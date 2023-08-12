import requests
from requests import PreparedRequest
from requests.auth import AuthBase
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import json
import re
from base64 import b64encode, b64decode
from io import BytesIO
import pytesseract
from logging import root as log
from PIL import Image
from fake_useragent import UserAgent

class HustAuth(AuthBase):
    """HustAuth for HustPass"""
    def __init__(self,uid,pwd):
        self.uid = uid
        self.pwd = pwd
        self.session = requests.Session()
        self.headers = {'User-Agent': UserAgent().random}
        self.session.headers.update(self.headers)

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        response = self.session.get(r.url)
        r.headers.update(self.headers)
        if 'https://pass.hust.edu.cn' in response.url:
            r.url = self._login(response)
        return r
    
    def _login(self, response: requests.Response) -> str:
        """Login and return redirection URL"""
        nonce = re.search(
            '<input type="hidden" id="lt" name="lt" value="(.*)" />', response.text).group(1)
        execution = re.search(
            '<input type="hidden" name="execution" value="(.*)" />', response.text).group(1)
        encrypted_u,encrypted_p = self._encrypt()
        login_form = {
            "rsa": None,
            "ul": encrypted_u,
            "pl": encrypted_p,
            "code": self._decaptcha(),
            "phoneCode": None,
            "lt": nonce,
            "execution": execution,
            "_eventId": "submit"
        }
        login_post = self.session.post(
            "https://pass.hust.edu.cn/cas/login",
            data=login_form,
            allow_redirects=False
        )
        try:
            return login_post.headers['Location']
        except:
            raise ConnectionRefusedError("---HustAuth Failed---")

    def _encrypt(self) -> tuple:
        response = self.session.post('https://pass.hust.edu.cn/cas/rsa')
        public_key = RSA.import_key(b64decode(json.loads(response.text)['publicKey']))
        cipher = PKCS1_v1_5.new(public_key)
        encrypted_u = b64encode(cipher.encrypt(self.uid.encode())).decode()
        encrypted_p = b64encode(cipher.encrypt(self.pwd.encode())).decode()
        return encrypted_u, encrypted_p
    
    def _decaptcha(self) -> str:
        captcha_img = self.session.get('https://pass.hust.edu.cn/cas/code', stream=True)
        log.debug('decaptching...')
        img_list = []
        with Image.open(BytesIO(captcha_img.content)) as img_gif:
            for i in range(img_gif.n_frames):
                img_gif.seek(i)
                img_list.append(img_gif.copy().convert('L'))
        width,height = img_list[0].size
        img_merge = Image.new(mode='L',size=(width,height),color=255)
        for pos in [(x,y) for x in range(width) for y in range(height)]:
            if sum([img.getpixel(pos) < 254 for img in img_list]) >= 3:
                img_merge.putpixel(pos,0)
        try:
            captcha_code = pytesseract.image_to_string(img_merge, config='-c tessedit_char_whitelist=0123456789 --psm 6').strip()
        except pytesseract.TesseractNotFoundError:
            log.fatal('tesseract is not installed !!', exc_info=True)
            raise EnvironmentError('USE sudo apt install tesseract-ocr OR go to https://tesseract-ocr.github.io/tessdoc/Downloads.html')
        log.debug('captcha_code:{}'.format(captcha_code.strip()))
        return captcha_code



