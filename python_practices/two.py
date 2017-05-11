# file two.py
import one

print("top-level in two.py")
one.func()

print "__name__ =" + " " + __name__