class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}\n")

    def display_timeline(self):
        return f'{self.username.upper()}\n{self.add_post(self, content)}'
    
    

def main():
    user = SocialMediaProfile('johndoe')
    print(user.display_timeline())

if __name__ =="__main__":
    main()
