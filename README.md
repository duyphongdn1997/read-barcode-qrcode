## Barcode/Qrcode Decoder
Barcode/Qrcode Decoder is a simple FastAPI using zbar to decode barcode/qrcode from a image.

## Installation

### Docker Image
(Recommendation)

```bash
docker-compose build
docker-compose up -d
```

### Local installation

Make suer that you have python installed on you machine
- Create a virtualenv

```bash
virtualenv venv
```

- Install dependencies

```bash
python -m pip install -r requirements.txt
```

- Run the app
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8501
```

There will be a fastapi running on your port 8501 after you finish those steps above.

## Usage

- View all API Docs at [http://0.0.0.0:8501/api/v1/docs](http://0.0.0.0:8501/api/v1/docs)
- Sample API request body:
```
POST /api/v1/barcode_decode HTTP/1.1
Host: 0.0.0.0:8501
Content-Length: 
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="image"; filename="filename.jpg"
Content-Type: image/jpeg

(data)
----WebKitFormBoundary
```

- Sample APi response:

```
{
    "message_code": 0,
    "message": "API success",
    "data": {
        "has_code": false,
        "codes": [],
        "bar_image": "{base64image}"
    }
}
```

You maybe decode base 64 by the function below:
```python
from base64 import b64decode
from typing import Text

import cv2
import numpy as np


def read_encode_image(image_str: Text) -> np.ndarray:
    """
    Get encoded image from base 64 image.
    Args:
        image_str: base64 string

    Returns:

    """
    nparr = np.frombuffer(b64decode(image_str), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Tree Directory
```
├── app
│   ├── api
│   │   ├── errors
│   │   │   ├── error_message.py
│   │   │   ├── http_error.py
│   │   │   ├── __init__.py
│   │   │   └── validation_error.py
│   │   ├── helpers
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   └── image.py
│   │   ├── responses
│   │   │   ├── base.py
│   │   │   └── __init__.py
│   │   ├── routes
│   │   │   ├── api.py
│   │   │   ├── barcode_api.py
│   │   │   └── __init__.py
│   │   ├── serializers
│   │   │   └── __init__.py
│   │   └── services
│   │       ├── barcode_decode.py
│   │       └── __init__.py
│   ├── core
│   │   ├── config.py
│   │   ├── constant.py
│   │   ├── __init__.py
│   │   └── logging.py
│   ├── frontend
│   │   ├── static
│   │   │   ├── css
│   │   │   ├── fonts
│   │   │   ├── images
│   │   │   └── js
│   │   └── templates
│   │       └── index.html
│   ├── __init__.py
│   ├── logger
│   │   ├── logger.log
│   │   └── logger.py
│   ├── main.py
│   ├── resources
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_api
│   │   │   └── __init__.py
│   │   └── test_services
│   │       └── __init__.py
│   └── utils
├── docker-compose.yml
├── Dockerfile
├── output
├── README.md
├── requirements.txt
├── src
│   ├── contants.py
│   ├── __init__.py
│   ├── utils
│   │   ├── draw_product_bbox.py
│   │   ├── __init__.py
│   │   └── utils.py
│   └── zbar
│       ├── __init__.py
│       └── zbar.py
└── utils
    └── simfang.ttf

```