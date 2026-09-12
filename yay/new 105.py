#starting line 2-4, we are establishing what TRAILoff means. In this script, you can tell by the framework that the code is ment to make the snoring effect
def trailOff(trail):
    return trail[0] + trail[1] + "..."

# we now know that the trailoff os going to copy what you say
word = input("What word should I say?") 

#this is the final product of us giving the input. putting it ino the terminal will produce this answer I‘ll say {insert wurd}.. *snore*
print("Okay, I‘ll say " + trailOff(word) + " *snore*")