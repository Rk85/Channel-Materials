supported_languages = [ "python", "java", "c", "js"]
max_lang_per_user = 3
user_selected_languages = []
user_option = 0

main_option = """
Welcome to RK Learning center, please select one of the following option
========================================================================
     1. To view the main option
     2. To view the list of supported programming languages
     3. To view the programming language in your list
     4. To Add the new programming language into your list
     5. To remove the already added programming language into your list
     9. To exit the application
**condition apply: maximum %s languages per person
"""

print(main_option %(max_lang_per_user) )

while user_option != 9:
    user_option = int( input("Please provide any one of the option above: ") )
    if user_option > 9:
        print("user provided option greater than 5, so continuing to user input")
        continue
    if user_option == 1:
        print(main_option %(max_lang_per_user) )
    elif user_option == 2:
        print("List of supported languages are ")
        for supported_language in supported_languages:
            print(supported_language)
    elif user_option == 3:
        print("Following languages are present in your list")
        for user_selected_language in user_selected_languages:
            print(user_selected_language)
        else:
            print("**********************")
    elif user_option == 4:
        if ( len(user_selected_languages) == max_lang_per_user ):
            error = ("You have reached your maximum supported languages",
                    "please remove one of them from your list to add new one")
            print(error)
        else:
            supp_lang_text = "Please select any of the supported language"
            selected_language = input(supp_lang_text)
            user_selected_languages.append(selected_language)
    else:
        if user_option != 9:
            print("Wrong option selected, Exiting the application")
            break
else:
    print("Exiting the application after user typed option 9")

