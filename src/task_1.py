import threading
import os
import time

def search_in_file(file_path, keywords, result):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            for keyword in keywords:
                if keyword in text:
                    result[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")


def threaded_file_search(file_paths, keywords):
    threads = []
    result = {keyword: [] for keyword in keywords}

    for file_path in file_paths:
        thread = threading.Thread(
            target=search_in_file, args=(file_path, keywords, result)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


keywords = ["keyword_1", "keyword_2"]
file_paths = ["./text/file_1.txt", "./text/file_2.txt", "./text/file_3.txt", "./text/file_4.txt", "./text/file_5.txt"]

start_time = time.time()
result = threaded_file_search(file_paths, keywords)
end_time = time.time()

print(f"Results: {result}")
print(f"Duration: {end_time - start_time} seconds")