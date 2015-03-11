'''
Created on Mar 9, 2015

@author: Rembrandt
'''
import media
import fresh_tomatoes

def create_movies():
    life_is_beautiful = media.Movie("Life Is Beautiful"
                            ,"A jewish Italian book shop owner, who must employ his fertile imagination to shield his son from the horrors of internment in a Nazi concentration camp"
                            ,"http://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg"
                            ,"https://www.youtube.com/watch?v=GCc2amcxwlA")
    
    memento = media.Movie("Memento"
                            ,"A man creates a strange system to help him remember things; so he can hunt for the murderer of his wife without his short-term memory loss being an obstacle"
                            ,"http://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg"
                            ,"https://www.youtube.com/watch?v=UFuFFdK7i44")    
    
    
    dead_men = media.Movie("Dead Men Don't Wear Plaid"
                            ,"Film noir parody with a detective uncovering a sinister plot"
                            ,"http://upload.wikimedia.org/wikipedia/en/1/1c/Deadmenplaidposter.jpg"
                            ,"https://www.youtube.com/watch?v=x2efDnLZjsk")
    
    last_mohicans = media.Movie("The Last of the Mohicans"
                            ,"Three trappers protect a British Colonel's daughters in the midst of the French and Indian War"
                            ,"http://upload.wikimedia.org/wikipedia/en/d/dd/Mohicansposter.jpg"
                            ,"https://www.youtube.com/watch?v=dn7UHJLcPp4")
    
    the_piano = media.Movie("The Piano"
                            ,"A mute woman along with her young daughter, and her prized piano, are sent to 1850s New Zealand for an arranged marriage to a wealthy landowner"
                            ,"http://upload.wikimedia.org/wikipedia/en/9/90/The-piano-poster.jpg"
                            ,"https://www.youtube.com/watch?v=I_kaUp8NDDU")
    
    brain_donors = media.Movie("Brain Donors"
                            ,"Three manic idiots; a lawyer, cab driver and a handyman team up to run a ballet company to fulfill the will of a millionaire"
                            ,"http://www.impawards.com/1992/posters/brain_donors.jpg"
                            ,"https://www.youtube.com/watch?v=zRkZwLk9fiw")
    
    return [life_is_beautiful, memento, dead_men, last_mohicans, the_piano, brain_donors]
    
if __name__ == "__main__":
    movies = create_movies()
    fresh_tomatoes.open_movies_page(movies)
