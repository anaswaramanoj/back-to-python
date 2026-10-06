EX = {
"basics": [
 dict(task="Set <code>a = 5</code> and <code>b = 9</code>. Swap them in <b>one line</b>, then print both.",
      hint="Multiple assignment works on both sides: <code>x, y = ...</code>",
      sol='''a = 5
b = 9
a, b = b, a
print(a, b)'''),
 dict(task="Add 10 + 20 + 30 + 40 over <b>two lines</b> without using a backslash. Print the total.",
      hint="Wrap the whole sum in brackets.",
      sol='''total = (10 + 20 +
         30 + 40)
print(total)'''),
 dict(task="Use the <code>keyword</code> module to check whether <code>lambda</code> and <code>print</code> are keywords.",
      hint="<code>keyword.iskeyword(\"word\")</code> returns True or False.",
      sol='''import keyword
print(keyword.iskeyword("lambda"))
print(keyword.iskeyword("print"))'''),
],
"types": [
 dict(task="Remove the duplicates from <code>[3, 1, 3, 2, 1]</code> and get back a <b>sorted list</b>.",
      hint="Convert to a set to drop duplicates, then <code>sorted()</code> gives a list.",
      sol='''nums = [3, 1, 3, 2, 1]
print(sorted(set(nums)))'''),
 dict(task="Turn the text <code>\"123\"</code> into a number, add 7, then turn it back into text and stick <code>\"!\"</code> on the end.",
      hint="<code>int()</code> one way, <code>str()</code> the other.",
      sol='''n = int("123") + 7
print(str(n) + "!")'''),
 dict(task="Print just the type <b>name</b> of each of these: <code>5, 5.0, \"5\", [5], (5,), {5}, {5: 5}</code>.",
      hint="Loop over them. <code>type(v).__name__</code> gives the name as text.",
      sol='''for v in [5, 5.0, "5", [5], (5,), {5}, {5: 5}]:
    print(type(v).__name__)'''),
],
"io": [
 dict(task="With <code>name = \"Ana\"</code> and <code>age = 30</code>, print <code>Ana is 30 years old</code> using an f-string.",
      hint="<code>f\"{name} ...\"</code>",
      sol='''name = "Ana"
age = 30
print(f"{name} is {age} years old")'''),
 dict(task="Print pi to 2 decimal places, then to 4.",
      hint="<code>import math</code>, then <code>f\"{math.pi:.2f}\"</code>.",
      sol='''import math
print(f"{math.pi:.2f}")
print(f"{math.pi:.4f}")'''),
 dict(task="Ask the user for two numbers and print their sum.",
      hint="<code>input()</code> gives text. Wrap each in <code>int()</code> before adding.",
      sol='''a = int(input("First: "))
b = int(input("Second: "))
print(f"Sum: {a + b}")''', stdin="4\n5\n", out="First: 4\nSecond: 5\nSum: 9"),
],
"ops": [
 dict(task="Turn 135 minutes into hours and minutes, like <code>2 h 15 min</code>.",
      hint="<code>//</code> gives whole hours, <code>%</code> gives what's left.",
      sol='''minutes = 135
print(f"{minutes // 60} h {minutes % 60} min")'''),
 dict(task="Is 2024 a leap year? It is if it divides by 4, except years that divide by 100 but not by 400.",
      hint="<code>y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)</code>",
      sol='''y = 2024
print(y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))'''),
 dict(task="With <code>prices = {\"apple\": 1.2}</code>, check whether <code>\"apple\"</code> is a key and whether <code>1.2</code> is a value.",
      hint="<code>in</code> checks keys. For values use <code>in prices.values()</code>.",
      sol='''prices = {"apple": 1.2}
print("apple" in prices)
print(1.2 in prices.values())'''),
],
"flow": [
 dict(task="<b>FizzBuzz</b> for 1 to 15: print Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for both, otherwise the number.",
      hint="Check the \"both\" case first (<code>i % 15 == 0</code>).",
      sol='''for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''),
 dict(task="Add up all the even numbers from 1 to 100 with a <code>for</code> loop.",
      hint="<code>range(2, 101, 2)</code> gives just the evens.",
      sol='''total = 0
for n in range(2, 101, 2):
    total += n
print(total)'''),
 dict(task="Find the first number above 10 in <code>[7, 12, 9, 20, 3]</code> and stop there. Print <code>none found</code> if there isn't one.",
      hint="<code>break</code> when you find it, and put the \"none found\" in the loop's <code>else</code>.",
      sol='''for n in [7, 12, 9, 20, 3]:
    if n > 10:
        print(n)
        break
else:
    print("none found")'''),
 dict(task="Start at 100 and keep halving with <code>//</code> until you reach 1. Count how many steps that takes.",
      hint="<code>while n > 1:</code> then <code>n //= 2</code> and add 1 to a counter.",
      sol='''n = 100
steps = 0
while n > 1:
    n //= 2
    steps += 1
print(steps)'''),
],
"lists": [
 dict(task="From <code>[5, 3, 8, 1]</code> print the largest, the smallest, and the list sorted high-to-low <b>without changing the original</b>.",
      hint="<code>max</code>, <code>min</code>, and <code>sorted(..., reverse=True)</code>.",
      sol='''nums = [5, 3, 8, 1]
print(max(nums), min(nums))
print(sorted(nums, reverse=True))
print(nums)'''),
 dict(task="Split <code>\"the cat sat on a big mat today\"</code> into words and keep the words with 3 or more letters, in CAPITALS.",
      hint="<code>[w.upper() for w in words if len(w) >= 3]</code>",
      sol='''words = "the cat sat on a big mat today".split()
print([w.upper() for w in words if len(w) >= 3])'''),
 dict(task="Flatten <code>[[1, 2], [3, 4], [5]]</code> into <code>[1, 2, 3, 4, 5]</code> with one comprehension.",
      hint="Two <code>for</code>s, in the same order you'd write the loops: <code>[x for row in m for x in row]</code>.",
      sol='''m = [[1, 2], [3, 4], [5]]
print([x for row in m for x in row])'''),
 dict(task="Make a <b>real copy</b> of <code>[1, 2, 3]</code>, add 4 to the copy, and show the original didn't change.",
      hint="<code>.copy()</code> or <code>[:]</code>",
      sol='''a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a, b)'''),
],
"tuples": [
 dict(task="Write <code>min_max(nums)</code> that returns the smallest and largest as a tuple. Unpack the result into two names.",
      hint="<code>return min(nums), max(nums)</code> already makes a tuple.",
      sol='''def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 9, 1])
