# Finding the largest square inside a 2d array

def findLargestSquareSize(samples):
    # Write your code here
    square = []
    for i in range(len(samples)):
        t = []
        for j in range(len(samples[0])):
            if i == 0 or j == 0:
                t.append(samples[i][j])
            else:
                t.append(0)
        square.append(t)
        
    maxLen = 0
    for i in range(1, len(samples)):
        for j in range(1, len(samples[0])):
            if (samples[i][j] == 1):
                square[i][j] = min(square[i][j - 1], square[i - 1][j], square[i - 1][j - 1]) + 1
                if square[i][j] > maxLen:
                    maxLen = square[i][j]
            else:
                square[i][j] = 0 
            
    return maxLen