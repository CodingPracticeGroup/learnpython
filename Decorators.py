def Type_Check(correct_type):
    #put code here
    def dec(old_func):
    	def new_func(arg):
            if type(arg) is correct_type:
                return old_func(arg)
            else:
                print "Bad Type"
        return new_func
    return dec

@Type_Check(int)
def Times2(num):
    return num*2

print Times2(2)
Times2('Not A Number')

@Type_Check(str)
def First_Letter(word):
    return word[0]

print First_Letter('Hello World')
First_Letter(['Not', 'A', 'String'])