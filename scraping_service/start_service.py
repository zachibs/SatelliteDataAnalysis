from generateFinalData import generate
from pushToInfluxDB import push_to_db
import time


def main():
    while(True):
        push_to_db()
        print("\n")
        print("--------------------------------------------------------------------------")
        print("\t\t\tSleeping 1 hour")
        print("--------------------------------------------------------------------------")
        print("\n")
        time.sleep(3600)


if __name__ == "__main__":
    main()
