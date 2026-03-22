# **Data encryption in the "Valgrind" program**

```
Warning! This program was created as part of my graduation project. It is not allowed to use it in real conditions to encrypt really important information.
```

### **Data Encryption**

Encryption Algorithm:
1. In the main menu, select the encryption mode (button on the left).

2. Enter the data to be encrypted.

3. Select the encryption method from the drop-down list.

4. Enter the key twice.

5. Confirm the encryption and receive the result.

```
The result is:
- Ciphertext.
- Checksum calculated by hashing the ciphertext and the key.
```

This data must be transmitted to the recipient.

### **Data Decryption**

Decryption Algorithm:
1. In the main menu, select the decryption mode (button on the right).

2. Enter the data to be decrypted.

3. Select the decryption method from the drop-down list.

4. Enter the key and checksum.

5. Confirm decryption and obtain the result.

```
The results are:
- Decrypted text.
- Checksum comparison result:
If the checksums match, the data is intact and usable.
If the checksums do not match, the data is not usable.
```