from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

class HelloBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        text = turn_context.activity.text.lower()

        if "hello" in text:
            await turn_context.send_activity("hello")
        else:
            await turn_context.send_activity("try saying 'hello")
