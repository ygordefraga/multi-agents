import spade
import threading
import time


class OnShotAgent(spade.agent.Agent):
    async def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))
        thread = threading.Thread(target=self.behaviour)
        thread.start()
    
    def behaviour(self):
        time.sleep(5)
        print("Behaviour")

async def main():
    agent = OnShotAgent("agent1@vitorias-air.lan", "admin")
    await agent.start()


if __name__ == "__main__":
    spade.run(main())