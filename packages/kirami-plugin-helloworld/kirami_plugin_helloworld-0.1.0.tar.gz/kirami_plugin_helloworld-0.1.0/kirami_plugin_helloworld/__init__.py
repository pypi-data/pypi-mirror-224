from typing import NoReturn

from kirami import on_fullmatch
from kirami.typing import Event, Matcher

I18N = {
    "hello": "world",
    "你好": "世界",
}


@on_fullmatch(*tuple(I18N), ignorecase=True)
async def _(matcher: Matcher, event: Event) -> NoReturn:
    key = event.get_plaintext().lower()
    await matcher.finish(I18N[key])
