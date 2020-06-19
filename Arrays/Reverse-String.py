# reverse string 
#'hi my name' => 'eman ym ih'
# if input is not string or length is less then 2 or empty string  => output string

# use slicing  - more efficient way , changes will happen in place
def reverse_str(string):
    if (type(string) != str or string == '' or len(string) < 2):
        return string
    else:
        return string[::-1]
    
 # use list reverse   - convert string into list and then reverse and join. Need memory for list.
def reverse_str1(string):
    if (type(string) != str or string == '' or len(string) < 2):
        return string
    else:
        newstr = list(string)
        newstr.reverse()
        return ''.join(newstr)

#Calling the function        
print(reverse_str1('hi my name'))
print(reverse_str('hi my name'))