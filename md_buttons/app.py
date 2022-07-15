from fastapi import FastAPI, Query, Request, Response
from fastapi.templating import Jinja2Templates
from pydantic.color import Color
from PIL import ImageFont


class SVGImageResponse(Response):
    media_type = "image/svg+xml"


HTTP_CACHE_TTL = 24 * 60 * 3600

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/button.svg", response_class=SVGImageResponse)
def get_button(
    request: Request,
    text: str = Query(),
    font_size: int = Query(32, alias="fs"),
    background_color: Color = Query(Color("#2ecc71"), alias="bg"),
    foreground_color: Color = Query(Color("#ffffff"), alias="fg"),
    padding_x: int = Query(20, alias="px"),
    padding_y: int = Query(30, alias="py"),
    border_radius: int = Query(5, alias="br"),
):
    font = ImageFont.truetype("Arial.ttf", font_size)
    width, height = font.getsize(text)
    width += padding_x
    height += padding_y

    padding_left = int(padding_x / 2)

    return templates.TemplateResponse(
        "button.svg.jinja2",
        {
            "request": request,
            "text": text,
            "font_size": font_size,
            "width": width,
            "height": height,
            "padding_left": padding_left,
            "border_radius": border_radius,
            "background_color": background_color,
            "foreground_color": foreground_color,
        },
        media_type="image/svg+xml",
        headers={"Cache-Control": f"public, max-age={HTTP_CACHE_TTL}, immutable"},
    )
