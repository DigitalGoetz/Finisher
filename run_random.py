import os
import random
import time
import uuid

useRandom = str(os.environ.get("RANDOM", "yes")).lower()
timeLimit = int(os.environ.get("LIMIT", "20"))

id = uuid.uuid4()
print(f"{id}: Running")

if useRandom == "yes":
    duration = random.randint(1, timeLimit)
else:
    duration = timeLimit

print(f"{id}: Sleeping for {duration} seconds")

time.sleep(duration)
print(f"{id} Completed")
