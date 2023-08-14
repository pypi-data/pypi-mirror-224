from typing import Any

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from .logger import logger


class MessageLogger(BaseMiddleware):
    logger = logger

    async def on_pre_process_message(self, message: types.Message, data: dict) -> Any:
        await self.logger.send_message(data=message, text=message.text)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.logger.send_message(data=query, text=query.data)
