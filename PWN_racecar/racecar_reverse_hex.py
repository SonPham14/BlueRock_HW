a = ['56f71340', '7b425448', '5f796877', '5f643164', '34735f31', '745f3376', '665f3368', '5f67346c', '745f6e30', '355f3368', '6b633474', '7d213f']




for i in a:
    print(chr(int(i[-2:], 16)), end='')
    for j in range(0, 5, 2):
        print(chr(int(i[-4-j:-2-j], 16)), end='')
        
        #print(chr(int(i[j:j+1],16)), end='')
