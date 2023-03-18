"""API route."""
import io

import numpy as np
from PIL import Image
from fastapi import APIRouter, File, UploadFile
from fastapi.openapi.docs import get_swagger_ui_html

from app.api.responses.base import response
from app.api.services.barcode_decode import barcode_decode_service
from app.logger.logger import configure_logging

logger = configure_logging(__name__)
router = APIRouter()


@router.post("/barcode_decode", response_description="Decode information from an image.")
def invoice_extract_from_image(image: UploadFile = File(...)):
    """Add user data to database."""
    request_object_content = image.file.read()
    logger.debug("Read image ...")
    pil_image = Image.open(io.BytesIO(request_object_content)).convert("RGB")
    open_cv_image = np.array(pil_image)
    image = open_cv_image[:, :, ::-1].copy()
    result = barcode_decode_service.decode(image)
    return response.success_response(data=result)


@router.get("/docs")
async def get_documentation():
    """Get documentation."""
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
