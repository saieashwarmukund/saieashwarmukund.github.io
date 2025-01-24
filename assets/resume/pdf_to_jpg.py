import fitz  # PyMuPDF
import os

def convert_pdf_to_jpg(input_pdf):
    try:
        # Check if the input file exists
        if not os.path.exists(input_pdf):
            print(f"Input PDF file not found: {input_pdf}")
            return

        # Determine the output JPG file path
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

        # Save the image as a JPG, replacing the file if it exists
        pixmap.save(output_jpg)
        print(f"PDF converted to JPG successfully: {output_jpg}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the PDF document
        pdf_document.close()


# Example Usage
if __name__ == "__main__":
    # Path to your PDF file
    input_pdf_path = r"SaieashwarMukund.pdf"

    # Convert the PDF to JPG
    convert_pdf_to_jpg(input_pdf_path)
