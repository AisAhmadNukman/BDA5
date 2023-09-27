# Import the add_and_subtract function from math_operations.py
from ml.predict import predict

# Get input from the user
hari = (input("Input hari: "))
jam = (input("Input jam : "))
area = (input("Input area: "))

# Call the add_and_subtract function
results = predict(hari, jam, area)

# Display the results
print(f"Prediksi jumlah kendaraan pada hari {hari} jam {jam} di area {area}: {results}")