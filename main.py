from database_manager import DatabaseManager
from gpt_manager import GPTManager
from pdf_manager import PDFManager
import os
from dotenv import load_dotenv


def main():
    ####### DB Area #######
    db_manager = DatabaseManager()  # db_name='db_information.db' is already specified in the class
    student_id =2  # Define the student ID to retrieve
    student_data = db_manager.get_student_data(student_id)  # Retrieve student data

    if student_data:  # Check if data was retrieved and print it
        print("Student data:")
        print(student_data)

        ####### GPT Area #######
        gpt_manager = GPTManager()  # Create an instance of GPTManager
        welcome_text = gpt_manager.generate_welcome_text(student_data)  # Generate welcome text based on student data
        study_text = gpt_manager.generate_study_text(student_data)
        dual_text = gpt_manager.generate_dual_text(student_data)
        appr_text = gpt_manager.generate_apprenticeship_text(student_data)
        summary_text = gpt_manager.generate_summary_text(student_data)

    else:
        print(f"No student found with ID {student_id}")

    db_manager.close()  # Close the database connection


    ####### PDF Area #######
    filename = f"Student_ID_{student_id}_{student_data[2]}_{student_data[1]}.pdf"
    pdf_manager = PDFManager(filename)                             
    pdf_manager.add_title("Personalized Career Counseling Report")
    pdf_manager.add_paragraph(welcome_text)
    pdf_manager.add_subtitle("Your prospects for a degree program:")
    pdf_manager.add_paragraph(study_text)
    pdf_manager.add_subtitle("Your prospects for a dual study program:")
    pdf_manager.add_paragraph(dual_text)
    pdf_manager.add_subtitle("Your prospects for an apprenticeship:")
    pdf_manager.add_paragraph(appr_text)
    pdf_manager.add_subtitle("Summary:")
    pdf_manager.add_paragraph(summary_text)
    pdf_manager.save()
    print(f"PDF successfully saved as {pdf_manager.filename}")


if __name__ == '__main__':
    main()
