from markitdown import MarkItDown

def convert_to_ai_friendly_format(file_path):
    """
    Converts a document to Markdown format for better AI readability.
    """
    md_converter = MarkItDown()
    
    try:
        # Perform the conversion
        result = md_converter.convert(file_path)
        markdown_output = result.text_content
        
        print(f"--- Conversion Successful for: {file_path} ---")
        print("Preview (First 500 characters):")
        print("-" * 30)
        print(markdown_output[:500])
        print("-" * 30)
        
        # Save the result - Changed to output.md to match your print statement
        output_filename = "beep.txt"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(markdown_output)
            
        print(f"Success! Full content saved to '{output_filename}'")
            
    except Exception as e:
        print(f"Error converting file: {e}")

# Trigger the function
convert_to_ai_friendly_format("data-for-markitdown.pptx")