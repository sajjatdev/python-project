import math


data = [
    [1, 2, 'Red'],
    [2, 3, 'Blue'],
    [3, 1, 'Red'],
    [6, 5, 'Blue']
]

test_point = [4, 3]

K = 3

# Compute distances
distances = []
for item in data:
    features = item[:-1]
    label = item[-1]

    distance = math.sqrt(sum((features[i] - test_point[i] )**2 for i in range(len(features))))
    distances.append((distance, label))


distances.sort(key=lambda x: x[0])
neighbors = distances[:K]

# Majority vote
votes = {}
for dist, label in neighbors:
    
    votes[label] = votes.get(label, 0) + 1

predicted_label = max(votes,key=votes.get)



print("Neighbors:", neighbors)
print("Votes:", votes)
print("Predicted Class:", predicted_label)
