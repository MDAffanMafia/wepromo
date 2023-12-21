# WePromo

## The Social Media Platform for Creators, by Creators, and Fueled by Creators.

Welcome to WePromo, the social media platform designed specifically for creators who want to collaborate, learn from their peers, and grow together. This documentation will guide you through the installation process, usage, features, contributing guidelines, license information, and how to get in touch.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MDAffanMafia/wepromo.git
   cd wepromo
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

Now you can access the project locally at 'http://localhost:8000'.

## Usage

1. Visit 'http://localhost:8000' in your web browser.
2. Log in with your superuser account or create a new account.
3. Explore the different features such as user feed, adding posts, chatting, and joining groups.

## Features

WePromo is a Django-based project with a variety of functionalities within the app:

- accounts: User accounts
- admin: Customization of the admin interface
- userFeed: Users can view content posted by other creators.
- addPost: Users can share their content to help them grow.
- chatting: Enjoy asynchronous chatting with other creators.
- group: Join communities of people with similar interests.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.
6. Please adhere to the code style and formatting guidelines.

If you encounter any issues or have ideas for improvements, please open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further assistance, feel free to reach out to the project maintainer:

- MDAffanMafia
  - Email: shaikhaffan005@gmail.com
  - GitHub: [MDAffanMafia](https://github.com/MDAffanMafia)

Thank you for using WePromo! Happy creating!


