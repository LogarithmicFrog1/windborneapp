import requests

url = "https://windbornesystems.com/career_applications.json"
data = {
    "career_application": {
        "name": "Dhruv Vaze",
        "email": "dhruv25@stanford.edu",
        "role": "Commercial Growth",
        "notes": "Excited to apply. Thanks for reviewing :)",
        "submission_url": "https://github.com/LogarithmicFrog1/windborneapp",
        "linkedin_url": "https://www.linkedin.com/in/dhruvvaze/",
        "resume_url": "https://drive.google.com/file/d/1IahAkB-TkESpcF_AqqifKM0-ne9b3Z7P/view?usp=sharing"
    }
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response body:", response.text)
