#how a loop generally works in python
day_string=["it's","a","wonderful","day"]
for item in day_string:
    print(item)

#loops working internally using built in iter() method
#uses next() method to go to next item
iterator_obj= iter(day_string)
try:
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj)) 
    print(next(iterator_obj)) #throws an exception for crossing the length
except:
    print("Crossed the limit but forgive and move on")

#reverse iterator using reversed()
rev_itr=reversed(day_string)
print(next(rev_itr))
print(next(rev_itr))
print("--------------------------------------------------------")

#Let's define a class to show the use of iterators
class music_player():
    def __init__(self) -> None:
        self.songs_category=['Bollywood','Hollywood','Folk','Pop']
        self.index=-1 

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index == len(self.songs_category):
            raise StopIteration
        return self.songs_category[self.index]

print("Let's play music on this wonderful day!")
player= music_player()
itr=iter(player)
print(next(player))
print(next(player))
print(next(player))
print(next(player))

    
    