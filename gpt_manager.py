import openai
import os
from openai import OpenAI
from dotenv import load_dotenv
from database_manager import DatabaseManager

# Load environment variables from the .env file in the current directory
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class GPTManager:
    def __init__(self, api_key = os.getenv("OPENAI_API_KEY")):
        """
        Initializes the GPTManager with the specified API key.

        Args:
            api_key (str): The OpenAI API key.
        """
        openai.api_key = api_key

    
    def generate_welcome_text(self, student_data):
        """
        Generates a welcome text for the student.

        Args:
            student_data (list): The student's data including name, surname, study preferences, hobbies, subjects, boring subjects, and work preferences.

        Returns:
            str: The generated welcome text.
        """
        name, surname, study, dual, appr, hobbys, subjects, bores, work_pref = student_data[1:]

        prompt = (
            f"First, write for one student: 'Welcome {surname} {name}\n"
            f"Do not include any closing remarks or greetings such as: Best regards or Sincerely or Good Luck."
            f"Remain neutral and, if at all, talk about the student or the person addressed in the text."
            f"Write a funny welcome text for a student who is just about to read a consultation text."
            f"The consultation text refers to studies, dual studies or training. Please remain neutral, as the student does not yet know what they want to do."
            f"Also write something about the surname {surname}, such as what another person has achieved through learning or practical work."
            f"Also explain why learning, further education, and practical work are worthwhile."
            f"Write something about how a good decision in career and studies as well as passion can positively impact life."
            f"Finally, describe that the following sections are intended to help the student prepare better for the in-person consultation."
            f"The welcome text must end with exact this sentence: The following sections are intended to help you better prepare for your personal career counseling session."
        )              
                
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],        
            max_tokens=1000,  # Maximum number of tokens in the response
            temperature=1.0,  # Creativity of the response (between 0 and 1)
            #top_p=0.9,  # Probability threshold for token selection
            n=1,  # Number of generated responses
            #stop=None,  # Stop sequences to end the response
            #presence_penalty=0.5,  # Penalty for new topics
            #frequency_penalty=0.5  # Penalty for frequent repetitions
        )
        return response.choices[0].message.content.strip()

    
    def generate_study_text(self, student_data):
        """
        Generates a study consultation text for the student.

        Args:
            student_data (list): The student's data including name, surname, study preferences, hobbies, subjects, boring subjects, and work preferences.

        Returns:
            str: The generated study consultation text.
        """
        name, surname, study, dual, appr, hobbys, subjects, bores, work_pref = student_data[1:]

        if study == "high":
            prompt = (
                f"Create a detailed english consultation text for a student and address them directly, who is interested in pursuing higher education. "
                f"Do not include greetings or farewells, only the sections listed below as specified."
                f"Choose 3 different but suitable study programs in Germany that match the following student details: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Describe each of the 3 study programs in detail and in different ways. For each study program section, follow this structure: "
                f"1. Description: Please first provide a very detailed description of the study program including the main subjects and typical course contents. "
                f"2. An explanation of why the study program fits the student with logical reasoning, based on the student's details listed above. "
                f"3. Career opportunities: Detailed information about future career opportunities with this study program, including at least one example of a possible career. "
                f"4. Additional similar study programs: List numerically at the end of each section 5 more study programs in bullet points that match the student's details."
                f"Use clear and precise language."
                f"Create a section for each study program with numbering, example: 1. Study Program: Sport Management, then \n"
                f"After each section, a double line break should be inserted in the form of 8 dashes, example: --------. "
                f"Remain professional and objective, and use the 'you' form."
            )

        elif study == "medium":
            prompt = (
                f"Create a moderate english consultation text for a student and address them directly, who is interested in pursuing higher education. "
                f"Do not include greetings or farewells, only the sections listed below as specified."
                f"Choose 2 different but suitable study programs in Germany that match the following student details: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Describe each of the 2 study programs in detail and in different ways. For each study program section, follow this structure: "
                f"1. Description: Please first provide a very detailed description of the study program including the main subjects and typical course contents. "
                f"2. An explanation of why the study program fits the student with logical reasoning, based on the student's details listed above. "
                f"3. Career opportunities: Detailed information about future career opportunities with this study program, including at least one example of a possible career. "
                f"4. Additional similar study programs: List numerically at the end of each section 2 more study programs in bullet points that match the student's details."
                f"Use clear and precise language."
                f"Create a section for each study program with numbering, example: 1. Study Program: Sport Management, then \n"
                f"After each section, a double line break should be inserted in the form of 8 dashes, example: --------. "
                f"Remain professional and objective, and use the 'you' form."
            )

        else:
            prompt = (
                f"Create a short english consultation text for a student and address them directly, who is interested in pursuing higher education. "
                f"Choose 3 different but suitable study programs in Germany that match the following student details: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Do not use greetings, farewells, or congratulations."
                f"Create a section for each study program with numbering, including a line break."
                f"Example: 1. Study Program: Sport Management, including a line break."
                f"Describe why the study programs might suit the student."
                f"Remain professional and objective, and use the 'you' form."
            )

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,  # Maximum number of tokens in the response
            temperature=1,  # Creativity of the response (between 0 and 1)
            #top_p=0.9,  # Probability threshold for token selection
            n=1,  # Number of generated responses
            stop=None,  # Stop sequences to end the response
            #presence_penalty=2,  # Penalty for new topics
            #frequency_penalty=0.2  # Penalty for frequent repetitions
        )
        return response.choices[0].message.content.strip()

    
    def generate_dual_text(self, student_data):
        """
        Generates a dual study consultation text for the student.

        Args:
            student_data (list): The student's data including name, surname, dual study preferences, hobbies, subjects, boring subjects, and work preferences.

        Returns:
            str: The generated dual study consultation text.
        """
        name, surname, study, dual, appr, hobbys, subjects, bores, work_pref = student_data[1:]

        if dual == "high":
            prompt = (
                f"Create a detailed english consultation text for a student and address them directly, who is interested in a dual study program. "
                f"Do not include greetings or farewells, only the sections below as specified."
                f"Choose 3 different but suitable dual study programs in Germany that match the student's preferences: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite school subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Describe each of the 3 dual study programs in detail and in a different manner. For each dual study program section, follow this structure: "
                f"1. Description: First, provide a very detailed description of the dual study program with main subjects and typical course content. "
                f"2. An explanation of why the dual study program fits the student with a logical justification based on the above-mentioned preferences of the student. "
                f"3. Career opportunities: Detailed information about the future career opportunities with this dual study program, including at least one example of a possible career. "
                f"4. Further similar dual study programs: List numerically at the end of each section 5 additional dual study programs in bullet points that match the student's preferences. "
                f"Use clear and precise language. "
                f"Create a section for each dual study program with numbering, example: 1. Dual Study Program: Sport Management, then \n"
                f"After each section, a double line break should be added in the form of 8 dashes, example: --------. "
                f"Remain professional and objective and use the 'you' form."
            )

        elif dual == "medium":
            prompt = (
                f"Create a moderate english consultation text for a student and address them directly, who is interested in a dual study program. "
                f"Do not include greetings or farewells, only the sections below as specified."
                f"Choose 2 different but suitable dual study programs in Germany that match the student's preferences: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite school subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Describe each of the 2 dual study programs in detail and in a different manner. For each dual study program section, follow this structure: "
                f"1. Description: First, provide a very detailed description of the dual study program with main subjects and typical course content. "
                f"2. An explanation of why the dual study program fits the student with a logical justification based on the above-mentioned preferences of the student. "
                f"3. Career opportunities: Detailed information about the future career opportunities with this dual study program, including at least one example of a possible career. "
                f"4. Further similar dual study programs: List numerically at the end of each section 2 additional dual study programs in bullet points that match the student's preferences. "
                f"Use clear and precise language. "
                f"Create a section for each dual study program with numbering, example: 1. Dual Study Program: Sport Management, then \n"
                f"After each section, a double line break should be added in the form of 8 dashes, example: --------. "
                f"Remain professional and objective and use the 'you' form."
            )

        else:
            prompt = (
                f"Create a short english consultation text for a student and address them directly, who is interested in a dual study program. "
                f"Choose 3 different but suitable dual study programs in Germany that match the student's preferences: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite school subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Do not include greetings, farewells, or congratulations."
                f"Create a section for each dual study program with numbering, including a line break."
                f"Example: 1. Dual Study Program: Sport Management including line break."
                f"Describe why the dual study programs might fit the student."
                f"Remain professional and objective and use the 'you' form."
            )

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,  # Maximum number of tokens in the response
            temperature=1.0,  # Creativity of the response (between 0 and 1)
            # top_p=0.9,  # Probability threshold for token selection
            n=1,  # Number of generated responses
            # stop=None,  # Stop sequences that cause the model to end the output
            # presence_penalty=0.5,  # Penalty for new topics
            # frequency_penalty=0.5  # Penalty for frequent repetitions
        )
        return response.choices[0].message.content.strip()
    
    
    def generate_apprenticeship_text(self, student_data):
        """
        Generates an apprenticeship consultation text for the student.

        Args:
            student_data (list): The student's data including name, surname, apprenticeship preferences, hobbies, subjects, boring subjects, and work preferences.

        Returns:
            str: The generated apprenticeship consultation text.
        """
        name, surname, study, dual, appr, hobbys, subjects, bores, work_pref = student_data[1:]

        if appr == "high":
            prompt = (
                f"Create a detailed english consultation text for a student and address them directly, who is interested in an apprenticeship. "
                f"Do not include greetings or farewells, only the sections below as specified. "
                f"Choose 3 different but suitable german apprenticeships in Germany that match the student's preferences: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite school subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Describe each of the apprenticeships in detail and in a different manner. For each apprenticeship section, follow this structure: "
                f"1. Description: First, provide a very detailed description of the apprenticeship with main subjects and typical course content. "
                f"2. An explanation of why the apprenticeship fits the student with a logical justification based on the above-mentioned preferences of the student. "
                f"3. Career opportunities: Detailed information about the future career opportunities with this apprenticeship, including at least one example of a possible career. "
                f"4. Further similar apprenticeships: List numerically at the end of each section 5 additional apprenticeships in bullet points that match the student's preferences. "
                f"Use clear and precise language. "
                f"Create a section for each apprenticeship with numbering, example: 1. Apprenticeship: Sport Management, then \n"
                f"After each section, a double line break should be added in the form of 8 dashes, example: --------. "
                f"Remain professional and objective and use the 'you' form."
            )

        elif appr == "medium":
            prompt = (
                f"Create a moderate english consultation text for a student and address them directly, who is interested in an apprenticeship. "
                f"Do not include greetings or farewells, only the sections below as specified. "
                f"Choose 2 different but suitable german apprenticeships in Germany that match the student's preferences: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite school subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Describe each of the apprenticeships in detail and in a different manner. For each apprenticeship section, follow this structure: "
                f"1. Description: First, provide a very detailed description of the apprenticeship with main subjects and typical course content. "
                f"2. An explanation of why the apprenticeship fits the student with a logical justification based on the above-mentioned preferences of the student. "
                f"3. Career opportunities: Detailed information about the future career opportunities with this apprenticeship, including at least one example of a possible career. "
                f"4. Further similar apprenticeships: List numerically at the end of each section 2 additional apprenticeships in bullet points that match the student's preferences. "
                f"Use clear and precise language. "
                f"Create a section for each apprenticeship with numbering, example: 1. Apprenticeship: Sport Management, then \n"
                f"After each section, a double line break should be added in the form of 8 dashes, example: --------. "
                f"Remain professional and objective and use the 'you' form."
            )

        else:
            prompt = (
                f"Create a short english consultation text for a student and address them directly, who is interested in an apprenticeship. "
                f"Choose 3 different but suitable german apprenticeships in Germany that match the student's preferences: "
                f"1. Hobbies: {hobbys}. "
                f"2. Favorite school subjects: {subjects}. "
                f"3. Bored by: {bores}. "
                f"4. Prefers to work: {work_pref}. "
                f"Do not include greetings, farewells, or congratulations. "
                f"Create a section for each apprenticeship with numbering including a line break. "
                f"Example: 1. Apprenticeship: Sport Management including line break. "
                f"Describe why the apprenticeships might fit the student. "
                f"Remain professional and objective and use the 'you' form."
            )

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,  # Maximum number of tokens in the response
            temperature=1.0,  # Creativity of the response (between 0 and 1)
            # top_p=0.9,  # Probability threshold for token selection
            n=1,  # Number of generated responses
            # stop=None,  # Stop sequences that cause the model to end the output
            # presence_penalty=0.5,  # Penalty for new topics
            # frequency_penalty=0.5  # Penalty for frequent repetitions
        )
        return response.choices[0].message.content.strip()


    def generate_summary_text(self, student_data):
        """
        Generates a summary text for the student consultation.

        Args:
            student_data (list): The student's data including name, surname, study preferences, dual study preferences, apprenticeship preferences, hobbies, subjects, boring subjects, and work preferences.

        Returns:
            str: The generated summary consultation text.
        """
        name, surname, study, dual, appr, hobbys, subjects, bores, work_pref = student_data[1:]

        prompt = (
            f"Write a detailed summary text for the consultation without any salutation."
            f"Leave out salutations like Dear Student or any other personalized address completely. "
            f"The summary should be based on a personalized consultation text for a study, dual study, and an apprenticeship created by an AI assistant. "
            f"Do not mention specific study programs, dual study programs, apprenticeships, or fields of study. "
            f"Consider the following aspects: "
            f"1. Student's hobbies: {hobbys}. "
            f"2. Favorite school subjects: {subjects}. "
            f"3. Student is bored by: {bores}. "
            f"4. How the student prefers to work: {work_pref}. "
            f"Describe in detail that all these preferences were considered in the consultation text created by the AI assistant. "
            f"Also write that despite the consultation text, it is important to discuss this with a career advisor. "
            f"Speak from the perspective of the AI assistant, example: I, the AI assistant... "
            f"Follow the instructions and use the 'you' form. "
            f"Add a line break after the summary before you finally write: "
            f"Best regards and good luck on your further career path! Your AI assistant."
        )

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,  # Maximum number of tokens in the response
            temperature=1.0,  # Creativity of the response (between 0 and 1)
            # top_p=0.9,  # Probability threshold for token selection
            n=1,  # Number of generated responses
            # stop=None,  # Stop sequences that cause the model to end the output
            # presence_penalty=0.5,  # Penalty for new topics
            # frequency_penalty=0.5  # Penalty for frequent repetitions
        )
        return response.choices[0].message.content.strip()


def main():
    """
    Main function to test the functionality of the GPTManager and DatabaseManager.

    This function retrieves student data from the database, generates various types of consultation texts
    (welcome, study, dual study, apprenticeship, and summary), and prints the results.
    """
    db_manager = DatabaseManager()
    student_id = 1
    student_data = db_manager.get_student_data(student_id)
    print(student_data)
    gpt_manager = GPTManager()
    welcome_text = gpt_manager.generate_welcome_text(student_data)
    print(welcome_text)
    study_text = gpt_manager.generate_study_text(student_data)
    print(study_text)
    dual_text = gpt_manager.generate_dual_text(student_data)
    print(dual_text)
    appr_text = gpt_manager.generate_apprenticeship_text(student_data)
    print(appr_text)
    summary_text = gpt_manager.generate_summary_text(student_data)
    print(summary_text)

if __name__ == "__main__":
    main()


    