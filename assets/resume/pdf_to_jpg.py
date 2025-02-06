import fitz  
import os

def convert_pdf_to_jpg():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_pdf = os.path.join(script_dir, "SaieashwarMukund.pdf")

        if not os.path.exists(input_pdf):
            print(f"File not found: {input_pdf}")
            return

        output_jpg = os.path.splitext(input_pdf)[0] + ".jpg"
        pdf_document = fitz.open(input_pdf)

        if pdf_document.page_count < 1:
            print("PDF has no pages.")
            return

        pixmap = pdf_document[0].get_pixmap(dpi=300)
        pixmap.save(output_jpg)
        print(f"Converted '{input_pdf}' to '{output_jpg}'")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        pdf_document.close()

if __name__ == "__main__":
    convert_pdf_to_jpg()