print(lo, hi)'''),
 dict(task="In <code>('a', 'b', 'a', 'c', 'a')</code>, count the <code>'a'</code>s and find where <code>'c'</code> is.",
      hint="<code>.count()</code> and <code>.index()</code>",
      sol='''t = ('a', 'b', 'a', 'c', 'a')
print(t.count('a'), t.index('c'))'''),
 dict(task="Sort <code>[(\"ana\", 30), (\"ben\", 25), (\"cy\", 35)]</code> by age (the second item).",
      hint="<code>sorted(pairs, key=lambda p: p[1])</code>",
      sol='''pairs = [("ana", 30), ("ben", 25), ("cy", 35)]
print(sorted(pairs, key=lambda p: p[1]))'''),
],
"sets": [
 dict(task="Ana's friends are <code>{\"ben\", \"cy\", \"dev\"}</code> and Ben's are <code>{\"cy\", \"dev\", \"eli\"}</code>. Print the friends they share, and the ones only Ana has.",
      hint="<code>&amp;</code> for shared, <code>-</code> for only-in-the-first. Wrap in <code>sorted()</code> for a tidy order.",
      sol='''ana = {"ben", "cy", "dev"}
ben = {"cy", "dev", "eli"}
print(sorted(ana & ben))
print(sorted(ana - ben))'''),
 dict(task="How many <b>different</b> words are in <code>\"to be or not to be\"</code>?",
      hint="<code>len(set(...split()))</code>",
      sol='''print(len(set("to be or not to be".split())))'''),
 dict(task="Check that every letter of <code>\"cab\"</code> appears in <code>\"abcdef\"</code>.",
      hint="Make both into sets and use <code>issubset</code>.",
      sol='''print(set("cab").issubset(set("abcdef")))'''),
],
"dicts": [
 dict(task="Count each letter in <code>\"banana\"</code> using a dict.",
      hint="<code>counts[ch] = counts.get(ch, 0) + 1</code>",
      sol='''counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)'''),
 dict(task="Flip <code>{'a': 1, 'b': 2}</code> so the values become keys.",
      hint="<code>{v: k for k, v in d.items()}</code>",
      sol='''d = {'a': 1, 'b': 2}
