# **Data Encryption Methods**

The program implements three encryption methods:
- XOR encryption
- Caesar cipher
- Vigenère cipher

These ciphers were chosen because they are fundamental to the study of cryptography. They are also simple to learn, yet reasonably secure when used correctly.

---

### **XOR Encryption**

**XOR cipher** (**XOR encryption**) is a cipher based on the logical operation **OR-NOT** (exclusive disjunction, XOR).

The essence of the cipher is to convert each character of the plaintext and key into a binary numeric value and perform the XOR operation between them.

This operation is performed for each character of the plaintext, after which the result is converted to the decimal number system. To encode a character into a numeric value and vice versa, you can use the ASCII standard, UNICODE (used in Valgrind), or a custom character alphabet.

To decrypt the text, you must reverse the operation with the key used to encrypt the original text.

---

### **Caesar Cipher**

The **Shift Cipher** (**Caesar Cipher**) is a cipher based on shifting characters through the alphabet by a fixed value.

The essence of the cipher is to change each character of the plaintext by shifting it right or left through the alphabet by a fixed value—the key.

For a **right** alphabetical shift, the key must be a **positive** number, and for a **left** alphabetical shift, the key must be a **negative** number.

To decrypt, a reverse alphabetical shift is required, i.e., applying a Caesar cipher to the ciphertext, reversing the key sign.

---

### **Vigenère Cipher**

**The Vigenère Cipher** is a cipher based on shifting symbols through the alphabet by a variable value.

The Vigenère cipher is a modified Caesar cipher, but with a variable shift value that changes from symbol to symbol. Encryption is performed using the following algorithm:

1. The codeword is written cyclically to match the length of the plaintext.

2. A plaintext symbol and its corresponding keyword symbol are selected.

3. The plaintext symbol is shifted through the alphabet by a specific value—the position of the corresponding keyword symbol in the alphabet.

In this way, each plaintext symbol is encrypted. Variability of the shift is achieved by choosing a keyword with a minimum number of repeating characters. Decryption is similar to decrypting a Caesar cipher.

---
```
© Project work: "Cryptographic Data Protection Tools"
```