# Worksheet: Binary, Boolean, and How Computers See Everything

DaSean Mitchell | DSDT | 2026

Everything a computer does — every password it checks, every image
it displays, every packet it sends — is binary underneath. This
worksheet builds the intuition for how that works.

---

## PART 1: BINARY — COUNTING WITH TWO DIGITS

Decimal uses ten digits (0–9). Binary uses two (0 and 1).
Same math, different base.

### Place Values

In decimal, places are powers of 10:

    1000  100   10    1
    10³   10²   10¹   10⁰

In binary, places are powers of 2:

    128   64    32    16    8     4     2     1
    2⁷    2⁶    2⁵    2⁴    2³    2²    2¹    2⁰

To convert binary → decimal: add up the place values where there's a 1.

### Worked Example

    Binary:  1 0 1 1 0 1 1 0
    Places: 128 64 32 16  8  4  2  1
    Active: 128  +  32+16  +  4+ 2
    Total:  128 + 32 + 16 + 4 + 2 = 182

So binary 10110110 = decimal 182.

### Exercise 1: Binary → Decimal

Convert these binary numbers to decimal. Show your work.

    128  64  32  16   8   4   2   1

a)  0    0   0   0   1   0   1   0  = ____

b)  0    0   0   0   1   1   1   1  = ____

c)  0    1   0   0   0   0   0   1  = ____

d)  1    0   0   0   0   0   0   0  = ____

e)  1    1   1   1   1   1   1   1  = ____

f)  0    0   1   0   1   0   1   0  = ____

### Exercise 2: Decimal → Binary

Convert these decimal numbers to binary. Fill in the 1s and 0s.

    128  64  32  16   8   4   2   1

a) 25  = ___  ___ ___ ___ ___ ___ ___ ___

b) 100 = ___  ___ ___ ___ ___ ___ ___ ___

c) 7   = ___  ___ ___ ___ ___ ___ ___ ___

d) 200 = ___  ___ ___ ___ ___ ___ ___ ___

e) 255 = ___  ___ ___ ___ ___ ___ ___ ___

f) 1   = ___  ___ ___ ___ ___ ___ ___ ___

**Method**: Start from the left (128). Is 128 ≤ your number? If yes,
write 1 and subtract. If no, write 0. Move right. Repeat.

---

## PART 2: BITS, BYTES, AND WHY THEY MATTER

| Term | What It Is | Example |
|------|-----------|---------|
| **Bit** | A single 0 or 1 | 1 |
| **Nibble** | 4 bits | 1010 |
| **Byte** | 8 bits | 10110110 |
| **Word** | 16, 32, or 64 bits depending on CPU | (varies) |

### Why 8 bits = 1 byte?

8 bits gives you 2⁸ = **256 possible values** (0 through 255).

That's enough to represent:
- Every letter, number, and symbol on a keyboard (ASCII)
- One color channel (0 = black, 255 = full brightness)
- One number in an IP address (each octet is 0–255)

### Exercise 3: Bit Sizes

Fill in the blanks:

a) 1 bit can represent ____ different values (0 or 1)

b) 2 bits can represent ____ different values (00, 01, 10, 11)

c) 4 bits can represent ____ different values

d) 8 bits can represent ____ different values

e) The pattern is: n bits = 2^n values. So 16 bits = ____ values.

f) A computer with a "64-bit processor" means it can handle a number
   up to 2⁶⁴ in one operation. That's ____________________ (big/small/huge?)

### Why This Matters for Cybersecurity

- **Encryption keys** are measured in bits. A 256-bit key has 2²⁵⁶
  possible combinations — more than atoms in the universe.
- **IP addresses** (IPv4) are 32 bits: four groups of 8 bits.
  192.168.1.1 is really: 11000000.10101000.00000001.00000001
- **Subnet masks** are just binary with all the 1s on the left.
  255.255.255.0 = 11111111.11111111.11111111.00000000

---

## PART 3: BOOLEAN LOGIC — TRUE/FALSE DECISIONS

A computer can only ask one kind of question: **is this true or false?**

Everything else — math, search, security, AI — is built by combining
millions of true/false decisions per second.

### The Three Operations

