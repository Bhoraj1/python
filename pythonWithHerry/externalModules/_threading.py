# import threading
# import time

# def worker(num):
#     print(f"Worker {num} : Started")
#     time.sleep(2)  # Pause for 2 seconds
#     print(f"Worker {num} : Finished")

# threads = []

# # Create and start 3 threads
# for i in range(3):
#     thread = threading.Thread(target=worker, args=(i,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to finish i.e 3 threads.
# for thread in threads:
#     thread.join()

# print("All threads finished")
