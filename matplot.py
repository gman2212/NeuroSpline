import json
import matplotlib.pyplot as plt

def plot_spline(output_file):
    """Plots the generated spline points."""
    with open(output_file, 'r') as file:
        data = json.load(file)
    
    x_points = [p["Position"]["X"] for p in data["SplinePoints"]]
    y_points = [p["Position"]["Y"] for p in data["SplinePoints"]]

    plt.plot(x_points, y_points, marker='o', linestyle='-', label="Generated Path")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.title("Spline Path Visualization")
    plt.legend()
    plt.grid()
    plt.show()

# Run the plot
plot_spline(r""C:\Users\govin\OneDrive\Desktop\LLM2\output.json"")
