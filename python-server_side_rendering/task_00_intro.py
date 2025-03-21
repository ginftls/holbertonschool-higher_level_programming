import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template with placeholders and a list of objects.
    
    Parameters:
        template (str): The template string containing placeholders.
        attendees (list): A list of dictionaries containing attendee data.
    
    Returns:
        None
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee and Generate Output Files
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing
        try:
            filled_template = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A")
            )
        except KeyError as e:
            print(f"Error: Missing key {e} in attendee data at index {index}. Skipping this entry.")
            continue

        # Define output file name
        output_file_name = f"output_{index}.txt"

        # Write the processed template to the output file
        try:
            with open(output_file_name, 'w') as output_file:
                output_file.write(filled_template)
            print(f"Generated file: {output_file_name}")
        except IOError as e:
            print(f"Error writing to file {output_file_name}: {e}")

# Example Main File to Test the Program
if __name__ == "__main__":
    # Read the template from a file
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: Template file 'template.txt' not found.")
        exit(1)

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
