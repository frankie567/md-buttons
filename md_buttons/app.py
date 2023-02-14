from typing import Optional, Tuple

from asgi_prometheus import PrometheusMiddleware
from fastapi import FastAPI, Query, Request, Response
from fastapi.templating import Jinja2Templates
from PIL import ImageFont
from pydantic.color import Color

from md_buttons.settings import settings


class SVGImageResponse(Response):
    media_type = "image/svg+xml"


app = FastAPI()
app.add_middleware(
    PrometheusMiddleware, metrics_url="/metrics", group_paths=["/button.svg"]
)
templates = Jinja2Templates(directory="templates")


def get_text_size(text: str, font_size: int) -> Tuple[int, int]:
    font = ImageFont.truetype(settings.font, font_size)
    text_width, text_height = font.getsize(text)
    return text_width, text_height


def guess_font_size(
    width: int, padding_x: int, height: int, padding_y: int, text: str
) -> int:
    font_size = 1
    while True:
        text_width, text_height = get_text_size(text, font_size)
        if text_width + padding_x > width or text_height + padding_y > height:
            break
        font_size += 1
    return font_size


@app.get("/button.svg", response_class=SVGImageResponse)
def get_button(
    request: Request,
    text: str = Query(),
    width: int = Query(100, ge=0, alias="w"),
    height: int = Query(30, ge=0, alias="h"),
    background_color: Color = Query(Color("#2ecc71"), alias="bg"),
    foreground_color: Color = Query(Color("#ffffff"), alias="fg"),
    padding_x: int = Query(20, ge=0, alias="px"),
    padding_y: int = Query(20, ge=0, alias="py"),
    border_radius: int = Query(5, ge=0, alias="br"),
    font_size: Optional[int] = Query(None, ge=0, alias="fs"),
):
    if font_size is None:
        font_size = guess_font_size(width, padding_x, height, padding_y, text)

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
        headers={
            "Cache-Control": f"public, max-age={settings.http_cache_ttl}, immutable"
        },
    )
