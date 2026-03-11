chat-link: https://gemini.google.com/share/e1a0cb89d1f2

# Digital Signature

### 7.1 Digital Signature

=> **Definition**: A **digital signature** is an authentication mechanism that enables the creator of a message to attach a code that acts as a signature.

=> **Core concept**: The signature is formed by taking the **hash of the message** and encrypting that hash with the creator's **private key**.

=> **Requirements**:

1. It must verify the **author** and the **date and time** of the signature.
2. It must **authenticate the contents** at the time of the signature.
3. It must be **verifiable by third parties** to resolve disputes.

=> **Properties**:

- Must be a **bit pattern** depending on the message being signed.
- Must use information **unique to the sender** to prevent forgery and denial.
- **Computationally easy** to produce a signature.
- **Computationally easy** to recognize and verify the signature.
- **Computationally infeasible** to forge (either by creating a new message for an existing signature or a fraudulent signature for a given message).
- Practical to retain a copy in **storage**.

---

### 7.1.1 Arbitrated Digital Signatures

=> **Core concept**: Every signed message from sender A to receiver B goes through an **arbiter BB** (Big Brother) that all parties trust.

=> **Explanation**:

=> **BB** (Arbiter) checks the signature, timestamp, origin, and content to ensure legitimacy.

=> Every user shares a **secret key** with the arbiter.

=> **BB** decrypts the message to verify it comes from A and checks the timestamp to protect against **replay attacks**.

=> B trusts the message because it comes from **BB**, even though B cannot check A's signature directly.

=> In case of a dispute, B shows the signature from **BB**, which **BB** can then decrypt to verify.

---

### 7.1.2 Direct Digital Signature

=> **Definition**: Involves only the communicating parties and is typically based on **public key cryptography**.

=> **Core concept**: The sender encrypts the entire message (or a hash code) with their own **private key**.

=> **Implementation details**:

=> If **confidentiality** is required, the sender further encrypts the result using the **receiver's public key** or a **shared secret key**.

=> In a dispute, receiver B produces the plaintext `P` and the signature `E(KRA, P)`. A judge applies A's public key `KUA` to verify the match.

=> **Weaknesses**:

=> The scheme depends entirely on the **sender's private key (KRA)** remaining secret.

=> If **KRA** is disclosed, anyone can produce the signature, and the "legal" argument of the judge fails.

=> **Attacks**:

1. A sender might claim their **private key** was lost to deny a signature (similar to credit card misuse).
2. An attacker (Eve) could get hold of an **old private key** and sign a document with an **old timestamp**.

---

### 7.1.3 Digital Signature Standard (DSS)

=> **Definition**: The **DSS** makes use of the **Secure Hash Algorithm (SHA)** and presents a technique known as the **Digital Signature Algorithm (DSA)**.

=> **Core concept**: **DSS** is designed specifically for digital signatures and cannot be used for encryption or key exchange.

=> **Explanation**:

=> A **hash function** provides a hash code as input to a **signature function**.

=> A **random number K** is generated for each particular signature to increase security.

=> The signature consists of two components, labeled **s** and **r**.

=> At the receiving end, the hash of the incoming message is generated and input into a **verification function**.

[Fig. 7.1.1 DSS approach]

=> **RSA Approach Comparison**:

=> In the **RSA approach**, the message hash is simply encrypted with the sender's **private key**.

=> The recipient decrypts the signature using the sender's **public key** and compares the resulting hash.

[Fig. 7.1.2 RSA approach]

---

### 7.1.4 Digital Signature Algorithm (DSA)

=> **Core concept**: The algorithm uses three public parameters common to a group of users.

=> **Key Parameters**:

1. **Prime number q**: A **160-bit** prime.
2. **Prime number p**: Between **512 and 1024 bits**, such that `q` divides `(p - 1)`.
3. **g**: Calculated as $h^{(p-1)/q} \mod p$, where `h` is an integer between 1 and `(p - 1)`.

=> **Steps for Key Generation**:

1. User selects a **private key x** (a number from 1 to $q - 1$).
2. User calculates the **public key y** using the formula $y = g^x \mod p$.

=> **Signature Generation (Signing)**:
The signature components **(r, s)** are functions of:

1. Public key components (`p, q, g`).
2. User's **private key (x)**.
3. Hash code of the message `H(M)`.
4. An additional random integer **(K)**.

=> **Verification**:
At the receiving end, the receiver generates a quantity `V` based on the public components, the sender's **public key (y)**, and the hash of the message. If `V` matches the **r** component of the signature, it is validated.

[Fig. 7.1.3 Signing and verifying]

# Digital Certificate and ElGamal

### 7.2 Digital Certificate

=> **Definition**: A **data structure** that securely binds an individual or entity to a **public key** used in cryptographic operations like digital signatures or asymmetric encryption.

=> **Core concept**: It acts as an **electronic ID card** issued by a trusted third party, providing unique identification for an entity across networks.

=> **Key Components**:
A digital certificate consists of:

1. The **public key** of the person being certified.
2. The **Distinguished Name (DN)** (Name and address of the person/organization).
3. The **digital signature** of the Certification Authority (CA).
4. The **issue date**.
5. The **expiry date**.

=> **Operational Details**:

=> To obtain a certificate, an organization applies to a **Certification Authority (CA)**.

=> The **CA** is responsible for validating and ensuring the authenticity of the requesting organization.

=> Recipient nodes must trust the **CA** that issued the certificate. Web browsers, for instance, have a default list of **trusted root keys**.

=> **Role of the Private Key**:
The certificate alone doesn't prove identity; it's the **private key** that prevents misuse. If a private key is stolen, the attacker can pose as the legitimate owner of that certificate.

---