**AND** — Both must be true.

    A AND B = true only if BOTH are true

    | A     | B     | A AND B |
    |-------|-------|---------|
    | false | false | false   |
    | false | true  | false   |
    | true  | false | false   |
    | true  | true  | TRUE    |

Military: "Fire IF target is in range AND you have authorization."
Both conditions must be met.

**OR** — At least one must be true.

    | A     | B     | A OR B  |
    |-------|-------|---------|
    | false | false | false   |
    | false | true  | TRUE    |
    | true  | false | TRUE    |
    | true  | true  | TRUE    |

Military: "Alert IF motion sensor triggers OR perimeter alarm sounds."
Either one is enough.

**NOT** — Flips the value.

    | A     | NOT A |
    |-------|-------|
    | false | TRUE  |
    | true  | false |

Military: "If the radio is NOT working, switch to backup."

### Exercise 4: Boolean Logic

Solve these. Use 1 for true, 0 for false.

a) 1 AND 1 = ____
b) 1 AND 0 = ____
c) 0 OR 1  = ____
d) 0 OR 0  = ____
e) NOT 1   = ____
f) NOT 0   = ____
g) (1 AND 0) OR 1 = ____
h) NOT (1 AND 1)  = ____
i) (1 OR 0) AND (NOT 0) = ____

### Exercise 5: Real-World Boolean

Write the boolean logic for these situations:

a) A firewall rule: "Block traffic IF source is external AND
   destination port is 22 AND the user is NOT on the whitelist."

   Block = external AND port22 AND NOT(__________)

b) An alert triggers: "Send alert IF CPU usage > 90% OR memory
   usage > 95%."

   Alert = __________ OR __________

c) A door lock: "Unlock IF badge is valid AND time is between
   8am–6pm AND door is NOT already unlocked."

   Unlock = __________ AND __________ AND NOT(__________)

---

## PART 4: HEXADECIMAL — BASE 16

Hex is shorthand for binary. Instead of writing 8 binary digits,
you write 2 hex characters.

### The Hex Digits

    Decimal:  0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
    Hex:      0  1  2  3  4  5  6  7  8  9   A   B   C   D   E   F
    Binary:  0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111

Each hex digit = exactly 4 bits (a nibble).
Two hex digits = exactly 8 bits (a byte) = values 0–255.

### Worked Example

    Hex: 4F
    4 = 0100
    F = 1111
    Binary: 01001111
    Decimal: 64 + 8 + 4 + 2 + 1 = 79

    So hex 4F = binary 01001111 = decimal 79

### Exercise 6: Hex Conversions

a) Hex A = decimal ____

b) Hex F = decimal ____

c) Hex FF = decimal ____

d) Hex 10 = decimal ____

e) Hex 00 = decimal ____

f) Decimal 200 = hex ____ (hint: 200 = 12×16 + 8, so C8)

g) Decimal 255 = hex ____

---

## PART 5: HOW A COMPUTER SEES EVERYTHING THE SAME WAY

Here's the big idea: **to the CPU, everything is just bytes.**
A password, a photo, a sound file, a network packet — all binary.
The computer doesn't "know" what the data means. The software
tells it how to interpret the bytes.

### Text (ASCII / UTF-8)

Every character has a number. The number is stored in binary.

    Letter  →  Decimal  →  Binary       →  Hex
    'A'     →  65       →  01000001     →  41
    'B'     →  66       →  01000010     →  42
    'a'     →  97       →  01100001     →  61
    '0'     →  48       →  00110000     →  30
    ' '     →  32       →  00100000     →  20

### Exercise 7: Decode This Message

Using the table above and ASCII (A=65, B=66, ... Z=90):

    72 101 108 108 111

a) Convert each number to a letter:
   72=____ 101=____ 108=____ 108=____ 111=____

b) The message is: _______________

Hint: 72=H, and lowercase letters start at 97 (a=97, b=98...).

### Colors (RGB)

A color on screen = three bytes: Red, Green, Blue. Each 0–255.

    Color      R     G     B     Hex Code
    Black      0     0     0     #000000
    White      255   255   255   #FFFFFF
    Red        255   0     0     #FF0000
    Green      0     255   0     #00FF00
    Blue       0     0     255   #0000FF
    Yellow     255   255   0     #FFFF00

### Exercise 8: Color Codes

a) What color is #FF00FF?
   R=255, G=____, B=____  → Color: ____________

