def create_string(pages):
    pages_sorted = sorted(set(pages))
    res = []
    start = end = pages_sorted[0]

    for page in pages_sorted[1:]:
        if page != end + 1:
            res.append(f"{start}-{end}" if start != end else str(start))
            start = page
        end = page
    res.append(f"{start}-{end}" if start != end else str(start))
    return ",".join(res)

if __name__ == "__main__":

    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9
    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1] 