def main():
    followers = read_usernames("followers.txt")
    following = read_usernames("following.txt")
    
    not_following_back = find_not_following_back(followers, following)
    
    with open("not_following_back.txt", "w") as f:
        for user in not_following_back:
            f.write(user + "\n")
    
    print("List of users who don't follow you back saved to 'not_following_back.txt'.")

def read_usernames(filename):
    usernames = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2): 
            usernames.append(lines[i].strip())
    return usernames

def find_not_following_back(followers, following):
    return [user for user in following if user not in followers]

main()
