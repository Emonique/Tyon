Tyon - Contribution Guide

Thank you for considering contributing to Tyon! We welcome contributions from developers, researchers, and enthusiasts who are passionate about evolving AI systems, fractal-based data structures, and cognitive architectures. 
Please take a moment to review our contribution guidelines to help make the process as smooth as possible.

Table of Contents

Getting Started

How to Contribute

Code of Conduct

Contribution Rules

License


Getting Started

Prerequisites

Before you can start contributing, ensure you have the following:

Python 3.7 or higher installed

Necessary dependencies (listed in requirements.txt)

Familiarity with the project's code structure and philosophy

A GitHub account and access to the Tyon repository


Fork the Repository

To contribute to Tyon, fork the repository to your own GitHub account by clicking the "Fork" button at the top-right of the page.

Clone Your Fork

After forking, clone the repository to your local machine:

git clone https://github.com/YOUR-USERNAME/tyon.git
cd tyon

Create a Branch

Before making any changes, create a new branch for your feature or fix:

git checkout -b my-new-feature

Install Dependencies

Install the necessary dependencies to run Tyon locally:

pip install -r requirements.txt


How to Contribute

1. Identify the Area of Contribution:

Bug Fixes: If you find any bugs or issues, check the existing issues and see if your bug has already been reported. If not, create a new issue.

Features: If you want to add new features or enhancements to Tyon, feel free to open a feature request before starting development to confirm that it's something the project would benefit from.

Documentation: You can help by improving documentation, writing tutorials, or fixing typos in the existing docs.



2. Make Changes:

Write code or documentation according to the contribution guidelines.

Ensure you follow the style guide and write clean, readable, and well-commented code.



3. Testing:

Make sure all tests pass before submitting your pull request. If you add a new feature, please add unit tests to validate it.



4. Commit and Push:

Commit your changes using meaningful commit messages.

Push your changes to your forked repository:


git push origin my-new-feature


5. Create a Pull Request:

Once your branch is ready, open a pull request (PR) on the Tyon repository.

Provide a clear description of the changes you've made and the problem they solve.

If your PR addresses an issue, reference it in the description (e.g., "Fixes #42").




Code of Conduct

By participating in this project, you are expected to uphold the following principles:

Respectful Communication: Treat others with respect, kindness, and courtesy. This includes both verbal and written communication.

Collaborative Spirit: Collaborate constructively with other contributors and maintain a positive environment.

No Tolerance for Harassment: Harassment of any kind, including discriminatory remarks, will not be tolerated.


For more details, please refer to our Code of Conduct.



Contribution Rules

To ensure a high standard of code quality and maintainability, we ask that all contributors follow these rules:

1. Follow Coding Standards

Use the PEP 8 style guide for Python code.

Adhere to the existing code style (e.g., naming conventions, indentation, etc.).

Write docstrings for all functions and classes.


2. Modular Code

Write modular, reusable, and well-documented code. Tyon is designed to be a flexible and scalable framework, so aim to keep each component isolated and easily testable.


3. Testing

Ensure that you write unit tests for new features or bug fixes.

Make sure all existing tests pass before submitting a pull request.

Test your changes locally by running the test suite:


pytest

4. Clear Commit Messages

Your commit messages should be clear, concise, and follow this format:

Bug Fixes: "Fix issue where [describe problem]"

New Features: "Add [feature] to [module]"

Refactoring: "Refactor [module] to improve [aspect]"


Avoid "WIP" (Work in Progress) commits.


5. Documentation Updates

If you add a new feature or make changes to existing ones, update the documentation to reflect those changes.

Documentation should be written clearly and be accessible to both developers and non-developers.


6. Backward Compatibility

Always aim to maintain backward compatibility. If breaking changes are necessary, ensure you provide proper migration instructions.


7. Security Considerations

Be mindful of security when contributing. Ensure your code does not introduce vulnerabilities such as SQL injections, buffer overflows, or other common exploits.

Do not commit sensitive information (e.g., passwords, API keys).


8. Respect Licensing

Ensure that your contribution is compliant with the licensing terms of the project (MIT License).

Do not submit code that is copyrighted or under a license incompatible with Tyon’s.




License

By contributing to Tyon, you agree to license your contributions under the terms of the CC BY-NC-ND License.
