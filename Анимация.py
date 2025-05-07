print ('Запустите анимацию :')

a = '*'
a1 = input()
import time
time.sleep(0.01)
import os
os.system('clear')

if a1 == 'старт' :
    for i in range(1):
        print('\n' * 4, a, sep = '')
        #print ('\n')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

    for i in range(1):
        print('\n' * 3, a, '\n', '*' * 2,  '\n', '*' * 1, sep = '')
        #print ('\n')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

    for i in range(1):
        print('\n' * 2, a, '\n', '*' * 2, '\n', '*' * 3, '\n', '*' * 2,  '\n', '*' * 1, sep = '')
        #print ('\n')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

    for i in range(1):
        print('\n', a, '\n', '*' * 2, '\n', '*' * 3, '\n', '*' * 4, '\n', '*' * 3, '\n', '*' * 2,  '\n', '*' * 1, sep = '')
        #print ('\n')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')


    for i in range(1):
        print(a, '\n', '*' * 2, '\n', '*' * 3, '\n', '*' * 4, '\n', '*' * 5, '\n', '*' * 4, '\n', '*' * 3, '\n', '*' * 2,  '\n', '*' * 1, sep = '')
        #print ('\n')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

#Обратный отчет
    for i in range(1):
        print(' *', '\n', '*' * 3, '\n', '*' * 4, '\n', '*' * 5, '\n', '*' * 6 ,'\n', '*' * 5, '\n', '*' * 4, '\n', '*' * 3, '\n', ' *', sep = '')
        print ('\n')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

    for i in range(1):
        print('  *', '\n', ' *','*' * 2, '\n', '*' * 5, '\n', '*' * 6, '\n', '*' * 7 ,'\n', '*' * 6, '\n', '*' * 5, '\n', ' *','*' * 2, '\n', '  *', sep = '')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

    for i in range(1):
        print('   *', '\n', '  *','*' * 2, '\n', ' *', '*' * 4, '\n', '*' * 7, '\n', '*' * 8 ,'\n', '*' * 7, '\n', ' *', '*' * 4, '\n', '  *','*' * 2, '\n', '   *', sep = '')
    import time
    time.sleep(0.01)
    import os
    os.system('clear')

    for i in range(1):
        print('    *', '\n', '   *','*' * 2, '\n', '  *', '*' * 4, '\n', ' *', '*' * 6, '\n', '*' * 9 ,'\n', ' *', '*' * 6, '\n', '  *', '*' * 4, '\n', '   *','*' * 2, '\n', '    *', sep = '')
    
else :
    print ('Старт отложен')