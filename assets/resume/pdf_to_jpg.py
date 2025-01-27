import fitz  # PyMuPDF
import os

def convert_pdf_to_jpg():
    try:
        # Get the current directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the input PDF file path (must be in the same directory as the script)
        input_pdf = os.path.join(script_dir, "SaieashwarMukund.pdf")
        
        # Check if the PDF file exists
        if not os.path.exists(input_pdf):
            print(f"Input PDF file not found: {input_pdf}")
            return
        
        # Define the output JPG file path
        output_jpg = os.path.splitext(input_pdf)[0] + ".jpg"
        
        # Open the PDF file
        pdf_document = fitz.open(input_pdf)
        
        # Ensure the PDF has at least one page
        if pdf_document.page_count < 1:
            print("The PDF file has no pages.")
            return
        
        # Render the first page of the PDF to an image
        page = pdf_document[0]
        pixmap = page.get_pixmap(dpi=300)  # Increase DPI for better quality
        
        # Save the image as a JPG (overwrite if it already exists)
        pixmap.save(output_jpg)
        print(f"Successfully converted '{input_pdf}' to '{output_jpg}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the PDF document
        pdf_document.close()


if __name__ == "__main__":
    convert_pdf_to_jpg()
