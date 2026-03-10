# **Symmetric Key Cryptography: Block Ciphers and Operations**

## **1. Cryptographic Fundamentals**

### **1.1. Core Encryption and Decryption Concepts**

=> **Definition**: `Cryptography involves securing information by transforming Plaintext into unreadable Ciphertext using specific mathematical algorithms.`

=> `Encryption`: In symmetric operations, the ciphertext ($C_i$) is mathematically generated, often by XORing ($\oplus$) the plaintext ($P_i$ or $m$) with a specific **Key stream** ($K_i$), denoted as: $$C_i = P_i \oplus K_i$$
=> `Decryption`: The original plaintext is retrieved by reversing the operation, typically by XORing the ciphertext back with the identical key stream $C_i = P_i \oplus K_i$

=> `Security goal`: To maintain data confidentiality by ensuring that only parties possessing the correct sequence of keys ($K_1, K_2, K_3...$) can decrypt the **Ciphertext** back into **Plaintext**.

![Block diagram of basic Encryption and Decryption using XOR]

## **2. Simplified Data Encryption Standard (S-DES)**

### **2.1. Core Concept and Architecture**

=> **Definition**: `Simplified DES (S-DES) is a smaller-scale educational version of the DES algorithm designed to illustrate core cryptographic principles using reduced bit sizes.`

=> `Key components`: The algorithm typically takes an 8-bit plaintext block and utilizes a 10-bit master key ($k_1$ to $k_{10}$).

=> `Working mechanism`: It relies on a combination of permutations and a complex function (`fK`), applied over multiple rounds using subkeys `K1` and `K2`.

### **2.2. S-DES Key Generation Process**

=> `Security objective`: To produce two unique subkeys (`K1` and `K2`) from a single 10-bit master key for use in the encryption rounds.

#### Key Generation Process:

1. **Initial Permutation**: The 10-bit master key undergoes a permutation to rearrange its bits.
2. **Splitting**: The permuted 10-bit key is split into two 5-bit halves.
3. **Left Shift 1 (LS1)**: Both halves undergo a 1-bit circular left shift.
4. **Subkey 1 Selection**: The shifted bits are combined and subjected to a second permutation to extract the first subkey (`K1`).
5. **Left Shift 2 (LS2)**: The output halves from `LS1` undergo a 2-bit circular left shift.
6. **Subkey 2 Selection**: A final permutation is applied to these shifted halves to produce the second subkey (`K2`).

### **2.3. S-DES Encryption Process**

=> Important properties: S-DES encryption relies on splitting data and passing it through substitution boxes (S-boxes) S1 and S2, which map 4-bit inputs to 2-bit outputs based on row and column lookups.

Encryption Process:

1. **Initial Permutation (IP)**: The 8-bit plaintext undergoes an initial rearrangement.
2. **Function fK1**: The right half of the permuted data is mathematically combined with subkey `K1` and passed through S-boxes, then XORed with the left half.
3. **Swap**: The left and right halves of the data are swapped.
4. **Function fK2**: The new right half is combined with subkey `K2`, processed through S-boxes, and XORed with the new left half.
5. **Inverse Initial Permutation**: The final combined 8-bit block undergoes the inverse of the initial permutation (`IP^-1`) to produce the ciphertext.

## **3. Data Encryption Standard (DES)**

### **3.1. Core Concept and Structure**

=> **Definition**: `DES` is a widely studied symmetric-key block cipher that encrypts 64-bit plaintext blocks into 64-bit ciphertext blocks using a 56-bit functional key.

=> `DES` is built on a **Feistel network** architecture, wherein the data block is split into a left half ($L_0$) and a right half ($R_0$), undergoing continuous substitutions and permutations over $n$ rounds.

=> Important properties: The mathematical transformation in each round is defined by $$L_i = R_{i-1}$$ $$R_i = L_{i-1} \oplus f(R_{i-1}, K_i)$$ meaning the left half becomes the previous right half, and the new right half is the XOR result of the old left half and the round function.

![Block diagram of a Feistel Network Round]

### **3.2. DES Key Generation Process**

