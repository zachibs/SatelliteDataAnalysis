from generateFinalData import generate
from pushToInfluxDB import push_to_db
import time


def main():
    while(True):
        push_to_db()
        print("\n")
        print("--------------------------------------------------------------------------")
        print("\t\t\tSleeping 10 minutes")
        print("--------------------------------------------------------------------------")
        print("\n")
        time.sleep(600)


if __name__ == "__main__":
    main()
