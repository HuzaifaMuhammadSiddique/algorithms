from main import shortest_path

def testcase1():
    grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 0]
    ]
    
    assert shortest_path(grid)[0] == 5

def testcase2():
    grid = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
           ]
    
    assert shortest_path(grid)[0] == 6

def testcase3():
    grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0]
            ]
    
    assert shortest_path(grid)[0] == 10
    
def testcase4():
    grid = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0]
            ]
    
    assert shortest_path(grid)[0] == 8
    
def main():
    testcase1()
    testcase2()
    testcase3()
    testcase4()
    
    print("ALL TESTS PASSED!")
    
    

if __name__ == "__main__":    
    main()