=> `Working mechanism`: `DES` expands a single 64-bit master key into sixteen distinct 48-bit round keys ($K_1$ through $K_{16}$).

Key Generation Process:

1. **Permuted Choice 1**: Selects 56 active bits from the 64-bit master key, discarding the 8 parity bits.
2. **Division**: The 56-bit key is divided into two 28-bit halves, $C_0$ and $D_0$.
3. **Left Shifts**: In each of the 16 rounds, both 28-bit halves undergo a 1-bit or 2-bit circular left shift.
4. **Permuted Choice 2**: The shifted 56-bit key is compressed and permuted to select a 48-bit subkey for the current round.

### **3.3. DES Encryption Process**

=> Security objective: To thoroughly confuse and diffuse the 64-bit plaintext bits over 16 rounds of complex mathematical manipulation.

Encryption Process:

1. **Initial Permutation**: The 64-bit plaintext is rearranged according to a fixed permutation table.
2. **Splitting**: The data is split into 32-bit left ($L_i$) and right ($R_i$) halves.
3. **Expansion Permutation**: The 32-bit right half is expanded into 48 bits.
4. **Key Mixing**: The 48-bit right half is XORed with the 48-bit round key ($K_i$).
5. **Substitution (S-boxes)**: The 48-bit result is divided into 6-bit chunks and passed through eight S-boxes (`S1` to `S8`). Each S-box uses a 4-bit column number and a 2-bit row number to map the 6 bits back down to 4 bits.
6. **Permutation (P)**: The substituted 32-bit output undergoes a final fixed permutation.
7. **Round Combination**: The permuted right half is XORed with the original left half to form the new right half.
8. **Final Swap and Inverse Permutation**: After 16 rounds, a 32-bit swap occurs, followed by an inverse initial permutation to generate the 64-bit ciphertext.

![DES Complete 16-Round Encryption Architecture]

## **4. Advanced Encryption Standard (AES)**

### **4.1. Core Concept and Architecture**

=> **Definition**: `AES` is a robust symmetric block cipher that processes data in a 4x4 matrix of bytes (called the state), replacing the older `DES` standard.

=> **Core concept**: Unlike the Feistel structure of DES, AES uses a substitution-permutation network applying operations across entire blocks of data simultaneously.

=> Key usage: Operations are organized into multiple rounds (e.g., 10 rounds for a 128-bit key), transforming an initial matrix of plaintext bytes into an equally sized matrix of ciphertext bytes.

![AES Overall Architecture and State Matrix]

### **4.2. AES Encryption Process**

=> `Working mechanism`: The encryption process manipulates the byte matrix through a highly structured series of diffusion and confusion transformations applied sequentially in each round.

Encryption Process:

1. **Initial Key Addition**: The initial state matrix is XORed with the first portion of the expanded key (`Add round key`).
2. **Substitute bytes**: Every byte in the state matrix is replaced with a different byte using a non-linear substitution table (S-box).
3. **Shift rows**: The rows of the matrix undergo cyclic shifts to the left (e.g., the second row shifts 1 byte, the third row 2 bytes, etc.).
4. **Mix columns**: Each column in the matrix is mathematically transformed and mixed to provide high diffusion.
5. **Add round key**: A 128-bit round key is XORed with the newly mixed state matrix.
6. **Final Round**: In the 10th and final round, the `Mix columns` step is explicitly omitted.

### **4.3. AES Decryption Process**

=> `Decryption`: The ciphertext is transformed back into plaintext by applying the exact inverse mathematical functions of the encryption process, applied in reverse order.

Decryption Process:

1. **Initial Add round key**: The ciphertext matrix is XORed with the final round key.
2. **Inverse shift rows**: The rows are cyclically shifted to the right to undo the left shifts.
3. **Inverse substitute bytes**: Every byte is passed through an inverse S-box to retrieve the original pre-substitution byte.
4. **Add round key**: The state is XORed with the corresponding round key from the key schedule.
5. **Inverse mix columns**: An inverse mathematical transformation is applied to un-mix the columns (Note: omitted in the final decryption round).

![AES Round Structure for Encryption and Decryption]
