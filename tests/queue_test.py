from queue_logic import Queue  

def test_queue():

    q = Queue()


    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)


    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() == 30

    print("Queue tests passed ✔")

if __name__ == "__main__":
    test_queue()