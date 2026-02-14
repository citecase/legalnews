import os
from github import Github

# GitHub Actions provides a default token, or you can use your own
token = os.getenv('GITHUB_TOKEN')
repo_name = os.getenv('GITHUB_REPOSITORY') # Automatically gets "user/repo"

def update_file():
    g = Github(token)
    repo = g.get_repo(repo_name)
    
    # Logic to fetch LiveLaw (placeholder for your scraping/update logic)
    new_content = "# LiveLaw Updates\n- Updated on 2026-02-14"
    
    file_obj = repo.get_contents("updates.md")
    repo.update_file(file_obj.path, "Scheduled Update", new_content, file_obj.sha)

if __name__ == "__main__":
    update_file()
