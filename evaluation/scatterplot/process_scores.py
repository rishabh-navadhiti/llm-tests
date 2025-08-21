import json
import os
import ast # For safely evaluating string literals
import numpy as np # Still useful for handling numpy types during conversion

def extract_scores_from_json_like(file_path):
    """
    Reads a JSON-like file with single quotes, converts it to valid JSON,
    and then extracts specific scores for predefined keys.
    Returns a new list of dictionaries with extracted scores.
    """
    with open(file_path, 'r') as f:
        # Read the file content as a single string
        content = f.read()

    # Safely evaluate the string to a Python list of dictionaries
    # This handles single quotes and numpy types in the initial string representation
    python_object = ast.literal_eval(content)

    extracted_scores_data = []
    
    # Define the keys for which we want to extract scores
    target_keys = [
        "PATIENT_NAME",
        "CHIEF_COMPLAINT",
        "HPI_SPENCER",
        "MUSCULOSKELETAL_VERBATIM",
        "IMAGING_RESULTS",
        "ASSESSMENT_SPENCER",
        "PLAN_SPENCER_"
    ]

    for item in python_object: # Iterate through the Python object
        if item.get('key') in target_keys:
            key_name = item['key']
            scores = {}
            # Extract and convert scores to standard Python types (float)
            if 'bleu_score' in item:
                scores['bleu_score'] = float(item['bleu_score'])
            if 'content_similarity' in item:
                scores['content_similarity'] = float(item['content_similarity'])
            if 'rhetorical_similarity' in item:
                scores['rhetorical_similarity'] = float(item['rhetorical_similarity'])
            if 'topic_similarity' in item:
                scores['topic_similarity'] = float(item['topic_similarity'])
            if 'content_analysis' in item:
                scores['content_analysis'] = float(item['content_analysis'])

            extracted_scores_data.append({key_name: scores})
            
    return extracted_scores_data

def process_directory_for_scores(input_dir, output_dir):
    """
    Processes all JSON-like files in the input directory, extracts scores,
    and saves the results to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"): # Assuming your files still have .json extension
            file_path = os.path.join(input_dir, filename)
            print(f"Processing {filename}...")
            
            try:
                extracted_scores_json = extract_scores_from_json_like(file_path)
                output_file_path = os.path.join(output_dir, f"scores_{filename}")
                with open(output_file_path, 'w') as outfile:
                    json.dump(extracted_scores_json, outfile, indent=2)
                print(f"Successfully extracted scores and saved to {output_file_path} 👍")
            except Exception as e:
                print(f"Error processing {filename}: {e} ❌")

if __name__ == "__main__":
    # --- Configuration ---
    # Place your single-quoted JSON-like files in this directory
    input_directory = "input_jsons"
    # This directory will store the new JSON files with only the extracted scores
    output_directory = "output_extracted_scores" 

    # --- Create dummy input files for demonstration if they don't exist ---
    if not os.path.exists(input_directory):
        os.makedirs(input_directory)
        print(f"Created dummy input directory: {input_directory}")
        
        # Example JSON-like content with single quotes
        # Note: numpy types are part of the literal string representation here
        example_json_like_content = """
        [{'title': 'Patient Name', 'content': [], 'key': 'PATIENT_NAME', 'bleu_score': 0.0, 'content_similarity': np.float32(0.1983), 'rhetorical_similarity': 0.0, 'topic_similarity': np.float64(0.601), 'content_analysis': 0.0}, {'title': 'Chief Complaint', 'content': ['numbness and tingling of her right hand'], 'key': 'CHIEF_COMPLAINT', 'bleu_score': 0.0, 'content_similarity': np.float32(0.8668), 'rhetorical_similarity': np.float32(0.8476), 'topic_similarity': np.float64(1.0), 'content_analysis': 0.6667}, {'title': 'HPI Spencer', 'content': ['The patient reports increasing numbness and tingling in her right hand following completion of chemotherapy for lymphoma. She has been at home more and notes difficulty feeling things and performing activities such as putting on earrings. She also mentions burning her right thumb, which has made it more challenging to feel objects. She has been trying to hold her phone less.'], 'key': 'HPI_SPENCER', 'bleu_score': 0.266, 'content_similarity': np.float32(0.8566), 'rhetorical_similarity': np.float32(0.6179), 'topic_similarity': np.float64(0.0148), 'content_analysis': 0.45}, {'title': 'Musculoskeletal', 'content': ['Bilateral upper extremity skin is clean, dry, and intact without erythema or ecchymosis. Moderate tenderness of the right small finger. A nodule and triggering are present. Excellent range of motion overall. PCGs are normal.'], 'key': 'MUSCULOSKELETAL_VERBATIM', 'bleu_score': 0.3651, 'content_similarity': np.float32(0.8631), 'rhetorical_similarity': np.float32(0.7102), 'topic_similarity': np.float64(1.0), 'content_analysis': 0.5714}, {'title': 'Imaging Results', 'content': ['X-ray normal'], 'key': 'IMAGING_RESULTS', 'bleu_score': 0, 'content_similarity': np.float32(0.2402), 'rhetorical_similarity': np.float32(0.1598), 'topic_similarity': np.float64(0.3759), 'content_analysis': 0.0}, {'title': 'Assessment', 'content': ['Right small finger trigger', 'Carpal tunnel syndrome', 'History of lymphoma'], 'key': 'ASSESSMENT_SPENCER', 'bleu_score': 0.0, 'content_similarity': np.float32(0.3833), 'rhetorical_similarity': np.float32(0.4175), 'topic_similarity': np.float64(0.1907), 'content_analysis': 0.2857}, {'title': 'Plan', 'content': ['Another injection in the right small finger', 'Night splints for carpal tunnel', 'Low threshold for nerve studies', 'Return to clinic in two months for follow-up.'], 'key': 'PLAN_SPENCER_', 'bleu_score': 0.327, 'content_similarity': np.float32(0.8179), 'rhetorical_similarity': np.float32(0.7298), 'topic_similarity': np.float64(0.0197), 'content_analysis': 0.5455}]
        """

        # Create 3 dummy files for demonstration
        for i in range(1, 4):
            dummy_file_path = os.path.join(input_directory, f"data_file_{i}.json")
            with open(dummy_file_path, 'w') as f:
                f.write(example_json_like_content) # Write as a string
            print(f"Created dummy file: {dummy_file_path}")

    # --- Run the processing ---
    print("\nStarting JSON-like file processing... 🚀")
    process_directory_for_scores(input_directory, output_directory)
    print("\nProcessing complete! 🎉")
    print(f"Check the '{output_directory}' folder for your extracted scores. 📁")