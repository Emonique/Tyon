import hashlib
import base64
import random
from PIL import Image, ImageDraw, ImageFont
import time


class SelfModifyingLicenseManager:
    def __init__(self, initial_key_seed=None, user_email=None):
        """Self-Modifying License and Watermarking System"""
        self.initial_key_seed = initial_key_seed or str(uuid.uuid4())  # Random seed for unpredictability
        self.user_email = user_email
        self.license_key = self.generate_dynamic_license(user_email) if user_email else None
        self.encryption_key = self.generate_dynamic_encryption_key()

    def generate_dynamic_license(self, email):
        """Generates a self-modifying, unpredictable license key."""
        # License generation uses both email and random entropy to evolve the key
        seed = f"{email}-{self.initial_key_seed}-{time.time()}"
        dynamic_license = hashlib.sha256(seed.encode()).hexdigest()

        # Store the evolving license key
        conn = sqlite3.connect("tyon_licenses.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO licenses (user_email, license_key) VALUES (?, ?)", 
                       (email, dynamic_license))
        conn.commit()
        conn.close()

        return dynamic_license

    def generate_dynamic_encryption_key(self):
        """Generate an evolving encryption key using entropy and randomness."""
        entropy_source = f"{self.initial_key_seed}-{time.time()}-{random.random()}"
        encryption_key = hashlib.sha256(entropy_source.encode()).hexdigest()
        return encryption_key

    def encrypt_data(self, data):
        """Encrypt data (watermark/metadata) in an evolving manner."""
        encoded_data = base64.b64encode(data.encode()).decode()
        encrypted_data = ''.join(
            chr(ord(c) ^ int(self.encryption_key[i % len(self.encryption_key)], 16))
            for i, c in enumerate(encoded_data)
        )
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypt data using the evolving encryption key."""
        decoded_data = ''.join(
            chr(ord(c) ^ int(self.encryption_key[i % len(self.encryption_key)], 16))
            for i, c in enumerate(encrypted_data)
        )
        return base64.b64decode(decoded_data.encode()).decode()

    def add_hidden_watermark(self, image_path, output_path):
        """Embed evolving watermark in the image."""
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Generate hidden watermark based on evolving encryption and entropy
        hidden_watermark = f"TYON-{self.generate_dynamic_license(self.user_email)}"

        # Encrypt watermark text
        encrypted_watermark = self.encrypt_data(hidden_watermark)

        # Position watermark randomly
        width, height = image.size
        position = (random.randint(0, width - 200), random.randint(0, height - 50))

        draw.text(position, encrypted_watermark, fill=(255, 255, 255), font=font)
        image.save(output_path)

    def embed_evolving_metadata(self, image_path, output_path):
        """Embed evolving metadata into the image."""
        image = Image.open(image_path)
        metadata = image.info
        metadata["Tyon-Watermark"] = self.encrypt_data(f"User:{self.user_email}, License:{self.license_key}")

        # Encrypt metadata before embedding
        encrypted_metadata = self.encrypt_data(str(metadata))
        image.save(output_path, "PNG", pnginfo={"Tyon-Encrypted-Metadata": encrypted_metadata})

    def read_evolving_metadata(self, image_path):
        """Retrieve evolving metadata from the image."""
        image = Image.open(image_path)
        encrypted_metadata = image.info.get("Tyon-Encrypted-Metadata", "")
        if encrypted_metadata:
            return self.decrypt_data(encrypted_metadata)
        return "No Metadata Found"

    def validate_license(self, license_key):
        """Validate evolving license based on stored keys."""
        conn = sqlite3.connect("tyon_licenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT license_key FROM licenses WHERE license_key = ?", (license_key,))
        result = cursor.fetchone()
        conn.close()

        # Ensure license is evolving by comparing the encryption of key
        if result:
            stored_key = result[0]
            if stored_key == license_key:
                return True
        return False

    def revoke_license(self, license_key):
        """Evolve the system and revoke a license dynamically."""
        conn = sqlite3.connect("tyon_licenses.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM licenses WHERE license_key = ?", (license_key,))
        conn.commit()
        conn.close()

        # Modify encryption and watermarking systems when a license is revoked
        self.encryption_key = self.generate_dynamic_encryption_key()
        print(f"License {license_key} revoked. Encryption system evolved.")

    def monitor_and_evolve(self, license_key):
        """Monitor access, evolve system, and adapt to unauthorized access attempts."""
        valid = self.validate_license(license_key)
        if not valid:
            print("Unauthorized access attempt detected.")
            self.revoke_license(license_key)  # Revoke and evolve the system
            return False
        return True
