from typing import Tuple
from fastapi import FastAPI, Query, Request, Response
from fastapi.templating import Jinja2Templates
from pydantic.color import Color
from PIL import ImageFont

from md_buttons.settings import settings


class SVGImageResponse(Response):
    media_type = "image/svg+xml"


app = FastAPI()
templates = Jinja2Templates(directory="templates")


def guess_font_size(width: int, padding_x: int, text: str) -> Tuple[int, int]:
    font_size = 1
    while True:
        font = ImageFont.truetype(settings.font, font_size)
        text_width, text_height = font.getsize(text)
        if text_width + padding_x > width:
            break
        font_size += 1
    return font_size, text_height


@app.get("/button.svg", response_class=SVGImageResponse)
def get_button(
    request: Request,
    text: str = Query(),
    width: int = Query(200, ge=0, alias="w"),
    background_color: Color = Query(Color("#2ecc71"), alias="bg"),
    foreground_color: Color = Query(Color("#ffffff"), alias="fg"),
    padding_x: int = Query(20, ge=0, alias="px"),
    padding_y: int = Query(30, ge=0, alias="py"),
    border_radius: int = Query(5, ge=0, alias="br"),
):
    font_size, height = guess_font_size(width, padding_x, text)
    width += padding_x
    height += padding_y

    return templates.TemplateResponse(
        "button.svg.jinja2",
        {
            "request": request,
            "text": text,
            "font_size": font_size,
            "width": width,
            "height": height,
            "border_radius": border_radius,
            "background_color": background_color,
            "foreground_color": foreground_color,
        },
        media_type="image/svg+xml",
        headers={"Cache-Control": f"public, max-age={settings.http_cache_ttl}, immutable"},
    )
