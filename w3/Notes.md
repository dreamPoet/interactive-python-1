Computer monitor - 2D grid of pixels stored in frame buffer
computers update the monitor based on the frame buffer at rate of around 60-72 times a second - refresh rate

many app. will register a special func. called a "draw handler".

origin in the upper left

for this module, when drawing elements, the position is the lower left of the drawn object.


str[-1] can be the last elem of string; str[-2], the second last lem.
str[-1] = str[len(str)-1]
len(str) (no \0 etc, just the number of elem of the str)
str[0:3] from 0 up to 3 but not include 3.
str[:3] from beginning
str[2:] to end


python does not support i++
python for:
 for letter in 'str' :'s'; 't'; 'r'
 for item in [a,b,c]: a;b;c
 for idex in range(0,5) 0 1 2 3 4

invalid: int("5.4")


if we change element of a list in a func, we do not need to set global list; as it does not change the whole list but just elem.

python 3:  /: real division //: int division