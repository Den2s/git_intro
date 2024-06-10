from subprocess import Popen
import sys

print('готовимся запустить процесс')
Popen([sys.executable, '-c', 'import time; time.sleep(3); print("дитё")'])
print('выходим')
