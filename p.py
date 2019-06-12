string="parush"
print(len(string))

text="programmer"
print(text.title())

text="python is easy to learn."
result=text.startswith('is easy')
print(result)

text="python programming is easy."
result=text.startswith('programming is',7)
print(result)

text="programming is easy"
result=text.startswith(('python','programming'))
print(result)
result=text.startswith(('is','easy','java'))



text='programming life'
print(text.rsplit())

grocery='milk,bread,butter'
print(grocery.rsplit(',',2))


quote='do small things with great love'
print(quote.rfind('things',10))

song='cold,cold heart'
replaced_song=song.replace('o','e')
print('original string:',song)
print('replaced string:',replaced_song)

translation={97: None, 98: None, 99: 105}
string="abcdef"
print("Original string:",string)

string="python is fun"
print(string.rpartition('is'))

random_string="     this is good"
print(random_string.rstrip())



string='xoxo love xoxo'
print(string.strip())
print(string.strip('xoxo e'))

random_string='   this is good'
print(random_string.lstrip())

string="THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())
string="this should all be lowercase."
print(string.swapcase())


string="this should be uppercase"
print(string.upper())


string="THIS SHOULD BE LOWERCASE"
print(string.lower())

string='cat'
width=5
print(string.rjust(width))


string='cat'
width=5
fillchar='*'

string='cat'
width=5
print(string.ljust(width))


string='cat'
width=5
fillchar='*'


numlist=['1','2','3','4']
separator=','
print(separator.join(numlist))
numTuple=('1','2','3','4')
print(separator.join(numTuple))


test={'mat':1,'that':2}
s='->'
print(s.join(test))
test={1:'mat',2:'that'}
s=','

string="THIS IS GOOD"
print(string.isupper());
string="THIS IS ALSO GOOD"

str='python'
print(str.isidentifier())
str='py thon'
print(str.isidentifier())


str1="root33"
if str1.isidentifier()==True:
    print(str1,'is a valid identifier')
else:
    print(str1,'is not a valid identifier')


s='12345'
print(s.isdigit())
s="good"


s="123"
print(s.isdigit())
s="abcdef"
print(s.isdigit())

s='1234'
print(s.isdecimal())
s='abcd123'
print(s.isdecimal())



print("hello {},your balance is {}.".format("abc",123.12))


quote="let it be,let it be,let it be"
result=quote.find("let it")
print("substring 'let it':",result)
result=quote.find('small')


str='xyz\t12345\tabc'
result=str.expandtabs()
print(result)


string="python is awesome,isn't it?"
substring="is"
count=string.count(substring)
print(count)


string="GOOD"	
print("lowercase string:",string.casefold())


string="python is basis"
capitalized_string=string.capitalize()
print('old string:',string)
print('capitalized string:',capitalized_string)



































