def bucketSort(array):
    bucket = []


    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
         bucket[i] = sorted(bucket[i])
         print(bucket)

    k = 0
    for i in range(len(array)):
        print(f'i = {i}')
        for j in range(len(bucket[i])):
             print(f'j = {j}')
             array[k] = bucket[i][j]
             k += 1
    return array

list = [.42, .33, .32, .52, .37, .47, .51]

print(bucketSort(list))
