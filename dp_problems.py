# Finding the largest square inside a 2d array

def findLargestSquareSize(samples):
    # Recreate the square but with only the top row and first column
    square = []
    for i in range(len(samples)):
        t = []
        for j in range(len(samples[0])):
            if i == 0 or j == 0:
                t.append(samples[i][j])
            else:
                t.append(0)
        square.append(t)
    
    # Look through the rows and columns
    maxLen = 0
    for i in range(1, len(samples)):
        for j in range(1, len(samples[0])):
            # If we find a 1, and theres a square created by it and the previous 3 dots, we put a two there.
            # This allows us to build up our square as we iterate over the 2d list.
            if (samples[i][j] == 1):
                square[i][j] = min(square[i][j - 1], square[i - 1][j], square[i - 1][j - 1]) + 1
                if square[i][j] > maxLen:
                    maxLen = square[i][j]
            else:
                square[i][j] = 0 
            
    return maxLen