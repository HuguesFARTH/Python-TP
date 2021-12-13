import App
import Time
running = False
FRAME_CAP = 60
TICK_CAP = 60

def init():
    app = App()
    app.tk.title("")
    app.tk.mainloop()

def start():
    pass

def stop():

	lastTickTime = time.time_ns()
	lastRenderTime = time.time_ns()

    tickTime = 1000000000.0 / 60.0;
	renderTime = 1000000000.0 / FRAME_CAP;

    ticks = 0
    frames = 0

    timer = current_millis()

    while running:
        if (time.time_ns() - lastTickTime > tickTime):
            lastTickTime += tickTime
            update()
            tick +=1
        elif (time.time_ns() - lastRenderTime > renderTime):
            lastRenderTime += renderTime
            render()
            frames += 1
        else:
            time.sleep(1/1000)

        if current_millis() - timer > 1000:
            timer += 1000
            print(tick, " ticks, ",frames," fps" )
            ticks = 0
            frames = 0
    exit()

def exit():
    pass

def loop():
    pass

def update():
    pass

def render():
    pass

def current_millis():
    return round(time.time() * 1000)

def current_nano():
    return time.time_ns()

init()
