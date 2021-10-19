
from aiohttp import web
import aiohttp_cors
from change_lab2 import main


async def getAnswer(request):
    post = await request.json()
    input_text = post.get("input_text")
    type = post.get("type")
    res = main(input_text, type)
    print(res)
    return web.json_response({"result": res})

app = web.Application()
app.router.add_route("POST", "/api/lab2", getAnswer)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            allow_headers="*"
    )
})

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=9000)