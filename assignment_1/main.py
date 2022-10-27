from functions import *

# Scale Factors
alpha1 = 1
beta1 = 1
alpha2 = 0.01
beta2 = 0.5

# Fature Vectors of the Computers
vectorA = [3.06, 500, 6]
vectorB = [2.68, 320, 4]
vectorC = [2.92, 640, 6]

# Dot Products of the feature vectors with alpha = 1 and beta = 1
dotProductAB1 = calculate_dot_product(vectorA, vectorB, alpha1, beta1)
dotProductBC1 = calculate_dot_product(vectorB, vectorC, alpha1, beta1)
dotProductAC1 = calculate_dot_product(vectorA, vectorC, alpha1, beta1)

# Dot Products of the feature vectors with alpha = 0.01 and beta = 0.5
dotProductAB2 = calculate_dot_product(vectorA, vectorB, alpha2, beta2)
dotProductBC2 = calculate_dot_product(vectorB, vectorC, alpha2, beta2)
dotProductAC2 = calculate_dot_product(vectorA, vectorC, alpha2, beta2)

# Length of the feature vectors with alpha = 1 and beta = 1
lengthA1 = calculate_length_of_vector(vectorA, alpha1, beta1)
lengthB1 = calculate_length_of_vector(vectorB, alpha1, beta1)
lengthC1 = calculate_length_of_vector(vectorC, alpha1, beta1)

# Length of the feature vectors with alpha = 1 and beta = 1
lengthA2 = calculate_length_of_vector(vectorA, alpha2, beta2)
lengthB2 = calculate_length_of_vector(vectorB, alpha2, beta2)
lengthC2 = calculate_length_of_vector(vectorC, alpha2, beta2)

# Angles between the feature vectors with alpha = 1 and beta = 1
angleAB1 = math.acos(dotProductAB1 / (lengthA1 * lengthB1))
angleBC1 = math.acos(dotProductBC1 / (lengthB1 * lengthC1))
angleAC1 = math.acos(dotProductAC1 / (lengthA1 * lengthC1))

# Angles between the feature vectors with alpha = 1 and beta = 1
angleAB2 = math.acos(dotProductAB2 / (lengthA2 * lengthB2))
angleBC2 = math.acos(dotProductBC2 / (lengthB2 * lengthC2))
angleAC2 = math.acos(dotProductAC2 / (lengthA2 * lengthC2))

print(angleAB2)
print(angleBC2)
print(angleAC2)
