"""
Drop old messages from a thread if the thread is too long.

"""
import logging
from typing import Optional

from totokenizers.factories import TotoModelInfo, Totokenizer
from totokenizers.model_info import ChatModelInfo
from totokenizers.schemas import Chat

from ..errors import InvalidModel, NotEnoughTokens

logging.basicConfig(level=logging.DEBUG)
class MessageDropper:
    def __init__(self, model: str):
        self.tokenizer = Totokenizer.from_model(model)
        self.model_info = TotoModelInfo.from_model(model)
        if not isinstance(self.model_info, ChatModelInfo):
            raise InvalidModel(self.tokenizer.model)
        self.logger = logging.getLogger(__name__)

    def run(
        self, thread: Chat, functions: Optional[list[dict]] = None
    ) -> Chat:
        """
        Drop enough messages so the token count is below the model's maximum.

        Skip the system message, as that's always the first message.
        """
        self.logger.info("Running MessageDropper on thread: %s", len(thread))
        thread = thread.copy()
        if len(thread) == 0:
            return thread
        index = 1 if thread[0]["role"] == "system" else 0
        while (
            token_count := self.tokenizer.count_chatml_tokens(thread, functions)
        ) > self.model_info.max_tokens:
            print(
                "Thread has %d tokens, which is more than the maximum of %d",
                token_count,
                self.model_info.max_tokens,
            )
            if len(thread) == 1:
                raise NotEnoughTokens(token_count, self.model_info.max_tokens)
            if len(thread) == 2:
                if thread[0]["role"] == "system":
                    raise NotEnoughTokens(token_count, self.model_info.max_tokens)
                else:
                    thread.pop(0)
                    continue
            print("Dropping message: %s", thread[1])
            thread.pop(index)
        print("Finished running MessageDropper on thread: %s", len(thread))
        return thread
