import pygame
import pygame_menu
import csv
from os import path
from play_hindustani_notes import play_notes
# from backend import read_raag_data

pygame.init()  # start listening to you drawing commands.
COLORS = pygame.color.THECOLORS
screen_size = width, height = 1024, 768
screen = pygame.display.set_mode(screen_size)

font = pygame.font.SysFont('Arial', 28)
large_font = pygame.font.SysFont('Arial', 60)
pygame.display.set_caption("Raag Dhwani")
selected_raag = ['Adana', 'aroha']
x = 0.5

def read_raag_data():
	# Read the CSV file in python using this code:
	filename = 'raga_data.csv'
	#create handle to open file in memory
	file_path = path.abspath(__file__) # full path of your script
	dir_path = path.dirname(file_path) # full path of the directory of your script
	filename_path = path.join(dir_path, filename) # absolute zip file path
	csvfile = open(filename_path, 'r')
	# create a reader that reads file as a dictionary
	dict_handle = csv.DictReader(csvfile)
	raag = dict()
	x = 6.0
	# look through the values in the reader and print:
	for d in dict_handle:
		raag[d['name']] = d
	return raag


def start_ui(raag):
	def set_raag(value, raag_value, **kwargs):
	  	# set value of selected_raag[0] here
		selected_raag[0] = raag_value
		print(value, raag_value)
		pass

	def set_raag_property(value, raag_value, **kwargs):
	  	# set value of selected_raag[1] here
		selected_raag[1] = value[0][0]
		print(value, raag_value)
		pass

	def playsound():
		# play_notes("n-S_m_m_m_P_g_m_n_D_N_S+")
		play_notes(raag[selected_raag[0]][selected_raag[1]])
		pass

	raag_selector = []
	for a_raag in raag:
		raag_selector.append((a_raag, a_raag))

	# raag_selector = [('aroha', 'a'), ('avaroha', 'b'), ('pakad', 'c')]
	raag_property = [('aroha', 'a'), ('avaroha', 'b'), ('pakad', 'c')]

  	# Widget examples
	menu = pygame_menu.Menu('Welcome', 800, 600,
							theme=pygame_menu.themes.THEME_BLUE)
	# menu.add.selector('Raag :', raag_selector, onchange=set_raag)
	menu.add.dropselect('Raag :', raag_selector, onchange=set_raag)
	menu.add.dropselect('Property :', raag_property, onchange=set_raag_property)
	menu.add.button('Play', playsound)
	menu.add.button('Quit', pygame_menu.events.EXIT)
	menu.mainloop(screen)


if __name__ == "__main__":
	# execute only if run as a script
	raag = read_raag_data()
	start_ui(raag)