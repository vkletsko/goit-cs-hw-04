import multiprocessing
import time

def search_in_file(file_path, keywords, queue):
    result = {keyword: [] for keyword in keywords}
    try:
        with open(file_path, "r") as file:
            text = file.read()
            for keyword in keywords:
                if keyword in text:
                    result[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    queue.put(result)


def multiprocess_file_search(file_paths, keywords):
    processes = []
    queue = multiprocessing.Queue()
    result = {keyword: [] for keyword in keywords}

    for file_path in file_paths:
        process = multiprocessing.Process(
            target=search_in_file, args=(file_path, keywords, queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not queue.empty():
        partial_result = queue.get()
        for keyword in partial_result:
            result[keyword].extend(partial_result[keyword])

    return result


if __name__ == "__main__":
    keywords = ["keyword_1", "keyword_2"]
    file_paths = ["./text/file_1.txt", "./text/file_2.txt", "./text/file_3.txt", "./text/file_4.txt", "./text/file_5.txt"]

    start_time = time.time()
    result = multiprocess_file_search(file_paths, keywords)
    end_time = time.time()

    print(f"Results: {result}")
    print(f"Duration: {end_time - start_time} seconds")