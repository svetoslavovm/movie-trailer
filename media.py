import webbrowser


class Movie():
    """ A class that store basic movie information """

    def main():
        print('main RUNS !')

    def __main__():
        print(' __main__ RUNS !')

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
        if __name__ == '__main__':
            # execute only if run as a script
            main()
            __main__()

            # __module__  <- what would this do ???

        # print(self.title)
        return self.title
