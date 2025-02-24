import json
import time
import requests
import re

def read_json(file_path):
    """Reads a JSON file and returns the parsed data."""
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json_structure(response_json):
    """Checks if the response contains a valid JSON structure."""
    required_keys = ["SplineId", "SplinePoints"]
    return all(key in response_json for key in required_keys)

def check_consistency(response_json, obstacles):
    """Checks if the model consistently avoids obstacles."""
    for point in response_json.get("SplinePoints", []):
        pos = point.get("Position", {})
        for obs in obstacles:
            if not all(k in obs for k in ["X", "Y"]):
                continue  # Skip invalid obstacles
            if (obs["X"] - 5 <= pos.get("X", 0) <= obs["X"] + 5) and \
               (obs["Y"] - 5 <= pos.get("Y", 0) <= obs["Y"] + 5):
                return False  # Collision detected
    return True

def check_accuracy(response_json, input_constraints):
    """Checks if the model follows input constraints."""
    for point in response_json.get("SplinePoints", []):
        pos = point.get("Position", {})
        if not all(k in input_constraints for k in ["min_x", "max_x", "min_y", "max_y"]):
            continue  # Skip invalid constraints
        if not (input_constraints["min_x"] <= pos.get("X", 0) <= input_constraints["max_x"] and
                input_constraints["min_y"] <= pos.get("Y", 0) <= input_constraints["max_y"]):
            return False
    return True

def check_z_axis_handling(response_json):
    """Checks if the model properly handles the Z-axis."""
    for point in response_json.get("SplinePoints", []):
        z_value = point.get("Position", {}).get("Z", None)
        if z_value is None or not isinstance(z_value, (int, float)):
            return "Ignored"
        if z_value != 0:
            return "Used Correctly"
    return "Confused"

def evaluate_output_json(output_file, input_file):
    """Evaluates the output JSON file based on various metrics."""
    response_json = read_json(output_file)
    input_data = read_json(input_file)
    
    metrics = {
        "Consistency": check_consistency(response_json, input_data.get("Obstacles", [])),
        "Accuracy": check_accuracy(response_json, input_data.get("Constraints", {})),
        "Output Structure": validate_json_structure(response_json),
        "Z-axis Handling": check_z_axis_handling(response_json)
    }
    return metrics

def main():
    output_file = r"C:\Users\govin\OneDrive\Desktop\LLM2\output.json" # Replace with actual output file path
    input_file = r"C:\Users\govin\OneDrive\Desktop\LLM2\Inputfile.json"  # Replace with actual input file path
    
    results = evaluate_output_json(output_file, input_file)
    
    with open("evaluation_results.json", "w") as file:
        json.dump(results, file, indent=4)
    
    print("Evaluation results saved to evaluation_results.json")

if __name__ == "__main__":
    main()
