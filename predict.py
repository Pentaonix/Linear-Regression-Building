import numpy as np  
from functions import *
[X, y] = Loadtxt("data.txt")
#Predict using Mean Normalization
[X, mu, s] = Normalize(X)
[Theta, J_hist] = GradientDescent(X,y,0.1,400)
input = np.array([19,2790])
input = (input-mu)/s
#Lưu ý sửa lại x0 = 1
input[0] = 1
predict1 = predict(input,Theta)
print("Predict using Mean Normalization: %.2f$"%(predict1))

#Predict using Normal Equation
Theta2 = NormEqn(X,y)
input2 = np.array([19,2790])
predict2 = predict(input2,Theta2)
print("Predict using Normal Equation: %.2f$"%(predict2))