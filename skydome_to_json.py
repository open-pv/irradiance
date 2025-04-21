import os
import csv
import json
import re

def process_csv_files(directory):
    """Process all CSV files in the directory, matching skymap data with metadata files."""
    
    # Get all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Extract unique location_id and period combinations
    pattern = r'(\d+)_(\d{4}(?:_\d{2}|_yearly))(?:_metadata|_skymap)?'
    unique_pairs = set()
    for file in csv_files:
        match = re.search(pattern, file)
        if match:
            location_id, period = match.groups()
            unique_pairs.add((location_id, period))
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(directory, "json_output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each pair of files
    for location_id, period in unique_pairs:
        data_file = f"{location_id}_{period}_skymap.csv"
        metadata_file = f"{location_id}_{period}_metadata.csv"
        
        # Skip if either file doesn't exist
        if not (os.path.exists(os.path.join(directory, data_file)) and 
                os.path.exists(os.path.join(directory, metadata_file))):
            print(f"Skipping {location_id}_{period} - files not found")
            continue
        
        try:
            # Load metadata
            metadata = {}
            with open(os.path.join(directory, metadata_file), newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # Get the first row (there should be only one)
                for row in reader:
                    for key, value in row.items():
                        # Convert numeric values
                        try:
                            if '.' in value:
                                metadata[key] = float(value)
                            else:
                                metadata[key] = int(value)
                        except (ValueError, TypeError):
                            metadata[key] = value
                    break  # Only process the first row
            
            # Load skymap data
            data = []
            with open(os.path.join(directory, data_file), newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Only include entries with elevation >= 0
                    elevation = float(row.get("elevation_deg", 0))
                    if elevation > 0:
                        data.append({
                            "altitude": elevation,
                            "azimuth": float(row["azimuth_nav_deg"]),
                            "radiance": float(row["average_radiance_W_m2_sr"])
                        })
            
            # Create output
            output = {
                "data": data,
                "metadata": metadata
            }
            
            # Save to JSON
            output_file = f"{location_id}_{period}.json"
            with open(os.path.join(output_dir, output_file), "w") as jsonfile:
                json.dump(output, jsonfile, indent=4)
            
            print(f"Processed {location_id}_{period}")
            
        except Exception as e:
            print(f"Error processing {location_id}_{period}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Use the current directory or specify your data directory
    data_directory = "../aggregated_results_claude_poa_comparison_processed/"
    process_csv_files(data_directory)