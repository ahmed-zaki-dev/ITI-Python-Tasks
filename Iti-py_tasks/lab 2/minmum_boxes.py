#You have n packs of apples and m boxes. Each pack i contains apple[i] apples,
#and each box i can hold up to capacity[i] apples.
#You need to find the minimum number of boxes needed to hold all the apples
#from the n packs.

def minimum_boxes(apple, capacity):
    total_apples = sum(apple)
    
    capacity.sort(reverse=True)
    
    boxes_count = 0
    
    for i in capacity:
        if total_apples <= 0:
            break
        total_apples -= i
        boxes_count += 1
        
    return boxes_count

# Test Case:
# apple = [4, 2, 3]
# capacity = [4, 3, 1, 5, 2]

print(minimum_boxes([4, 3, 2], [1, 3, 4, 5, 2]))
