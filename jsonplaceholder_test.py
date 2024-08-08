import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        print("GET /posts:")
        print(response.json())
    else:
        print("Failed to retrieve posts")

def get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"GET /posts/{post_id}:")
        print(response.json())
    else:
        print("Failed to retrieve post")

def get_post_comments(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    if response.status_code == 200:
        print(f"GET /posts/{post_id}/comments:")
        print(response.json())
    else:
        print("Failed to retrieve comments")

def post_post():
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    if response.status_code == 201:
        print("POST /posts:")
        print(response.json())
    else:
        print("Failed to create post")

def put_post(post_id):
    data = {"title": "foo", "body": "bar updated", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    if response.status_code == 200:
        print(f"PUT /posts/{post_id}:")
        print(response.json())
    else:
        print("Failed to update post")

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"DELETE /posts/{post_id}: Successfully deleted")
    else:
        print("Failed to delete post")

if __name__ == "__main__":
    # Example usage:
    get_posts()
    get_post_by_id(1)
    get_post_comments(1)
    post_post()
    put_post(1)
    delete_post(1)

