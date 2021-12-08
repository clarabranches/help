import time
import pyautogui

time.sleep(3)  # tempo para posicionar o mouse no objeto desejado
pyautogui.position()  # captura as coordenadas em x e y da posição do mouse

# por apenas capturar a posição devemos usar outra forma de verificar a posição com:
print(pyautogui.position())  # imprimindo na tela
x = pyautogui.position()  # salvando em uma variável para utilizar futuramente


pyautogui.click(6, 757)  # clica no objeto capturado (configurando de forma manual)
pyautogui.click(x)  # clica no objeto capturado e salvo na variável


pyautogui.press('esc')  # usado para precionar uma tecla(no caso esc)
pyautogui.hotkey('ctrl', 'v')  # usado para precionar mais de uma tecla ao mesmo tempo


pyautogui.typewrite('clarabranches')  # usado para digitar algo
