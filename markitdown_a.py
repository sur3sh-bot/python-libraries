from markitdown import MarkItDown

def convert_to_ai_friendly_format(file_path):
    """
    Converts a document to Markdown format for better AI readability.
    """
    # Initialize the converter
    md_converter = MarkItDown()
    
    try:
        # Perform the conversion using the file path provided
        result = md_converter.convert(file_path)
        
        # Access the markdown text
        markdown_output = result.text_content
        
        print(f"--- Conversion Successful for: {file_path} ---")
        print("Preview (First 500 characters):")
        print("-" * 30)
        print(markdown_output[:500])
        print("-" * 30)
        
        # Save the result to a file called 'output.md'
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(markdown_output)
        print("Success! Full content saved to 'output.md'")
            
    except Exception as e:
        print(f"Error converting file: {e}")

# --- EXECUTION ---
# This line triggers the function with your specific PowerPoint file
convert_to_ai_friendly_format("data-for-markitdown.pptx")