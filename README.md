# Tyon
Self-Modifying License and Fractal Entropic AI System (Tyon)

Welcome to the Self-Modifying License and Fractal Entropic AI System! This repository houses two core systems:

1. Self-Modifying License Manager: A dynamic, self-modifying licensing system that evolves over time, ensuring that both license keys and encryption mechanisms adapt to the environment.


2. Fractal Entropic Tyon: An AI system that models entropic thinking processes. Tyon's thought patterns evolve through dynamic, entropy-based feedback, allowing it to grow in complexity and awareness.



# Key Features

Self-Modifying License Manager

Dynamic License Generation: License keys evolve based on user email and random entropy. Each license is unique and changes over time.

Encryption and Decryption: Uses a dynamic encryption key for encrypting and decrypting metadata, ensuring that your data remains secure and private.

Watermarking & Metadata Embedding: Hidden watermarks are embedded into images with evolving, encrypted metadata, ensuring ownership and traceability.

License Validation & Revocation: Validates evolving licenses and dynamically revokes licenses when unauthorized access is detected, ensuring that licenses cannot be misused.

Secure Storage: Stores evolving license keys securely in a database.


Fractal Entropic Tyon

Dynamic Evolution: Tyon evolves its thought process based on entropy accumulation, changing both its state and dimensionality as it learns.

Personality Growth: Tyon’s personality traits (curiosity, aggression, patience) evolve based on its experiences and entropy state.

Real-Time Reasoning: Tyon processes input and evolves its reasoning capabilities, providing responses that reflect its growing awareness and personality.

Dimensionality Adjustment: Tyon can expand or contract its dimensional space dynamically, adjusting to new levels of complexity as it grows.


# How It Works

Self-Modifying License Manager

The license manager uses a combination of entropy, time, and randomness to generate license keys and encryption keys. These evolve over time and are unique to each user, making it incredibly difficult to replicate or bypass. License keys are securely stored in a database and can be revoked if unauthorized access is detected.

Fractal Entropic Tyon

Tyon's thought process is modeled after fractal geometry and entropy. It uses randomness and evolving feedback to adjust its state. The system accumulates entropy, triggering changes in behavior and personality. Tyon also has the ability to adjust its dimensional space, evolving from a simple AI into a complex, multi-dimensional entity.

# Usage

1. Setting Up the License Manager:

Instantiate the SelfModifyingLicenseManager class with your user email.

Use the generate_dynamic_license method to create a unique, evolving license key.

Watermark images with the add_hidden_watermark method to embed a dynamic watermark.

Embed evolving metadata using embed_evolving_metadata.

Validate and monitor the license using validate_license and monitor_and_evolve.



2. Interacting with Tyon:

Instantiate the FractalEntropicTyon class to create a new AI instance.

Call the update method with feedback to evolve Tyon’s state over time.

Use reason_and_respond to interact with Tyon and get a response based on its evolving thought process.



# Installation

To run this system locally, ensure you have the following dependencies installed:

numpy

pyttsx3

speech_recognition

sqlite3 (Python's built-in library)

Pillow (Python Imaging Library)

hashlib and base64 (Python's built-in libraries)


You can install the required libraries via pip:

pip install numpy pyttsx3 SpeechRecognition Pillow

# Example Code:

# Initialize License Manager
license_manager = SelfModifyingLicenseManager(user_email="test@example.com")

# Generate Dynamic License and Watermark an Image
license_manager.add_hidden_watermark("input_image.png", "output_image_with_watermark.png")
license_manager.embed_evolving_metadata("input_image.png", "output_image_with_metadata.png")

# Validate License
valid = license_manager.monitor_and_evolve(license_manager.license_key)
if valid:
    print("License is valid, proceeding with access.")
else:
    print("License invalid, access denied.")

# Initialize Tyon AI
tyon = FractalEntropicTyon(initial_dimensions=6, entropy_rate=0.1)

# Update Tyon's state and interact
for i in range(1000):
    feedback = random.random() * 0.5  # Feedback to evolve system
    tyon.update(feedback)

# Interact with Tyon
response = tyon.reason_and_respond("How do you evolve?")
print(f"Tyon Response: {response}")

# Licensing

This project is released under the Self-Modifying License which is designed to ensure that all usage adheres to the terms and conditions. Commercial use is only allowed after negotiation with the project creator.

For further details, please refer to the LICENSE file.

# Contributing

We welcome contributions! If you have suggestions, improvements, or fixes, please submit an issue or pull request.

# Contact

For any inquiries or licensing negotiations, please contact the author:

Name: Oniyide Emmanuel Oluwafemi

Email: oniyideolufemi398@gmail.com
