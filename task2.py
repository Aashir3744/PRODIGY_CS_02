from PIL import Image
import numpy as np
import random

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    encrypted_pixels = pixels.copy()
    
    random.seed(key)
    h, w = pixels.shape[:2]
    
    for i in range(h):
        for j in range(w):
            random_i = random.randint(0, h - 1)
            random_j = random.randint(0, w - 1)
            encrypted_pixels[i, j], encrypted_pixels[random_i, random_j] = encrypted_pixels[random_i, random_j], encrypted_pixels[i, j]
    
    encrypted_image = Image.fromarray(encrypted_pixels)
    return encrypted_image

def decrypt_image(encrypted_image, key):
    encrypted_pixels = np.array(encrypted_image)
    decrypted_pixels = encrypted_pixels.copy()
    
    random.seed(key)
    h, w = encrypted_pixels.shape[:2]
    
    swaps = []
    for i in range(h):
        for j in range(w):
            random_i = random.randint(0, h - 1)
            random_j = random.randint(0, w - 1)
            swaps.append(((i, j), (random_i, random_j)))
    
    for (i, j), (random_i, random_j) in reversed(swaps):
        decrypted_pixels[i, j], decrypted_pixels[random_i, random_j] = decrypted_pixels[random_i, random_j], decrypted_pixels[i, j]
    
    decrypted_image = Image.fromarray(decrypted_pixels)
    return decrypted_image

def main():
    while True:
        print("Image Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            key = input("Enter the encryption key: ")
            encrypted_image = encrypt_image(image_path, key)
            encrypted_image_path = image_path.replace('.', '_encrypted.')
            encrypted_image.save(encrypted_image_path)
            print(f"Encrypted image saved as {encrypted_image_path}\n")
        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt: ")
            key = input("Enter the decryption key: ")
            encrypted_image = Image.open(image_path)
            decrypted_image = decrypt_image(encrypted_image, key)
            decrypted_image_path = image_path.replace('.', '_decrypted.')
            decrypted_image.save(decrypted_image_path)
            print(f"Decrypted image saved as {decrypted_image_path}\n")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