b) What's the hex code for pure green? #__________

c) How many total colors can RGB represent?
   256 × 256 × 256 = ____________

d) Why does hex make sense for colors?
   Each color channel is one byte = two hex digits = ____

### Images

A photo is a grid of pixels. Each pixel is an RGB color (3 bytes).

    A 1920×1080 image = 1920 × 1080 pixels
                      = 2,073,600 pixels
                      × 3 bytes each
                      = 6,220,800 bytes
                      ≈ 6 MB (uncompressed)

That's why JPEG exists — compression shrinks the file by throwing
out data your eyes won't miss.

### Passwords

When you type "Pass123", the computer sees:

    P  a  s  s  1  2  3
    80 97 115 115 49 50 51

Seven bytes. The computer doesn't see a "word" — it sees seven
numbers. A hash function scrambles those numbers into a fixed-length
string that can't be reversed. That's how passwords are stored:
the system never keeps your actual password, just the hash.

### Network Packets

When Swiftgate pings the tasknode:

    Source IP:      192.168.1.50  →  C0.A8.01.32 (hex)
    Destination IP: 192.168.1.99  →  C0.A8.01.63 (hex)
    Protocol:       ICMP          →  01 (hex)

The entire packet is just bytes. Wireshark shows you those bytes
and helps you read them. Every field in the packet has a defined
position and length — that's what a "protocol" is.

### Exercise 9: Everything Is Bytes

a) The letter 'Z' is ASCII 90. In binary: __________
   In hex: ____

b) The IP address 10.0.0.1 in binary:
   10 = __________, 0 = __________, 0 = __________, 1 = __________

c) A 4-character password uses ____ bytes of memory.

d) A hacker captures a packet. They see hex: 48 54 54 50
   What protocol is that? (Hint: convert to ASCII)
   48=____ 54=____ 54=____ 50=____  → ____________

---

## PART 6: WHY MORE BITS = MORE POWER

Every time you add a bit, you DOUBLE the number of possibilities.

| Bits | Possible Values | Real-World Use |
|------|----------------|----------------|
| 1 | 2 | A switch: on/off |
| 4 | 16 | One hex digit |
| 8 | 256 | One ASCII character, one color channel, one IP octet |
| 16 | 65,536 | One port number (0–65535) |
| 32 | ~4.3 billion | IPv4 address space (why we ran out) |
| 64 | ~18.4 quintillion | Modern CPU word size |
| 128 | ~340 undecillion | IPv6 address space (won't run out) |
| 256 | More than atoms in universe | AES-256 encryption key space |

### Exercise 10: Thinking in Powers of 2

a) IPv4 uses 32-bit addresses. That's about 4.3 billion addresses.
   The world has ~8 billion people. Why is that a problem?

b) IPv6 uses 128-bit addresses. Is that enough? Why?

c) An AES-256 encryption key has 2²⁵⁶ possible combinations.
   If a computer could try 1 billion keys per second, how many
   years would it take to try them all?
   (Hint: 2²⁵⁶ ÷ 10⁹ ÷ 60 ÷ 60 ÷ 24 ÷ 365 = a number so large
   the universe will end first. That's why encryption works.)

---

## ANSWER KEY

**Exercise 1**: a) 10, b) 15, c) 65, d) 128, e) 255, f) 42
**Exercise 2**: a) 00011001, b) 01100100, c) 00000111,
d) 11001000, e) 11111111, f) 00000001
**Exercise 3**: a) 2, b) 4, c) 16, d) 256, e) 65536, f) huge
**Exercise 4**: a) 1, b) 0, c) 1, d) 0, e) 0, f) 1,
g) 1, h) 0, i) 1
**Exercise 6**: a) 10, b) 15, c) 255, d) 16, e) 0, f) C8, g) FF
**Exercise 7**: a) H-e-l-l-o, b) "Hello"
**Exercise 8**: a) G=0 B=255 → Magenta/Purple, b) #00FF00,
c) 16,777,216, d) two hex digits per channel = clean notation
**Exercise 9**: a) 01011010, 5A, b) 00001010, 00000000, 00000000,
00000001, c) 4 bytes, d) H-T-T-P → "HTTP"

---

*Print date: ___________*
*Score: ____/10 exercises*

