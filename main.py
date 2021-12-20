import App
import time
import config


class Main:
    def __init__(self):
        self.running = False
        self.FRAME_CAP = 60
        self.TICK_CAP = 30
        self.xSize = 1000
        self.ySize = 600

    def start(self):
        self.running = True
        self.app = App.App(self)
        self.app.tk.title("space invader")
        self.app.tk.protocol("WM_DELETE_WINDOW", self.stop)
        self.loop()

    def stop(self):
        self.running = False

    def exit(self):
        self.app.tk.destroy()
        exit(0)

    def loop(self):
        lastTickTime = time.time_ns()
        lastRenderTime = time.time_ns()
        tickTime = 1000000000.0 / self.TICK_CAP
        renderTime = 1000000000.0 / self.FRAME_CAP
        ticks = 0
        frames = 0

        timer = current_millis()

        while self.running:
            if self.app.tk.winfo_exists():
                pass
            else:
                exit()
            if time.time_ns() - lastTickTime > tickTime:
                lastTickTime += tickTime
                self.update()
                ticks += 1
            elif time.time_ns() - lastRenderTime > renderTime:
                lastRenderTime += renderTime
                self.draw()
                frames += 1
            else:
                time.sleep(1/1000)

            if current_millis() - timer > 1000:
                timer += 1000
                print(ticks, " ticks, ",frames," fps" )
                ticks = 0
                frames = 0

        self.exit()

    def update(self):
        self.app.update()

    def draw(self):
        self.app.draw()


def current_millis():
    return round(time.time() * 1000)


def current_nano():
    return time.time_ns()


if __name__ == "__main__":
    main = Main()
    main.start()
