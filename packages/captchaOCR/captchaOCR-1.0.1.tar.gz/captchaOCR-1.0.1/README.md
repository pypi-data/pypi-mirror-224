# captchaOCR

* 用于爬虫的验证码识别模块，[Github link](https://github.com/Do1e/captchaOCR)，[PyPI link](https://pypi.org/project/captchaOCR/)。

## 安装

```bash
python setup.py install
```

或者

```bash
pip install captchaOCR
```

## 使用

```python
from captchaOCR import CaptchaOCR
ocr = CaptchaOCR()
captchaImg = (bytes, str, pathlib.PurePath, Image.Image)()
text = ocr.get_text(captchaImg)
```

## 补充

* 本项目基于[sml2h3/ddddocr](https://github.com/sml2h3/ddddocr)编写，在此表示感谢。
