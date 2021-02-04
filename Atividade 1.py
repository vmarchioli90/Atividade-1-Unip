z = ["ma", "pa", "ba", "Urmah", "ba"]
w = ["ca", "fo" "na", "lu", "ta"]
x = [2, 2, 2, 2, 1]
y = []


def agrupar(z,w,x):
    for i in range(len(z)):
        y.append(z[i]+w[i]*x[i])


agrupar(z,w,x)
print(y)