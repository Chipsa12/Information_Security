from algorithm import main

from aiohttp import web
import aiohttp_cors


async def getAnswer(request):
    try:
        post = await request.json()
        assert post.get("input_text")
        assert post.get("type_mode")
        input_text, type_mode = post.get("input_text"), post.get("type_mode")
        res = main(input_text, type_mode) if main(input_text, type_mode) else "Ошибка обработки данных"
        return web.json_response({"answer": res})
    except AssertionError:
        return web.json_response({"answer": 'Ошибка получения данных'})

app = web.Application()
app.router.add_route("POST", "/api/lab3", getAnswer)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            allow_headers="*"
    )
})

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=9000)