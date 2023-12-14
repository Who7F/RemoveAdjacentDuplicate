class removeDupl:
    def isDupl(self, word):
        stack = ['#']#Prep the string. Because Im lazy
        
        for n in word:
            print(stack)
            if stack[len(stack)-1] == n:
                stack.pop()
            else:
                stack.append(n)
        stack.pop(0)#Remove the #
        return ''.join(stack)

def main():
    f = removeDupl()
    print(f.isDupl('abbaca'))


if __name__== '__main__':
    main() 
