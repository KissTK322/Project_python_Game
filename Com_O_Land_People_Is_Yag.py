import curses
import time

menu_options = ['Start Game', 'Load Game', 'Save Game', 'Quit']

Dialog_kla = ["บังกล้าชะล่าใจ : ยินดีต้อนรับเข้าสู่เมืองแห่งคอมโอที่มีแต่พวก yag!" , "บังกล้าชะล่าใจ : เอ้ย! ไม่ใช่ที่นี่มีแต่สุภาพชนที่พร้อมจะพูดคำว่า \"คุณ\" กับ \"Kub\" " , "บังกล้าชะล่าใจ : ว่าแต่คุณชื่ออะไรหรอ kub ...\n"]
len_kla = len(Dialog_kla) 
kla = 0

# Define the default game data
game_data = {'score': 0 , 'length': 1, 'snake': [(10, 10)], 'direction': curses.KEY_RIGHT}

# Define the function to draw the menu
def draw_menu(stdscr, current_option):
    stdscr.clear()
    stdscr.addstr(0, 0, "Com O Land People Is Yag")
    for i, option in enumerate(menu_options):
        if i == current_option:
            stdscr.addstr(i + 2, 0, f"> {option}")
        else:
            stdscr.addstr(i + 2, 0, f"  {option}")
    stdscr.refresh()


# Define the function to handle user input in the menu
def handle_menu_input(stdscr, game_data):
    current_option = 0
    draw_menu(stdscr, current_option)
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(menu_options) - 1:
            current_option += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_option, game_data
        draw_menu(stdscr, current_option)


# Define the function to save game data to a file
def save_game_data(game_data):
    with open('game_data.txt', 'w') as file:
        for key, value in game_data.items():
            file.write(f"{key}: {value}\n")

# Define the function to load game data from a file
import ast

def load_game_data():
    game_data = {}
    try:
        with open('game_data.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                if key == 'snake':
                    game_data[key] = ast.literal_eval(value)
                else:
                    game_data[key] = int(value)
    except FileNotFoundError:
        pass
    return game_data

def get_name(stdscr):
    stdscr.addstr(len_kla + 1, 0, "Enter your name: ")
    curses.echo()
    name = stdscr.getstr().decode('utf-8')
    curses.noecho()
    return name

def kla_dialog(stdscr, kla):
    stdscr.addstr(len_kla + 2, 0, "Press Enter to continue...")
    while kla != len_kla:
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            kla += 1
        elif kla == 2 :
            while True :
                key = stdscr.getch()
                name = get_name(stdscr)
                if key == curses.KEY_ENTER or key in [10, 13]:
                    break
            stdscr.addstr(kla, 0, Dialog_kla[kla] + name)
        else:
            stdscr.addstr(kla, 0, Dialog_kla[kla])
            time.sleep(0.35)

def main(stdscr):
    game_data = load_game_data()
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    kla = 0
    kla_dialog(stdscr , kla)
    while True:
        # Draw the main menu and get user input
        menu_option, game_data = handle_menu_input(stdscr, game_data)

        if menu_option == 0:  # Start Game
            # Draw the new menu and get user input
            new_menu_options = ['Option 1', 'Option 2', 'Back']
            current_option = 0
            while True:
                stdscr.clear()
                stdscr.addstr(0, 0, "New Menu")
                for i, option in enumerate(new_menu_options):
                    if i == current_option:
                        stdscr.addstr(i + 2, 0, f"> {option}")
                    else:
                        stdscr.addstr(i + 2, 0, f"  {option}")
                stdscr.refresh()

                key = stdscr.getch()
                if key == curses.KEY_UP and current_option > 0:
                    current_option -= 1
                elif key == curses.KEY_DOWN and current_option < len(new_menu_options) - 1:
                    current_option += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    if current_option == 0:  # Option 1
                        # TODO: Implement option 1 logic
                        pass
                    elif current_option == 1:  # Option 2
                        # TODO: Implement option 2 logic
                        pass
                    elif current_option == 2:  # Back
                        break  # Return to main menu

        elif menu_option == 1:  # Load Game
            # TODO: Implement Load Game logic
            pass

        elif menu_option == 2:  # Save Game
            save_game_data(game_data)

        elif menu_option == 3:  # Quit
            return  # Exit game


if __name__ == '__main__':
    # Initialize curses
    curses.wrapper(main)