print({v: k for k, v in d.items()})'''),
 dict(task="Print each item in <code>{\"apple\": 1.2, \"bread\": 2.5}</code> as a price, like <code>apple: £1.20</code>.",
      hint="Loop with <code>.items()</code> and use <code>:.2f</code> in an f-string.",
      sol='''prices = {"apple": 1.2, "bread": 2.5}
for item, price in prices.items():
    print(f"{item}: £{price:.2f}")'''),
 dict(task="Merge <code>{'a': 1, 'b': 2}</code> and <code>{'b': 9, 'c': 3}</code>. Which <code>'b'</code> wins?",
      hint="<code>d1 | d2</code>. The right-hand dict wins on a clash.",
      sol='''d1 = {'a': 1, 'b': 2}
d2 = {'b': 9, 'c': 3}
print(d1 | d2)'''),
],
"strings": [
 dict(task="Count the vowels in <code>\"Programming in Python\"</code>.",
      hint="Loop over <code>s.lower()</code> and check <code>ch in \"aeiou\"</code>.",
      sol='''s = "Programming in Python"
print(sum(1 for ch in s.lower() if ch in "aeiou"))'''),
 dict(task="Turn <code>\"hello big world\"</code> into <code>\"World Big Hello\"</code>.",
      hint="<code>.title()</code>, <code>.split()</code>, reverse with <code>[::-1]</code>, then <code>' '.join()</code>.",
      sol='''s = "hello big world"
print(' '.join(s.title().split()[::-1]))'''),
 dict(task="Is <code>\"Never odd or even\"</code> a palindrome if you ignore spaces and capitals?",
      hint="Remove spaces with <code>.replace(\" \", \"\")</code>, lowercase it, compare with its reverse.",
      sol='''s = "Never odd or even"
clean = s.replace(" ", "").lower()
print(clean == clean[::-1])'''),
],
"functions": [
 dict(task="Write <code>area(width, height=1)</code>. Call it as <code>area(5)</code> and <code>area(5, 3)</code>.",
      hint="Give <code>height</code> a default in the <code>def</code> line.",
      sol='''def area(width, height=1):
    return width * height

print(area(5), area(5, 3))'''),
 dict(task="Write <code>average(*nums)</code> that takes any number of values and returns their mean.",
      hint="<code>nums</code> is a tuple, so <code>sum(nums) / len(nums)</code> works.",
      sol='''def average(*nums):
    return sum(nums) / len(nums)

