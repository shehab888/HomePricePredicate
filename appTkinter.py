import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the pre-trained model
with open('C:/Users/sheha/PycharmProjects/SimplePythonProject/home_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the main window
root = tk.Tk()
root.title("House Price Prediction")
root.geometry("400x300")  # Set window size
root.config(bg="#f0f0f0")

# Add a frame for the main content
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

# Header Label
header_label = tk.Label(frame, text="House Price Prediction", font=("Arial", 16, "bold"), bg="#f0f0f0")
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Function to predict price
def predict_price():
    try:
        # Get the user input
        area = float(entry_area.get())
        rooms = int(entry_rooms.get())
        age = int(entry_age.get())

        # Prepare the input data for prediction
        input_data = np.array([[area, rooms, age]])

        # Predict the price
        predicted_price = model.predict(input_data)[0]

        # Display the result
        result_label.config(text=f"Predicted Price: ${predicted_price:,.2f}")
    except ValueError:
        # Show error if input is invalid
        messagebox.showerror("Invalid input", "Please enter valid values for area, rooms, and age.")

# Area Input
label_area = tk.Label(frame, text="Enter area (sq ft):", font=("Arial", 10), bg="#f0f0f0")
label_area.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_area = tk.Entry(frame, font=("Arial", 10), width=20)
entry_area.grid(row=1, column=1, pady=5)

# Rooms Input
label_rooms = tk.Label(frame, text="Enter number of rooms:", font=("Arial", 10), bg="#f0f0f0")
label_rooms.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_rooms = tk.Entry(frame, font=("Arial", 10), width=20)
entry_rooms.grid(row=2, column=1, pady=5)

# Age Input
label_age = tk.Label(frame, text="Enter house age (years):", font=("Arial", 10), bg="#f0f0f0")
label_age.grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_age = tk.Entry(frame, font=("Arial", 10), width=20)
entry_age.grid(row=3, column=1, pady=5)

# Predict Button
predict_button = tk.Button(frame, text="Predict Price", font=("Arial", 12), bg="#4CAF50", fg="white", command=predict_price)
predict_button.grid(row=4, column=0, columnspan=2, pady=20)

# Result Label
result_label = tk.Label(frame, text="Predicted Price: $0.00", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
