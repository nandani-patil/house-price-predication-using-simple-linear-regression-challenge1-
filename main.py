from train_model import train_model

model = train_model()

area = int(input("Enter house area: "))

price = model.predict([[area]])

print("Predicted Price:", price[0])