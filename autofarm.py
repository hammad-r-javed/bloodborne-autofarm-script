from pynput.keyboard import Key as KK
from pynput.keyboard import Controller as KC
import time

MAX_RUN_COUNT = 1

kc = KC()

time.sleep(6)

def single_key_press(c, duration=0.1):
	kc.press(c)
	time.sleep(duration)
	kc.release(c)

def single_cylce():
	print('get into position')
	single_key_press('w', duration=3)
	single_key_press('a', duration=1)

	print('wait for death')
	time.sleep(19)

	print('select bold hunters mark')
	single_key_press('v')

	print('use bold hunters mark')
	time.sleep(0.5)
	single_key_press('n')

	print('wait for loading screen')
	time.sleep(8)

def restock():
	print('move to lantern')
	single_key_press('w', duration=1.3)

	print('select lantern')
	time.sleep(0.5)
	single_key_press('n')

	print('hover over yes')
	single_key_press(KK.left)

	print('press yes')
	time.sleep(0.5)
	single_key_press('n')

	print('wait for loading screen')
	time.sleep(9.5)

	print('move to store')
	single_key_press('w', duration=1.2)
	single_key_press('a', duration=1.3)
	single_key_press('w', duration=2.5)

	print('open store')
	single_key_press('n')

	print('press acquire items')
	time.sleep(0.7)
	single_key_press('n')

	print('hover over bold hunters mark')
	time.sleep(1)
	for x in range(3):
		single_key_press(KK.up)
		time.sleep(0.2)

	print('select bold hunters mark')
	time.sleep(1)
	single_key_press('n')

	print('select max number of bold hunters marks')
	time.sleep(0.5)
	single_key_press(KK.down)

	print('purchase hunters marks')
	time.sleep(0.5)
	single_key_press('n')

	print('exit shop')
	time.sleep(0.5)
	single_key_press('b')
	time.sleep(0.7)
	single_key_press('b')

	print('move back to chalice gravestone')
	time.sleep(0.5)
	single_key_press('s', duration=2)
	single_key_press('a', duration=1.4)
	single_key_press('w', duration=0.9)

	print('enter chalice')
	time.sleep(0.5)
	single_key_press('n')
	time.sleep(1.5)
	single_key_press('n')
	
	print('wait for loading screen')
	time.sleep(11)

	print('set position - consume 1 hunters mark')
	single_key_press('v')
	time.sleep(0.5)
	single_key_press('n')

	print('wait for loading screen')
	time.sleep(8)

run_count = MAX_RUN_COUNT

while True:
	while run_count != 0:
		single_cylce()
		run_count -= 1

	restock()
	run_count = MAX_RUN_COUNT
