import webbrowser


class Movie():
    """ A class that store basic movie information """

    # Initialize class instance with appropriate values
    def __init__(self, title, storyline, image_url, youtube_url):

        self.title = title
        self.storyline = storyline
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url

    # Opens default browser and loads movie url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # Returns movile title
    def get_title(self):
        
        return self.title