print(average(2, 4, 9))'''),
 dict(task="Write a <b>recursive</b> <code>sum_digits(n)</code>, so <code>sum_digits(1234)</code> gives 10.",
      hint="Last digit is <code>n % 10</code>. The rest is <code>n // 10</code>. Stop when <code>n</code> is 0.",
      sol='''def sum_digits(n):
    return 0 if n == 0 else n % 10 + sum_digits(n // 10)

print(sum_digits(1234))'''),
 dict(task="Write <code>describe(**info)</code> that prints each <code>key: value</code> on its own line.",
      hint="<code>info</code> is a dict, so loop over <code>info.items()</code>.",
      sol='''def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe(name="Ana", city="Leeds")'''),
],
"builtins": [
 dict(task="Convert <code>[0, 25, 100]</code> Celsius to Fahrenheit with <code>map</code> and a lambda.",
      hint="F = C × 9/5 + 32",
      sol='''temps = [0, 25, 100]
print(list(map(lambda c: c * 9 / 5 + 32, temps)))'''),
 dict(task="Keep only the words starting with <code>\"p\"</code> from <code>[\"python\", \"java\", \"perl\", \"go\"]</code>, using <code>filter</code>.",
      hint="<code>w.startswith(\"p\")</code>",
      sol='''langs = ["python", "java", "perl", "go"]
print(list(filter(lambda w: w.startswith("p"), langs)))'''),
 dict(task="Print a numbered shopping list starting at 1: milk, eggs, bread.",
      hint="<code>enumerate(items, start=1)</code>",
      sol='''for i, item in enumerate(["milk", "eggs", "bread"], start=1):
    print(f"{i}. {item}")'''),
 dict(task="Find the biggest number in <code>[3, 9, 2]</code> using <code>reduce</code> (no <code>max</code>).",
      hint="<code>lambda a, b: a if a &gt; b else b</code>",
      sol='''from functools import reduce
print(reduce(lambda a, b: a if a > b else b, [3, 9, 2]))'''),
],
"modules": [
 dict(task="Use <code>math</code> to get the square root of 144 and round 4.2 <b>up</b>.",
      hint="<code>math.sqrt</code> and <code>math.ceil</code>",
      sol='''import math
print(math.sqrt(144), math.ceil(4.2))'''),
 dict(task="Import just <code>date</code> from <code>datetime</code> and print the current year.",
      hint="<code>from datetime import date</code>, then <code>date.today().year</code>.",
      sol='''from datetime import date
print(date.today().year)''', out="2026", norun=True),
 dict(task="Make your own module: a file <code>greetings.py</code> with a <code>hello(name)</code> function, used from <code>main.py</code>.",
      hint="Both files go in the same folder. In <code>main.py</code>: <code>import greetings</code>.",
      sol='''# greetings.py
def hello(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

# main.py
import greetings
print(greetings.hello("Ana"))''', out="Hello, Ana!", norun=True),
],
"numpy1": [
 dict(task="Make a 3×3 array of the numbers 1 to 9.",
      hint="<code>np.arange(1, 10)</code>, then <code>.reshape(3, 3)</code> folds it into rows.",
      sol='''import numpy as np
print(np.arange(1, 10).reshape(3, 3))'''),
 dict(task="Make 5 evenly spaced points from 0 to 100.",
      hint="<code>linspace</code> takes how many points you want.",
      sol='''import numpy as np
print(np.linspace(0, 100, 5))'''),
 dict(task="Make a 4×4 identity matrix and print its <code>shape</code> and <code>dtype</code>.",
      hint="<code>np.eye(4)</code>",
      sol='''import numpy as np
m = np.eye(4)
print(m.shape, m.dtype)'''),
],
"numpy2": [
 dict(task="From <code>np.arange(1, 11)</code>, keep only values above 5.",
      hint="A mask: <code>a[a &gt; 5]</code>",
      sol='''import numpy as np
a = np.arange(1, 11)
print(a[a > 5])'''),
 dict(task="For <code>[[1, 2, 3], [4, 5, 6]]</code>, print the column sums and the row sums.",
      hint="<code>axis=0</code> per column, <code>axis=1</code> per row.",
      sol='''import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x.sum(axis=0))
print(x.sum(axis=1))'''),
 dict(task="In <code>[3, -1, 4, -5, 2]</code>, replace every negative with 0.",
      hint="Assign through a mask: <code>a[a &lt; 0] = 0</code>",
      sol='''import numpy as np
a = np.array([3, -1, 4, -5, 2])
a[a < 0] = 0
print(a)'''),
 dict(task="Scale <code>[10, 20, 30]</code> so the smallest becomes 0 and the largest 1.",
      hint="<code>(x - x.min()) / (x.max() - x.min())</code>",
      sol='''import numpy as np
x = np.array([10, 20, 30])
print((x - x.min()) / (x.max() - x.min()))'''),
],
}