### 7.3 ElGamal

=> **Definition**: A public-key encryption algorithm that serves as an alternative to **RSA**.

=> **Core concept**: While **RSA**'s security is based on the difficulty of **factoring large integers**, **ElGamal**'s security depends on the difficulty of computing **discrete logarithms** in a large prime modulus.

=> **Key Features**:

=> **Advantage**: The same plaintext results in a **different ciphertext** each time it is encrypted (due to the random integer `k`).

=> **Disadvantage**: The **ciphertext** is twice as long as the **plaintext**.

=> **Key Generation**:

1. Select a large **prime number p** (ideally $p-1$ is divisible by another large prime).
2. Compute a **generator number g**.
3. Select a random integer **a** (where $a < p-1$). This is the **secret key**.
4. Compute $b = g^a \pmod p$.
5. The **public key** consists of the triplet **(p, g, b)**.

---

### 7.3.1 Encryption and Decryption

=> **Encryption Process**:
To send message **m** to Alice, Bob performs the following steps:

1. Look up Alice's public key **(p, g, b)**.
2. Select a **random key k** (where $k < p-1$).
3. Compute two numbers:

- $c_1 = g^k \pmod p$
- $c_2 = m \cdot b^k \pmod p$

4. Send the pair **(c1, c2)** to Alice.

=> **Decryption Process**:
Alice receives the ciphertext and uses her **secret key a** to recover the message:

1. Compute $m = c_2 \cdot c_1^{-a} \pmod p$.

=> **Mathematical Proof**:

$$c_2 \cdot c_1^{-a} = (m \cdot b^k) \cdot (g^k)^{-a} = m \cdot (g^a)^k \cdot g^{-ak} = m \cdot g^{ak} \cdot g^{-ak} = m \pmod p$$

---

### 7.3.2 Implementation and Security Notes

=> Bob should choose a **different random integer k** for every message (or block) sent.

=> If the same **k** is used for two different messages ($M_1$ and $M_2$) and an attacker (Eve) discovers $M_1$, she can easily compute $M_2$.

=> **Example Calculation**:

=> If Alice selects $p=11$, $g=7$, and $a=2$:

- Public key $b = 7^2 \pmod{11} = 5$.
- Public key triplet is **(11, 7, 5)**.

=> Bob sends the letter "a" (ASCII 01100001) by breaking it into blocks (e.g., $1, 2, 0, 1$):

- For $m=1$, with $k=3$:
- $c_1 = 7^3 \pmod{11} = 2$
- $c_2 = 1 \cdot 5^3 \pmod{11} = 4$
- Ciphertext pair: **(2, 4)**.

=> **Deciphering**:

- Alice uses $a=2$ on **(2, 4)**:
- $m = 4 \cdot (2)^{-2} \pmod{11}$
- Since $2^2=4$ and the inverse of $4 \pmod{11}$ is $3$:
- $m = 4 \cdot 3 = 12 \pmod{11} = 1$.

# Schnorr Signature and NIST Algorithm

### 7.4 Schnorr Signature

=> **Definition**: The **Schnorr signature** scheme is a digital signature scheme derived from Schnorr's identification protocol using the **Fiat-Shamir heuristic**.

=> **Core concept**: It is related to the **Digital Signature Standard (DSS)** and works within a subgroup of the group $Z^*_p$ for a prime number $p$.

=> **Security**: Its security is analyzed in the **Random Oracle Model (ROM)** under the **Discrete Logarithm (DL)** assumption.

=> **Key Efficiency Advantage**:

=> The scheme minimizes message-dependent computation.

=> The main work for signature generation does not depend on the message and can be performed during the **idle time** of the processor.

=> The message-dependent part only requires multiplying a **2n-bit integer** with an **n-bit integer**.

---

### 7.4.1 Schnorr Key Generation and Signing

=> **Key Generation Steps**:

1. Choose primes **p** and **q**, such that **q** is a prime factor of **p - 1**.
2. Choose an integer **a** such that $a^q = 1 \pmod p$. The values **(a, p, q)** comprise the global public key.
3. Choose a random integer **s** ($0 < s < q$) as the user's **private key**.
4. Calculate the user's **public key**: $v = a^{-s} \pmod p$.

=> **Signature Generation**:

1. Choose a random integer **r** ($0 < r < q$).
2. Compute $x = a^r \pmod p$ (This is independent of the message and can be pre-computed).
3. Concatenate message **M** with **x** and hash the result: $e = H(M \ || \ x)$.
4. Compute $y = (r + se) \pmod q$.
5. The signature consists of the pair **(e, y)**.

=> **Verification Process**:

1. Compute $x' = a^y v^e \pmod p$.
2. Verify that $e = H(M \ || \ x')$.

---

### 7.5 NIST Digital Signature Algorithm

=> **Definition**: A standard specified by the **National Institute of Standards and Technology (NIST)** to ensure the integrity of electronic documents and the identity of the signer.

=> **Core concept**: It is part of the **Federal Information Processing Standard (FIPS) 186-3**, providing a means of guaranteeing authenticity that is nearly impossible to forge.

=> **Algorithm Types**:
NIST specifies three algorithms suitable for digital signature generation and verification:

1. **Digital Signature Algorithm (DSA)**
2. **Rivest-Shamir-Adleman (RSA)**
3. **Elliptic Curve Digital Signature Algorithm (ECDSA)**

=> **Benefits**:

=> Eliminates the need for transmitting **passwords** for authentication, reducing compromise risks.

=> Prevents attackers from **masquerading** as another entity since they lack the private key.

=> Provides security for **e-mail**, **Electronic Funds Transfer (EFT)**, and **software distribution**.

=> Ensures **data integrity** and **data origin authentication**.
