from ceylon import Agent, on_message
from loguru import logger

from data.message import Message
from data.user_details import UserDetails


class ProcessAgent(Agent):

    @on_message(UserDetails)
    async def on_user_details(self, user_details: UserDetails):
        logger.info(f"Received user details: {user_details}")

    @on_message(Message)
    async def on_chat_message(self, message: Message, agent_id: "str", time: "int"):
        logger.info(f"Received message {message} from {agent_id} at {time}")

    async def run(self, inputs: "bytes"):
        logger.info(f"Process agent running with inputs: {inputs}")
