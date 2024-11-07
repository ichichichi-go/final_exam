from faker import Faker

def generate_fake_data(num_entries):
    fake = Faker()
    fake_data = []

    for _ in range(num_entries):
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        job_title = fake.job()  # Correct method name is 'job'
        company = fake.company()
        fake_data.append({
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "job_title": job_title,
            "company": company
        })

    return fake_data

def print_fake_data(fake_data):
    for entry in fake_data:
        # Improved readability by using formatted string literals
        print(f"Name: {entry['name']}")
        print(f"Email: {entry['email']}")
        print(f"Phone: {entry['phone_number']}")
        print(f"Job Title: {entry['job_title']}")
        print(f"Company: {entry['company']}")
        print('-' * 40)  # Separates entries for clarity

if __name__ == "__main__":
    num_entries = 10  # You can change this to generate more entries
    fake_data = generate_fake_data(num_entries)
    print_fake_data(fake_data)
