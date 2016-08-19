#Change the loop so it counts up to 9 (inclusive).
#Be careful not to change or remove the count += 1 bit—if Python has no way to increase count, your loop could go on forever and become an infinite loop
count = 0
if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1