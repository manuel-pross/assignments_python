import math


def calculate_dot_product(vector1, vector2, alpha, beta):
    sum = 0
    for i in range(len(vector1)):
        if i == 0:
            sum += vector1[i] * vector2[i]
        elif i == 1:
            sum += (vector1[i] * alpha) * (vector2[i] * alpha)
        elif i >= 2:
            sum += (vector1[i] * beta) * (vector2[i] * beta)
    return sum


def calculate_length_of_vector(vector, alpha, beta):
    sum = 0
    for i in range(len(vector)):
        if i == 0:
            sum += pow(vector[i], 2)
        elif i == 1:
            sum += pow(vector[i] * alpha, 2)
        elif i >= 2:
            sum += pow(vector[i] * beta, 2)
    return math.sqrt(sum)


def normalizeVector(vector, averages):
    normalizedVector = []
    for i in range(len(vector)):
        normalizedVector.append(vector[i] - averages[i])
    return normalizedVector


def getWeight(vector, maxPossibleRank):
    weightVector = []
    for i in range(len(vector)):
        weightVector.append(vector[i] / maxPossibleRank)
    return weightVector


def generateUserProfile(weights, features):
    sum = 0
    for i in range(len(weights)):
        sum += weights[i] * features[i]
    return sum
