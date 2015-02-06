#!/usr/bin/env python
#easy recommendation
import recommendations

def loadMovies(path='data/'):
    movies={}
    #get movie_id from u.item
    for line in open('u.item'):
        (id,title) = line.split('|')[0:2]
        movies[id] = title
    
    #load info
    prefs={}
    for line in open('u.data'):
        (user,movieid,rating,ts) = line.split('\t')
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

if __name__ == '__main__':
    data = loadMovies()
    print recommendations.getRecommendations(data, '87')[0:30]
     

