from lesson_package import human
from lesson_package import utils

f = utils.say_hello(human.sing())

f = human.cry
print(f)

g = human.cry()
print(g)
