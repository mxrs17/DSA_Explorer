from stack import Stack

def test_stack():

    s = Stack()


    s.push(10)
    s.push(20)
    s.push(30)


    assert s.pop() == 30
    assert s.pop() == 20
    assert s.pop() == 10


    assert s.is_empty() == True

    print("Stack tests passed ✔")

if __name__ == "__main__":
    test_stack()