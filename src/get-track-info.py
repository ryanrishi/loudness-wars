from client import sp


def get_track_info(name, artist):
    query = '%s %s' % (name, artist)
    results = sp.search(q=query)
    return results
    
    
if __name__ == "__main__":
    print get_track_info("All Star", "Smash Mouth")