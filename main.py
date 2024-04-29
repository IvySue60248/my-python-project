from user import User
from post import Post

app_user_one = User("ivy", "ivy@xue.com", "pwd", "Java Developer")
app_user_one.get_user_info()
app_user_one.change_job_title("QA")
app_user_one.get_user_info()

app_user_two = User("AA", "aa@aa.com", "abc", "Project Manager")
app_user_two.get_user_info()
app_user_two.change_password("abc123")
app_user_two.get_user_info()

new_post = Post("Hello World", "James Bond")
new_post.get_post_info()

