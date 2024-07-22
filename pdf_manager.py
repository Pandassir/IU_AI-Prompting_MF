from fpdf import FPDF

class PDFManager:
    def __init__(self, filename='output.pdf'):
        """
        Initializes the PDFManager with a specified output filename.

        Args:
            filename (str): The name of the output PDF file.
        """
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_font("Arial", size=12)

    def add_title(self, title):
        """
        Adds a title to the PDF document.

        Args:
            title (str): The title text to add.
        """
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, txt=title, ln=True, align='C')
        self.pdf.ln(20)

    def add_subtitle(self, text):
        """
        Adds a subtitle to the PDF document.

        Args:
            text (str): The subtitle text to add.
        """
        self.pdf.set_font("Arial", 'B', size=14)
        self.pdf.multi_cell(0,5, txt=text)
        self.pdf.ln(7)

    def add_paragraph(self, text):
        """
        Adds a paragraph to the PDF document.

        Args:
            text (str): The paragraph text to add.
        """
        self.pdf.set_font("Arial", size=10)
        self.pdf.multi_cell(0,5, txt=text)
        self.pdf.ln(15)

    def save(self):
        """
        Saves the PDF document to the specified filename.
        """
        self.pdf.output(self.filename)

def main():
    """
    Test function to demonstrate PDF creation.
    """
    pdf_manager = PDFManager('example_output.pdf')
    pdf_manager.add_title("Career Counseling Report")
    pdf_manager.add_subtitle("Your First Interest:")
    pdf_manager.add_paragraph("Text 1.")
    pdf_manager.add_paragraph("Text 2.")
    pdf_manager.save()
    print(f"PDF successfully saved as {pdf_manager.filename}")

if __name__ == "__main__":
    main()
