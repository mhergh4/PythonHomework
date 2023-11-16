import requests

base_url = "https://jsonplaceholder.typicode.com"

def get_and_filter(endpoint):
    response = requests.get(f"{base_url}/{endpoint}")
    if response.status_code == 200:
        data = response.json()

        filtered_titles = [post['title'] for post in data if len(post['title'].split()) <= 6]

        filtered_body = [post for post in data if len(post.get('body', '').split('\n')) <= 3]

        return filtered_titles, filtered_body
    else:
        print(f"Error {response.status_code}: {response.text}")

def post_request(endpoint, data):
    response = requests.post(f"{base_url}/{endpoint}", json=data)
    return response.json()

def put_request(endpoint, data):
    response = requests.put(f"{base_url}/{endpoint}", json=data)
    return response.json()

def delete_request(endpoint):
    response = requests.delete(f"{base_url}/{endpoint}")
    return response.status_code

if __name__ == "__main__":
    titles, body = get_and_filter("posts")
    print("Filtered Titles:", titles)
    print("Filtered Body:", body)

    new_post_data = {
        "title": "New Post",
        "body": "This is a new post.",
        "userId": 1
    }
    created_post = post_request("posts", new_post_data)
    print("Created Post:", created_post)

    post_to_update_id = 1
    updated_post_data = {
        "title": "Updated Post",
        "body": "This post has been updated.",
        "userId": 1
    }
    updated_post = put_request(f"posts/{post_to_update_id}", updated_post_data)
    print("Updated Post:", updated_post)

    post_to_delete_id = 1
    delete_status = delete_request(f"posts/{post_to_delete_id}")
    print("Delete Status Code:", delete_status)
