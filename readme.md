Experience:
Alright, so how did I solve this algorithmic problem. Well the first thing did
was read the problem over. Next, I watched the videos through. I'll admit, I
broke my algorithmic flowchart just a bit because I did some research on
BFS via Google. I quickly found that it was the one to use. I wrote up some code
fairly quickly and hit my head against a wall. Since I was not writing unit
tests outside the instructor tests, I was passing 0/74 of the hidden tests.
I talked with my TA though and was able to get over that hump and made it up
to 69/74. I got stuck though. With the help of another TA I was able to come
up with a solution that passed all hidden instructor tests. There's
a caveat with that though as I'll explain in my explanation.

Explanation:
So the way my code works is that it loads in the data like I have for the
past couple coding assignments. It makes a dictionary of dictionaries, where
the dictionaries are mapped to their names. You could make this lighter, but
it is not effecting my Big O, so I am not too concerned.

The way I found Dr. Bart (the furthest room away from the start room(first room)) was that I kept
track of all the rooms that I visited. I then added that first room's edges to a queue and put the first
room into my traversed list so that I did not visit it again. I do the same process within a while loop,
appending to my queue as I go. Once my queue is empty, I know that the last room I visited was the
last room in my traversed list, which is Dr. Bart's room. 

Now I handle the ATDB's with a similar algorithm, but coded it a little bit differently. There's still a
traversed list and queue again, but now my queue is a list of lists. This is because we are keeping track
of different paths between rooms, so that way we make sure we don't go through the same path again.
The Big O for this would be O(RV+RE) where R is the number of robots, V is the number of rooms, 
and E is the number of connections. In this worst case all robots are at the furthest possible room
away from Dr. Bart and the last path checked. I said would be the worst case, and most of the time
it would be. There's one issue though. For some reason my code was producing a single loop for one of the
test cases. I was able to get the correct output, but the fix is just a patch since it still loop, the loop
is just deleted from the path. It seems to be a rarer issue since I only failed 5 test cases back before I
I half-fixed it. In other words most of the time my code runs in O(RV+RE), but there is at least one edge
case where it is slightly (only loops once, never more than once) worse.