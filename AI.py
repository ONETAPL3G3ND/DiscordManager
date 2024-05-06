import json
import g4f

class AI:
    def __init__(self):
        self.config = []
        self.chat = {}
        self._chat: dict[int, list] = self.chat
        with open("config.json", "r") as file:
            self.config = json.load(file)

        with open("chat.json", "r") as file:
            self.chat = json.load(file)

    def DumpJson(self) -> None:
        with open("config.json", "w") as file:
            json.dump(self.config, file)

        with open("chat.json", "w") as file:
            json.dump(self.chat, file)

    async def CreateMessage(self, id: int, msg: str) -> str:
        self._chat[str(id)].append({"role": "user", "content": msg})

        responce = await g4f.ChatCompletion.create_async(model=g4f.models.gpt_4_turbo, messages=self._chat[str(id)])

        self._chat[str(id)].append({"role": "assistant", "content": responce})

        with open("chat.json", "w") as file:
            json.dump(self._chat, file)
        return responce

