from hash import main

from aiohttp import web
import aiohttp_cors

async def getAnswer(request):
    try:
        post = await request.json()
        assert post.get("input_text")
        assert post.get("type_mode")
        inputText, typeMode = post.get("input_text"), post.get("type_mode")
        result = main(inputText, typeMode) if main(inputText, typeMode) else "Ошибка обработки данных"
        return web.json_response({"answer": result})
    except AssertionError:
        return web.json_response({"answer": 'Ошибка получения данных'})
    except:
        return web.json_response({"answer": 'Ошибка соединения'})


app = web.Application()
app.router.add_route("POST", "/api/lab4", getAnswer)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            allow_headers="*"
    )
})

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=9000)