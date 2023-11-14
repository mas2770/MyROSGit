#!/usr/bin/env python3
import time

def main():
    while True:
    	current_time = time.strftime("%H:%M:%S", time.localtime()) 
    	print("Текущее время:", current_time)
    	time.sleep(5) 


if __name__ == "__main__":
    main()
