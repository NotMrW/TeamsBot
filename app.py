import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from bot import HelloBot

APP_ID = os.getenv("MICROSOFT_APP_ID", "c99e75a7-369f-4c7e-a615-60068a94f79d")
APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "")

adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

bot = HelloBot()

async def messages(req: web.Request) -> web.Response:
    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")
    response = await adapter.process_activity(activity, auth_header, bot.on_turn)
    return web.Response(status=201)


app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=3978)
