# **Advanced Caesar Cipher with DES-like Rounds**  

## **Introduction**  
This project implements an advanced version of the **Caesar Cipher** combined with **modern cryptographic techniques**. Unlike the traditional Caesar Cipher, which uses a fixed shift value, this encryption system introduces **16 rounds** of transformation, enhancing security while maintaining simplicity.  

## **Features**  
🔹 **16-Round Encryption Process** – Instead of a single shift, the encryption is applied multiple times with unique transformations per round.  
🔹 **Dynamic Key Scheduling** – The shift values change dynamically for each round, making brute-force attacks significantly harder.  
🔹 **XOR-Based Mixing** – A key-mixing step adds additional security, making the output unpredictable.  
🔹 **Block-Based Processing** – Instead of encrypting single characters, the algorithm processes text in structured blocks.  
🔹 **Permutation and Diffusion Techniques** – Inspired by modern cryptographic techniques to strengthen the encryption.  
🔹 **Fully Reversible Decryption** – The encrypted data can be perfectly decrypted using the correct key.  

## **Usage**  
### **Prerequisites**  
Ensure you have Python installed on your system. This project runs on **Python 3+**.  

### **Installation**  
Clone the repository:  
```bash
git clone https://github.com/safi-ullah-031/Advanced-Caesar-Cipher.git  
cd Advanced-Caesar-Cipher
```
Run the encryption script:  
```bash
python encrypt.py
```
Run the decryption script:  
```bash
python decrypt.py
```

## **Input and Output**  
- **Encryption**: The program takes a plaintext message and a key as input and returns an encrypted ciphertext.  
- **Decryption**: The program takes the ciphertext and key to reconstruct the original message.  

## **License**  
This project is open-source and available under the GNU License.  

