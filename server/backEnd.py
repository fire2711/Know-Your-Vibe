
class Song:
    def __init__(self, name= "", artists= "Unknown Artist", bpm= 0, length= 0, album= "", popularity= 0):
        self.name = name
        self.artists = artists
        self.bpm = bpm
        self.length = length
        self.album = album
        self.popularity = popularity

    def display(self):
         if hasattr(self, 'artists'):
            print(self.name, ''.join(self.artists), self.bpm, self.length, self.album, self.popularity)
         else:
            print(self.name, "Unknown Artist", self.bpm, self.length, self.album, self.popularity)

bpms = {}
#songs = list(bpms.keys())
least_ordered = []
max_ordered = []

def insert_song_BackEnd(song, bpm):
    if bpm in bpms and song not in bpms[bpm]:
        bpms[bpm].append(song)
    else:
        bpms[bpm] = [song]
        least_ordered.append(bpm)
        max_ordered.append(bpm)

#-------------------------------------------------

def heapify(arr, n, i):         #https://www.geeksforgeeks.org/heap-sort/
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest] , arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#-----------------------------------------------------

def partition(arr, low, high):      #https://www.geeksforgeeks.org/quick-sort/
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

#------------------------------------------------------

def use_quick_sort():
    n = len(least_ordered)
    quick_sort(least_ordered, 0, n -1)

    #sorted_songs = [(bpm, bpms[bpm]) for bpm in least_ordered]
    return least_ordered

def use_heap_sort():
    heap_sort(max_ordered)

    #sorted_songs = [(bpm, bpms[bpm]) for bpm in max_ordered]
    return max_ordered