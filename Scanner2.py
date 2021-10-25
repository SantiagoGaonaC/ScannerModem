import speedtest
import datetime
s = speedtest.Speedtest()
while True:
    time = datetime.datetime.now().strftime("%H:%M:%S")
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1048576), 2)
    print(
        f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
