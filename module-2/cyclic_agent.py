import spade
import asyncio

class CyclicBehaviour(spade.behaviour.CyclicBehaviour):
    async def on_start(self) -> None:
        self.count = 0
        print("on start")

    async def run(self) -> None:
        self.count += 1
        print(f"run {self.count}")
        await asyncio.sleep(1)
        if self.count == 10:
            self.kill()

    async def on_end(self) -> None:
        print("on end")


class CyclicAgent(spade.agent.Agent):
    async def setup(self):
        self.behaviour = CyclicBehaviour()
        self.add_behaviour(self.behaviour)

        print("Hello World! I'm agent {}".format(str(self.jid)))

async def main():
    agent = CyclicAgent("agent1@vitorias-air.lan", "admin")
    
    await agent.start()
    
    # await dummy.stop()
    # if dummy.is_alive():
    #    print("is alive")

    while not agent.behaviour.is_killed():
        await asyncio.sleep(1)

if __name__ == "__main__":
    spade.run(main())