import tkinter as tk
from tkinter import messagebox
from instabot import Bot
import time
import threading

# Function to log in and fetch user details
def login_and_show_followers(username, password):
    bot = Bot()
    bot.login(username=username, password=password)

    # Fetch followers and following count
    user_info = bot.get_user_info(username)
    followers = user_info.get('followers', 0)
    following = user_info.get('following', 0)
    
    return bot, followers, following

# Function to simulate increasing followers every hour (for educational purposes)
def increase_followers_simulation(bot, username, label_followers):
    while True:
        time.sleep(3600)  # Wait for 1 hour
        # Simulate followers increase (for educational purposes, not real action)
        followers_count = bot.get_user_info(username)['followers'] + 100
        label_followers.config(text=f"Followers: {followers_count}")
        print(f"Followers increased to {followers_count}")

# Function to simulate liking posts
def like_posts(bot):
    # Get the posts that the bot is interested in liking (can be modified as needed)
    posts = bot.get_user_medias(bot.user_id, filtration=False)
    if not posts:
        messagebox.showwarning("No Posts Found", "No posts to like.")
        return
    
    # Simulate liking the first post for educational purposes
    post_id = posts[0]  # Get the first post ID
    bot.like(post_id)
    messagebox.showinfo("Action Simulated", f"Post {post_id} liked!")

# Function to simulate commenting on posts
def comment_on_posts(bot):
    # Get the posts that the bot is interested in commenting (can be modified as needed)
    posts = bot.get_user_medias(bot.user_id, filtration=False)
    if not posts:
        messagebox.showwarning("No Posts Found", "No posts to comment on.")
        return
    
    # Simulate commenting on the first post for educational purposes
    post_id = posts[0]  # Get the first post ID
    comment = "Nice post!"
    bot.comment(post_id, comment)
    messagebox.showinfo("Action Simulated", f"Comment '{comment}' posted on post {post_id}!")

# Function to simulate adding followers (for educational purposes)
def add_followers_simulation(bot, username, label_followers):
    messagebox.showinfo("Action Simulated", "Simulating adding followers...")
    new_followers = bot.get_user_info(username)['followers'] + 100
    label_followers.config(text=f"Followers: {new_followers}")
    print(f"Followers increased to {new_followers}")

# Function to handle login and update UI
def handle_login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password")
        return

    try:
        bot, followers, following = login_and_show_followers(username, password)
        
        # Update UI with follower and following count
        label_followers.config(text=f"Followers: {followers}")
        label_following.config(text=f"Following: {following}")
        
        # Start the simulation in a separate thread (so UI remains responsive)
        threading.Thread(target=increase_followers_simulation, args=(bot, username, label_followers), daemon=True).start()
        
        messagebox.showinfo("Login Success", f"Logged in as {username}")

    except Exception as e:
        messagebox.showerror("Login Failed", f"Failed to log in: {str(e)}")

# Main UI Setup
root = tk.Tk()
root.title("Instagram Bot - Educational Purposes")

# Set the window size and simple color theme
root.geometry("400x400")
root.configure(bg="#f5f5f5")

# Username and Password Entry
tk.Label(root, text="Instagram Username:", bg="#f5f5f5", font=("Arial", 12)).pack(pady=10)
entry_username = tk.Entry(root, width=30, font=("Arial", 12))
entry_username.pack(pady=5)

tk.Label(root, text="Instagram Password:", bg="#f5f5f5", font=("Arial", 12)).pack(pady=10)
entry_password = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry_password.pack(pady=5)

# Login Button
btn_login = tk.Button(root, text="Login", command=handle_login, width=15, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_login.pack(pady=20)

# Display follower and following counts
label_followers = tk.Label(root, text="Followers: 0", bg="#f5f5f5", font=("Arial", 12))
label_followers.pack(pady=5)

label_following = tk.Label(root, text="Following: 0", bg="#f5f5f5", font=("Arial", 12))
label_following.pack(pady=5)

# Action Buttons (Simulate actions)
btn_add_followers = tk.Button(root, text="Add Followers", command=lambda: add_followers_simulation(bot, entry_username.get(), label_followers), width=20, bg="#2196F3", fg="white", font=("Arial", 12))
btn_add_followers.pack(pady=10)

btn_like_posts = tk.Button(root, text="Like Posts (Simulate)", command=lambda: like_posts(bot), width=20, bg="#FF9800", fg="white", font=("Arial", 12))
btn_like_posts.pack(pady=10)

btn_comment_on_posts = tk.Button(root, text="Comment on Posts (Simulate)", command=lambda: comment_on_posts(bot), width=20, bg="#9C27B0", fg="white", font=("Arial", 12))
btn_comment_on_posts.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
