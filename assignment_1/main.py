from functions import *

# Scale Factors
alpha1 = 1
beta1 = 1
alpha2 = 0.01
beta2 = 0.5

# Feature Vectors of the Computers
vectorA = [3.06, 500, 6]
vectorB = [2.68, 320, 4]
vectorC = [2.92, 640, 6]

# Feature Vectors of Attributes
processorSpeedVec = [3.06, 2.68, 2.92]
diskSizeVec = [500, 320, 640]
mainMemSizeVec = [6, 4, 6]

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

# Length of the feature vectors with alpha = 0.01 and beta = 0.5
lengthA2 = calculate_length_of_vector(vectorA, alpha2, beta2)
lengthB2 = calculate_length_of_vector(vectorB, alpha2, beta2)
lengthC2 = calculate_length_of_vector(vectorC, alpha2, beta2)

# Angles between the feature vectors with alpha = 1 and beta = 1
angleAB1 = math.acos(dotProductAB1 / (lengthA1 * lengthB1)) * (180.0 / math.pi)
angleBC1 = math.acos(dotProductBC1 / (lengthB1 * lengthC1)) * (180.0 / math.pi)
angleAC1 = math.acos(dotProductAC1 / (lengthA1 * lengthC1)) * (180.0 / math.pi)

# Angles between the feature vectors with alpha = 0.01 and beta = 0.5
angleAB2 = math.acos(dotProductAB2 / (lengthA2 * lengthB2)) * (180.0 / math.pi)
angleBC2 = math.acos(dotProductBC2 / (lengthB2 * lengthC2)) * (180.0 / math.pi)
angleAC2 = math.acos(dotProductAC2 / (lengthA2 * lengthC2)) * (180.0 / math.pi)

# Average of every component
avgProcessorSpeed = (vectorA[0] + vectorB[0] + vectorC[0]) / 3
avgDiskSize = (vectorA[1] + vectorB[1] + vectorC[1]) / 3
avgMainMemSize = (vectorA[2] + vectorB[2] + vectorC[2]) / 3

# Make Disk Size and Main Memory Size Inversily Proportional
invPropDiskSize = 1 / avgDiskSize
invPropMainMem = 1 / avgMainMemSize

# Dot Products of feature Vectors with alpha = invPropDiskSize and beta = invPropMainMem
dotProductAB3 = calculate_dot_product(vectorA, vectorB, invPropDiskSize, invPropMainMem)
dotProductBC3 = calculate_dot_product(vectorB, vectorC, invPropDiskSize, invPropMainMem)
dotProductAC3 = calculate_dot_product(vectorA, vectorC, invPropDiskSize, invPropMainMem)

# Length of the feature vectors with alpha = invPropDiskSize and beta = invPropMainMem
lengthA3 = calculate_length_of_vector(vectorA, invPropDiskSize, invPropMainMem)
lengthB3 = calculate_length_of_vector(vectorB, invPropDiskSize, invPropMainMem)
lengthC3 = calculate_length_of_vector(vectorC, invPropDiskSize, invPropMainMem)

# Angles between the feature vectors with alpha = invPropDiskSize and beta = invPropMainMem
angleAB3 = math.acos(dotProductAB3 / (lengthA3 * lengthB3)) * (180.0 / math.pi)
angleBC3 = math.acos(dotProductBC3 / (lengthB3 * lengthC3)) * (180.0 / math.pi)
angleAC3 = math.acos(dotProductAC3 / (lengthA3 * lengthC3)) * (180.0 / math.pi)

# Normalizing the vectors
avgVector = [avgProcessorSpeed, avgDiskSize, avgMainMemSize]
normalizedVectorA = normalizeVector(vectorA, avgVector)
normalizedVectorB = normalizeVector(vectorB, avgVector)
normalizedVectorC = normalizeVector(vectorC, avgVector)

# Ein kleiner Winkel zwischen Vektoren bedeutet grundsätzlich, dass sie sich ziemlich ähnlich bzw. ziemlich ähnlich ausgerichtet sind
#

# Dot product of the normalized Vectors
dotProductNormVecAB = calculate_dot_product(normalizedVectorA, normalizedVectorB, 1, 1)
dotProductNormVecBC = calculate_dot_product(normalizedVectorB, normalizedVectorC, 1, 1)
dotProductNormVecAC = calculate_dot_product(normalizedVectorA, normalizedVectorC, 1, 1)

# Length of normalized Vectors
lengthNormVecA = calculate_length_of_vector(normalizedVectorA, 1, 1)
lengthNormVecB = calculate_length_of_vector(normalizedVectorB, 1, 1)
lengthNormVecC = calculate_length_of_vector(normalizedVectorC, 1, 1)

# Angles between the normalized Vectors
angleNormVecAB = math.acos(dotProductNormVecAB / (lengthNormVecA * lengthNormVecB)) * (
    180.0 / math.pi
)
angleNormVecBC = math.acos(dotProductNormVecBC / (lengthNormVecB * lengthNormVecC)) * (
    180.0 / math.pi
)
angleNormVecAC = math.acos(dotProductNormVecAC / (lengthNormVecA * lengthNormVecC)) * (
    180.0 / math.pi
)

# user vector
userVector = [4.0, 2.0, 5.0]

# average user rating
averageUserRating = sum(userVector) / len(userVector)

# Normalizing the vector for user ratings
normalizedUserVec = normalizeVector(
    userVector, [averageUserRating, averageUserRating, averageUserRating]
)

# User weights
userWeights = getWeight(userVector, 5)

# Generate a user profile the feature vector
userProfile = []

userProfileProcessor = generateUserProfile(userWeights, processorSpeedVec)
userProfileDiskSize = generateUserProfile(userWeights, diskSizeVec)
userProfileMainMemSize = generateUserProfile(userWeights, mainMemSizeVec)

userProfile.append(userProfileProcessor)
userProfile.append(userProfileDiskSize)
userProfile.append(userProfileMainMemSize)

print(userProfile)
