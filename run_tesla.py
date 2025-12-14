import sys
import commotion

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python run_tesla.py x1 y1 x2 y2 x3 y3")
        sys.exit(1)
    commotion.main(sys.argv[1:])