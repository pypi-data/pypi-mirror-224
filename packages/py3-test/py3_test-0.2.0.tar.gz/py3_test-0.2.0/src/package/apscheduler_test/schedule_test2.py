import time

import schedule


def job():
    print("I'm working...")


# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

schedule.every(1)

while True:
    schedule.run_pending()
    time.sleep(1)
