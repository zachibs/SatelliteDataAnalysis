from generateFinalData import generate
from pushToInfluxDB import push_to_db
import time
import random


def main():
    while(True):
        push_to_db()
        time_to_sleep = random.randint(2400, 3600)
        print("\n")
        print("--------------------------------------------------------------------------")
        print(f"\t\t\tSleeping {time_to_sleep} seconds")
        print("--------------------------------------------------------------------------")
        print("\n")
        time.sleep(time_to_sleep)


if __name__ == "__main__":
    main()
