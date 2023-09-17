## Description
`Did you know that racecar spelled backwards is racecar? Well, now that you know everything about racing, win this race and get the flag!`
## Solving
As the name of the challenge, I should choose a car to win the race.
If I lost, I will lose all my coins and the program will exit.

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/442c29cc-a786-46af-943a-1b4b73d0eb30)

Else, I will get 100 coins then input something and ... the program will exit again.

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/53a73336-5f70-4e69-b5ec-5d6fb031a902)

Let's load the program into IDA to see what the program do.

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/dc56e573-b6ae-407f-98e5-c43091cbb94f)

Go to `car_menu` function.

Noticing to the following code. We can ignore the above code because they are not too important.

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/52376d88-3274-428e-9631-fea7cae17b99)

The code will print notification when I win and read the flag and store in stack before I input something.

Focus on 76th line. The `printf(buf)` has a vulnerability called [Format string vulnerability](https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability/). [Read More](https://owasp.org/www-community/attacks/Format_string_attack)

So, I use `%x` parameter to exploit that vulerability. It will pop off a stack values and print them in hexadecimal.
![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/d43ab6d3-7223-4987-ad91-6a53d60737fa)

Then I will try using 20 times of `%x` to leak 20 stacks and use CyberChef to convert Hex to ASCII.

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/8babf28c-f138-4437-83b4-1aa488d37914)

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/35528aaa-ad59-4592-ad0b-a92775c91fd3)

Alright, flag here but it is look like reversed. Of course, because Stack operates on the principle of "last in, first out" (LIFO). To get the flag, I write a script to reverse it.

![image](https://github.com/SonPham14/BlueRock_HW/assets/103044792/9e61be03-650d-467a-89f4-ba36572aefde)




