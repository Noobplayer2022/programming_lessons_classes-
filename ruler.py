
# i have 16GB of RAM python use 1byte per character, that means
# 16GB = 31 for best performance

#  using psutil package we can monitor memory usage.
import sys
import psutil 

n = int(sys.argv[1])
ruler = ' '

for i in range(1, n + 1):
    ruler = ruler + str(i) + ruler
    
    # Monitor memory usage
    memory_used = psutil.virtual_memory().percent
    print(f"Step {i}: Memory Usage = {memory_used}%")

    if memory_used > 90:  # Stop before crashing
        print("Warning: Memory usage too high! Stopping...")
        break

print("Final string length:", len(ruler))
