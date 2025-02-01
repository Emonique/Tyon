import hashlib
import base64
import random
import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class EncryptionManager:
    """
    A class responsible for all encryption and decryption operations in the Tyon system.

    It includes dynamic encryption key generation, data encryption/decryption, and the ability to 
    generate self-modifying licenses and watermarks. The system utilizes entropy sources to ensure 
    security and unpredictability.
    """

    def __init__(self, initial_key_seed=None, user_email=None):
        """
        Initializes the EncryptionManager with optional initial key seed and user email.

        Args:
            initial_key_seed (str): A seed value used to generate dynamic encryption keys. If None, a random UUID is used.
            user_email (str): The user's email address. Used for generating dynamic licenses.

        Attributes:
            initial_key_seed (str): The seed for the encryption process.
            user_email (str): The email of the user for personalized encryption.
            license_key (str): The generated dynamic license key.
            encryption_key (str): The generated encryption key based on entropy and randomness.
        """
        self.initial_key_seed = initial_key_seed or str(uuid.uuid4())
        self.user_email = user_email
        self.license_key = self.generate_dynamic_license(user_email) if user_email else None
        self.encryption_key = self.generate_dynamic_encryption_key()

    def generate_dynamic_license(self, email):
        """
        Generates a self-modifying, unpredictable license key based on the user's email 
        and a dynamic entropy source.

        Args:
            email (str): The user's email used to create a unique license key.

        Returns:
            str: A dynamically generated license key.
        """
        seed = f"{email}-{self.initial_key_seed}-{time.time()}"
        dynamic_license = hashlib.sha256(seed.encode()).hexdigest()

        return dynamic_license

    def generate_dynamic_encryption_key(self):
        """
        Generates an evolving encryption key using a combination of entropy and randomness 
        to ensure unpredictability.

        Returns:
            str: A dynamically generated encryption key.
        """
        entropy_source = f"{self.initial_key_seed}-{time.time()}-{random.random()}"
        encryption_key = hashlib.sha256(entropy_source.encode()).hexdigest()

        return encryption_key

    def encrypt_data(self, data):
        """
        Encrypts data using the evolving encryption key. The data is first base64-encoded and 
        then encrypted using XOR-based encryption combined with the encryption key.

        Args:
            data (str): The data to be encrypted.

        Returns:
            str: The encrypted data.
        """
        encoded_data = base64.b64encode(data.encode()).decode()
        encrypted_data = ''.join(
            chr(ord(c) ^ int(self.encryption_key[i % len(self.encryption_key)], 16))
            for i, c in enumerate(encoded_data)
        )
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the encrypted data using the evolving encryption key. The process reverses 
        the encryption and decodes the data back to its original format.

        Args:
            encrypted_data (str): The encrypted data to be decrypted.

        Returns:
            str: The decrypted data.
        """
        decoded_data = ''.join(
            chr(ord(c) ^ int(self.encryption_key[i % len(self.encryption_key)], 16))
            for i, c in enumerate(encrypted_data)
        )
        return base64.b64decode(decoded_data.encode()).decode()

    def add_hidden_watermark(self, image_path, output_path):
        """
        Embeds an evolving watermark into an image using the encryption system. The watermark 
        is encrypted and placed in a random position on the image.

        Args:
            image_path (str): The path to the image file.
            output_path (str): The path where the watermarked image will be saved.
        """
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Generate and encrypt the watermark
        hidden_watermark = f"TYON-{self.generate_dynamic_license(self.user_email)}"
        encrypted_watermark = self.encrypt_data(hidden_watermark)

        # Randomly position the watermark
        width, height = image.size
        position = (random.randint(0, width - 200), random.randint(0, height - 50))

        draw.text(position, encrypted_watermark, fill=(255, 255, 255), font=font)
        image.save(output_path)

    def embed_evolving_metadata(self, image_path, output_path):
        """
        Embeds encrypted metadata into an image. The metadata includes user information 
        and license keys, which are encrypted and saved in the image.

        Args:
            image_path (str): The path to the image file.
            output_path (str): The path to save the image with encrypted metadata.
        """
        image = Image.open(image_path)
        metadata = image.info
        metadata["Tyon-Watermark"] = self.encrypt_data(f"User:{self.user_email}, License:{self.license_key}")

        encrypted_metadata = self.encrypt_data(str(metadata))
        image.save(output_path, "PNG", pnginfo={"Tyon-Encrypted-Metadata": encrypted_metadata})

    def read_evolving_metadata(self, image_path):
        """
        Retrieves encrypted metadata from an image and decrypts it using the encryption key.

        Args:
            image_path (str): The path to the image file containing the encrypted metadata.

        Returns:
            str: The decrypted metadata, or a message indicating no metadata is found.
        """
        image = Image.open(image_path)
        encrypted_metadata = image.info.get("Tyon-Encrypted-Metadata", "")
        if encrypted_metadata:
            return self.decrypt_data(encrypted_metadata)
        return "No Metadata Found"

    def validate_license(self, license_key):
        """
        Validates the evolving license key by checking if it matches any stored license 
        in the database.

        Args:
            license_key (str): The license key to be validated.

        Returns:
            bool: True if the license key is valid, False otherwise.
        """
        conn = sqlite3.connect("tyon_licenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT license_key FROM licenses WHERE license_key = ?", (license_key,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_key = result[0]
            if stored_key == license_key:
                return True
        return False

    def revoke_license(self, license_key):
        """
        Revokes a license dynamically and evolves the encryption system by changing the 
        encryption key. This ensures that the system evolves in case of license issues.

        Args:
            license_key (str): The license key to be revoked.
        """
        conn = sqlite3.connect("tyon_licenses.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM licenses WHERE license_key = ?", (license_key,))
        conn.commit()
        conn.close()

        # Evolve the system by modifying the encryption key
        self.encryption_key = self.generate_dynamic_encryption_key()
        print(f"License {license_key} revoked. Encryption system evolved.")

    def monitor_and_evolve(self, license_key):
        """
        Monitors access attempts and evolves the system when unauthorized access is detected.

        Args:
            license_key (str): The license key to monitor.

        Returns:
            bool: True if the license is valid and access is allowed, False if unauthorized access is detected.
        """
        valid = self.validate_license(license_key)
        if not valid:
            print("Unauthorized access attempt detected.")
            self.revoke_license(license_key)  # Revoke and evolve the system
            return False
        return True
