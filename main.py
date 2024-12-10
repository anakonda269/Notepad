from rich import print
import pickle
import os
import random
import string

# Dictionary to store notes
Notepad = {
    'ID': [],
    'Title': [],
    'Content': []
}

# File to store notes
NOTE_FILE = "notepad.pkl"


def initialize_notepad():
    """Initializes the notepad file if it doesn't already exist."""
    if not os.path.exists(NOTE_FILE):
        # Create a new file if it doesn't exist
        with open(NOTE_FILE, 'wb') as file:
            pickle.dump(Notepad, file)
        print("[green]The notepad file has been created![/green]")
    else:
        load_notepad()


def load_notepad():
    """Loads notes from the file."""
    try:
        with open(NOTE_FILE, 'rb') as file:
            global Notepad
            Notepad = pickle.load(file)
    except (EOFError, pickle.UnpicklingError):
        # Handle corrupted or empty files
        print("[red]Error while loading notes. The file may be corrupted.[/red]")
        Notepad = {
            'ID': [],
            'Title': [],
            'Content': []
        }


def save_notepad():
    """Saves notes to the file."""
    try:
        with open(NOTE_FILE, 'wb') as file:
            pickle.dump(Notepad, file)
        print("[green]Notes saved successfully![/green]")
    except Exception as e:
        # Handle any errors during the save process
        print(f"[red]Error while saving notes: {e}[/red]")


def Notatnik():
    """Main menu for the notepad."""
    while True:
        if len(Notepad['ID']) == 0:
            # Notify user if the notepad is empty
            print("[yellow]The notepad is empty![/yellow]")
            print("[cyan]Add a new note to get started.[/cyan]")
            NewNote()
        else:
            # Display all notes
            print("[blue]Your notes:[/blue]")
            for i in range(len(Notepad['ID'])):
                print(f"{Notepad['ID'][i]}. {Notepad['Title'][i]}")
            
            # Display menu options
            print("[cyan]1. Create a new note[/cyan]")
            print("[cyan]2. Edit an existing note[/cyan]")
            print("[cyan]3. Exit[/cyan]")

            try:
                # Get user choice
                opcja = int(input("Choose an option: "))
                if opcja == 1:
                    NewNote()
                elif opcja == 2:
                    EditNote()
                elif opcja == 3:
                    print("[green]Goodbye![/green]")
                    break
                else:
                    print("[red]Invalid option. Please try again.[/red]")
            except ValueError:
                # Handle invalid input
                print("[red]Invalid choice. Please enter a number.[/red]")


def NewNote():
    """Adds a new note."""
    # Calculate the next available ID
    Next_ID = len(Notepad["ID"]) + 1
    Notepad['ID'].append(Next_ID)
    
    # Get title and content from the user
    Note_Title = input("Enter the title of the note: ")
    Notepad['Title'].append(Note_Title)
    Note_Content = input("Enter the content of the note: ")
    Notepad['Content'].append(Note_Content)
    
    # Save changes to the file
    save_notepad()


def EditNote():
    """Edits an existing note."""
    if len(Notepad['ID']) == 0:
        # Notify user if there are no notes to edit
        print("[red]No notes available for editing.[/red]")
        return

    # Display available notes
    print("[blue]Available notes:[/blue]")
    for i, title in enumerate(Notepad['Title']):
        print(f"{i+1}. {title}")

    try:
        # Ask user to select a note to edit
        choice = int(input("Choose the number of the note to edit: "))
        index = choice - 1
        if 0 <= index < len(Notepad['Title']):
            # Display the current content of the selected note
            print(f"[yellow]Current content:[/yellow] {Notepad['Content'][index]}")

            # Generate a random 5-character end phrase
            end_phrase = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            print(f"[cyan]Edit the content (type '{end_phrase}' to finish):[/cyan]")

            new_content = ''
            while True:
                # Allow multiline input until the user types the end phrase
                line = input()
                if line.strip() == end_phrase:
                    break
                new_content += line + '\n'

            # Update the note's content
            Notepad['Content'][index] = new_content.strip()
            print("[green]The note has been updated![/green]")
            # Save changes to the file
            save_notepad()
        else:
            # Handle invalid note number
            print("[red]Invalid note number.[/red]")
    except ValueError:
        # Handle non-numeric input
        print("[red]Invalid choice. Please enter a number.[/red]")


def main():
    """Main function of the program."""
    print("[green]Welcome to the Notepad![/green]")
    # Initialize the notepad file
    initialize_notepad()
    # Start the main menu
    Notatnik()


# Run the program
if __name__ == "__main__":
    main()
