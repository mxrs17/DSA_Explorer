from heap_logic import MinHeap


def test_heap():

    heap = MinHeap()

    heap.insert((5, "Task A"))
    heap.insert((2, "Task B"))
    heap.insert((8, "Task C"))

    assert heap.extract_min() == (2, "Task B")

    assert heap.extract_min() == (5, "Task A")

    assert heap.extract_min() == (8, "Task C")

    assert heap.is_empty() == True

    print("Heap tests passed ✔")


if __name__ == "__main__":

    test_heap()