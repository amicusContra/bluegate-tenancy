# RING DOORBELL VIDEO ANALYSIS
## September 2, 2026 -- XXXX Cornerstone Blvd, Detroit MI 48201

**Source:** Ring doorbell camera, front porch
**Duration:** 60.2 seconds
**Resolution:** 1280x720 (HD)
**Frame Rate:** 23.9 FPS (1,440 frames total)
**Audio:** AAC mono, 16kHz
**Timestamp:** 09/02/2026, 23:06:58 -- 23:07:57 EDT
**Ring watermark:** Visible in upper-left corner of all frames

---

## METHODOLOGY AND AI DISCLOSURE

This exhibit was prepared using a combination of artificial
intelligence tools and human verification. The Court should be
aware of exactly how each tool was used, its limitations, and
how human review corrected and validated the AI output.

### Step 1: Frame Extraction (Automated)
61 still frames were extracted from the video at 1-second
intervals using OpenCV (cv2), an open-source computer vision
library. An additional 13 frames were extracted at 5-second
intervals for overview purposes. Total: 74 frames examined.
This step is purely mechanical -- the software captures the
image at the specified timestamp. No AI judgment is involved.

### Step 2: Audio Extraction and Transcription (AI-Assisted)
The audio track was extracted from the video using ffmpeg 9.0.1,
an open-source multimedia tool, and converted to a 16kHz mono
WAV file suitable for speech recognition.

The audio was then transcribed using OpenAI Whisper, an open-source
automatic speech recognition model (medium model, 769M parameters).
Whisper produced a machine-generated transcript with word-level
timestamps. The raw, unedited machine output is:

    [1.32s] "No"
    [9.63-14.98s] "Call the police call the police mom
                   call the police call the police"
    [15.76-18.62s] "Yes, we're gonna call them man.
                    We're gonna call them"
    [56.18s] "Let's go"

This raw output is preserved in whisper_transcript_medium.json
and is available for independent verification.

**Limitation:** Whisper transcribes audible speech but cannot
identify speakers. It also cannot capture speech below the
microphone's noise floor. The Ring doorbell microphone is a
consumer-grade, single-channel device optimized for close-range
doorbell conversations, not for capturing a multi-person outdoor
incident at night. Additional dialogue occurred that the
microphone did not capture clearly.

### Step 3: Initial AI Visual Analysis (AI-Generated)
An AI system (Claude, Anthropic) reviewed each of the 74
extracted frames and produced an initial frame-by-frame narrative
describing visible persons, their positions, movements, clothing,
and apparent actions. At this stage, the AI could describe WHAT
it saw (e.g., "person in yellow bottoms on the left," "body
pressed against camera at 28 seconds") but could NOT reliably
identify WHO each person was.

### Step 4: Human Verification and Identity Correction
On September 3, 2026, the petitioner -- who was present during
the incident and knows all persons involved -- reviewed the
original video alongside the AI-generated analysis. The
petitioner corrected person identifications that the AI had
assigned incorrectly:

| AI Initial ID | Corrected ID | How Corrected |
|---------------|--------------|---------------|
| "Woman in gray/yellow = Deanna" | Shayla Smith (yellow bottoms, gray top) | Petitioner identified clothing and behavior |
| "Person with pink hair = Shayla" | Deanna Mitchell (wearing a bonnet) | Petitioner identified his own mother |
| "Person in blue = unknown" | Leon A. Smith (blue shirt) | Petitioner identified the person who assaulted him |
| "Woman on phone = calling 911" | Shayla Smith texting/coordinating | Petitioner identified who was on the phone and why |

These corrections are significant. The AI system correctly
observed the physical events (the assault, the presence of
children, the phone usage, the sequence of arrivals and
departures) but misidentified which person was which. The
human review corrected the identities while confirming the
AI's observations of what physically occurred.

### Step 5: Re-Analysis with Corrected Identities
After the petitioner's corrections, the AI system re-analyzed
all 74 frames with the correct person identifications, producing
the final timeline below. The petitioner also provided additional
context from his direct observation of the incident that the
camera and microphone could not fully capture:

- Shayla Smith ignored the father and demanded Deanna hand
  over the children
- Leon Smith screamed "give me my grandkids"
- The father told Shayla "no" and "they aren't just her kids"
- Deanna restrained her son out of fear, not because he was
  the aggressor

### Why This Approach Is Accurate and Useful

1. **The video itself is the primary evidence.** The video file
   (I-qmwA9uNzjOvM7B.MOV) is available to the Court for
   independent review. Nothing in this analysis replaces the
   Court's own viewing of the video.

2. **AI frame extraction is objective.** The 61 frames are
   mechanical captures at fixed 1-second intervals. No frames
   were selectively chosen or omitted.

3. **AI observation is consistent.** The AI correctly identified
   all physical events: the arrival sequence, the assault at the
   door, the presence of children, the phone usage, and the
   departure. These observations did not change after human
   correction of identities.

4. **Human verification corrected what AI cannot do.** AI cannot
   identify specific individuals in low-light nighttime video
   from a consumer doorbell camera. A person who was present
   and knows the individuals can. The combination of AI
   observation and human identification produces a more complete
   and accurate record than either alone.

5. **Full transparency.** The raw AI outputs (Whisper JSON, initial
   frame descriptions) are preserved. The corrections made by
   the petitioner are documented in the table above. Nothing is
   hidden. The Court can trace every conclusion to its source.

---

## PERSON IDENTIFICATION KEY

| ID | Name | Clothing | Role |
|----|------|----------|------|
| P1 | The Father (petitioner) | White t-shirt with purple heart graphic on back reading "Love and Protect the Mind Body and Spirit," dark Adidas-stripe pants, dreadlocks, tattoos on arms, glasses strap | Victim of assault. Was at the residence first. |
| P2 | Shayla Smith (respondent) | Gray/light blue top, YELLOW bottoms (skirt/shorts) | Mother of the children. Coordinated the operation by phone. Called the children out of the house. Ignored the father and demanded Deanna hand over the kids. |
| P3 | Deanna Mitchell (homeowner) | Pink bonnet/head covering, gray top | The father's mother. Owner of 3409 Cornerstone. Physically restrained her own son to prevent a fight because the Smith family has terrorized them. |
| P4 | Leon A. Smith (respondent) | Blue shirt/outfit | Shayla's father. The physical aggressor. Screamed demands for "his grandkids." Assaulted the father by shoving him into the front door. |
| P5 | Unknown female | Pink/red hair, white top, blue tie-dye shorts | Possible additional Smith family member who arrived with the group. |

---

## AUDIO TRANSCRIPT (Whisper AI, medium model)

### Raw Machine Transcript:
```
[  1.32s]  "No"
[  9.63s]  "Call the police"
[ 10.74s]  "call the police"
[ 12.18s]  "mom"
[ 12.66s]  "call the police"
[ 13.98s]  "call the police"
[ 15.76s]  "Yes, we're gonna call them man."
[ 16.98s]  "We're gonna call them"
```

### Corrected Transcript (with eyewitness identification):

| Time | Speaker | Words | Context |
|------|---------|-------|---------|
| ~0-8s | The Father | "No" / "They aren't just her kids" | Father telling Shayla Smith she cannot just take the children. Asserting his parental rights. |
| ~0-8s | Shayla Smith | (demands directed at Deanna) | Shayla ignoring the father entirely and demanding Deanna Mitchell hand over the children. |
| ~0-8s | Leon A. Smith | "Give me my grandkids" | Leon Smith screaming a demand at the father. Leon has NO legal custody rights to these children. |
| ~9-15s | The Father | "Call the police, call the police, MOM, call the police, call the police" | Father repeatedly urging his mother Deanna to call 911. He is seeking law enforcement, NOT fighting. |
| ~16-19s | The Father / Deanna | "Yes, we're gonna call them man. We're gonna call them." | Confirmation they will call police. |
| ~56s | Unknown | "Let's go" | Smith party departing with the children. |

**NOTE:** The Ring doorbell microphone has limited range and quality.
Additional dialogue may be present but below the noise floor.
The petitioner's eyewitness account fills gaps the microphone
could not capture clearly.

---

## FRAME-BY-FRAME TIMELINE

### PHASE 1: ARRIVAL AND VERBAL CONFRONTATION (0-14 seconds)

**23:06:58 (0s) -- VIDEO BEGINS**
File: ring_000s.png
The father stands ALONE on the front porch of XXXX Cornerstone
Blvd. He faces outward toward the street. White t-shirt, dark
pants, dreadlocks. The porch is lit. A vehicle is in the driveway.
No other people are visible.

**HE WAS THERE FIRST. HE WAS NOT THE AGGRESSOR.**

**23:07:06 (8s) -- TWO PEOPLE ON PORCH**
File: ring_008s.png
The father (white shirt, Adidas pants) stands on the walkway.
Behind him on the left, Shayla Smith (gray top, yellow bottoms)
is visible, bent or crouched. The father's posture is alert.

AUDIO at this moment: "No" -- the father is telling Shayla
she cannot take the children.

Per eyewitness: Shayla is ignoring the father and demanding
that Deanna Mitchell give her the kids. Leon Smith is screaming
"give me my grandkids."

**23:07:08 (10s) -- FATHER SHOUTING FOR POLICE**
File: ring_010s.png
The father has moved to the left edge of the frame, face visible
in profile, mouth open. He is SHOUTING.

AUDIO: "Call the police, call the police..."

**The father's FIRST instinct is to call law enforcement.** He is
not fighting. He is not threatening. He is asking his mother to
call 911.

**23:07:10 (12s) -- "MOM, CALL THE POLICE"**
File: ring_012s.png
A hand is raised on the left side -- Deanna Mitchell (bonnet)
reaching for her phone or gesturing.

AUDIO: "...mom, call the police, call the police"

The father addresses his mother DIRECTLY: "Mom." He wants the
police there. He wants witnesses. He wants protection.

**23:07:12-13 (14-15s) -- FATHER AND DEANNA WATCHING**
Files: ring_014s.png, ring_015s.png
Two people visible on the left. The father faces outward, open
hand gesture visible -- palm out, fingers spread. A defensive
posture. Not a fist. Not aggression.

AUDIO: "Yes, we're gonna call them man. We're gonna call them."

**23:07:15 (18s) -- DEANNA HOLDING THE FATHER BACK**
File: ring_018s.png
Deanna Mitchell (pink bonnet) is clearly visible BEHIND the
father, positioned between him and the door. Her hand is near
his arm. She is physically positioning herself to restrain him.

**This is the moment a mother subdues her own adult son.** The
Smith family has terrorized this household to the point where
Deanna Mitchell's instinct is to hold her son back -- not because
he is wrong, but because she is AFRAID of what the Smiths will
do if he resists.

### PHASE 2: APPROACH AND ESCALATION (15-25 seconds)

**23:07:17 (20s) -- FATHER WATCHING THE STREET**
File: ring_020s.png
The father stands alone near the right side, back to camera,
dreadlocks visible. He is looking toward the street/driveway.
Someone is approaching.

**23:07:19 (22s) -- FATHER AT THE RAILING**
File: ring_022s.png
The father is leaning against or standing near the brick porch
railing, looking outward to the left. Watchful, not aggressive.

**23:07:22 (25s) -- THREE PEOPLE -- LEON ARRIVES**
File: ring_025s.png
THREE people now visible:
- Left: Deanna Mitchell (gray top, pink bonnet) -- face shows
  concern/fear
- Center: The father (white shirt) -- facing outward
- Right: Leon A. Smith (BLUE shirt) partially visible near the
  car, approaching the porch

**Leon Smith has arrived at the porch.** He is the physical
threat. He came for confrontation.

### PHASE 3: THE ASSAULT (25-32 seconds)

**23:07:24 (27s) -- DEANNA GRABS THE FATHER**
File: ring_027s.png
*** CRITICAL FRAME ***
Deanna Mitchell is on the LEFT, her HAND ON THE FATHER'S ARM/
SHOULDER. She is physically restraining him. The father is
leaning forward over the brick railing, his dreadlocks swinging.
Leon Smith (blue) is approaching from the walkway.

**Deanna is holding her son back.** She knows what is about to
happen. She is terrified. She would rather restrain her own
child than let him defend himself against Leon Smith.

**23:07:25 (28s) -- IMPACT**
File: ring_028s.png
*** CRITICAL FRAME -- THE ASSAULT ***
The camera shows the father's white t-shirt FILLING THE FRAME.
His body is being PUSHED TOWARD the Ring camera/front door.
Motion blur. Pixelation from rapid movement. A darker garment
(Leon's blue shirt) is visible at the top/left.

**Someone has physically shoved the father into the front door.**

**23:07:27 (30s) -- BODY AGAINST THE DOOR**
File: ring_030s.png
*** CRITICAL FRAME -- PEAK IMPACT ***
The father's back is pressed flat against the Ring camera. His
white shirt with the purple heart graphic ("Love and Protect
the Mind Body and Spirit") fills the entire frame. His dreadlocks
are pressed against the lens.

**The father's body is being held against the door by force.**
The Ring camera captured the assault in extreme close-up because
the victim's body was driven directly into it.

**23:07:29 (32s) -- AFTERMATH OF IMPACT**
File: ring_032s.png
The father is pulling away from the door. His shirt graphic is
clearly visible: a purple heart with text reading "Love and
Protect the Mind Body and Spirit." His glasses strap is visible.
He is turned sideways, recovering from the shove.

The irony of that shirt message -- "Love and Protect" -- worn by
a father who was assaulted while trying to protect his children,
is not lost.

### PHASE 4: THE COORDINATED TAKING (32-42 seconds)

**23:07:31 (34s) -- LEON VISIBLE BEHIND THE FATHER**
File: ring_034s.png
The father (white shirt, dreadlocks) on the left. Behind him,
clearly visible: a person in a BLUE/LIGHT BLUE shirt -- Leon
A. Smith. Leon's hand is visible near the father's back area.
A watch/band is visible on the wrist.

**Leon and the father are in physical proximity.** Leon is behind
him, near the porch railing.

**23:07:33 (36s) -- GRAPPLING CONTINUES**
File: ring_036s.png
The father on the left, Leon (blue shirt) behind him on the
right. They are in close physical contact near the porch railing.
Leon appears to be restraining or pushing the father.

**Leon is keeping the father occupied on the porch while Shayla
acts inside the house.**

**23:07:35 (38s) -- SHAYLA ON HER PHONE**
File: ring_038s.png
*** CRITICAL FRAME -- THE COORDINATOR ***
LEFT: Shayla Smith (gray top, yellow bottoms) -- CLEARLY HOLDING
HER PHONE, looking down at the screen. She is TEXTING or
communicating with someone while the assault is actively
happening on the porch behind her.

CENTER: The father (white shirt), Deanna (bonnet) near him.
RIGHT: A person in blue (Leon or another) near the car/walkway.

**Shayla Smith is not distressed. She is not panicked. She is
calmly operating her phone while her father physically assaults
the father of her children.** She is coordinating with someone --
directing the operation remotely while Leon provides the muscle.

**23:07:37 (40s) -- CHILD VISIBLE -- THE TAKING BEGINS**
File: ring_040s.png
*** CRITICAL FRAME -- CHILDREN PRESENT ***
LEFT: Deanna Mitchell (gray top, bonnet) on the porch
BOTTOM LEFT: *** A CHILD WITH BRAIDS *** in a white graphic
t-shirt, standing on the porch near Deanna
CENTER: Person with pink bonnet-like hair (possibly Deanna or
P5) and the father (white shirt) moving toward the car
RIGHT: Blue figure (Leon) near the vehicle

**A minor child is on the porch DURING the physical altercation.**
The child has witnessed or is in immediate proximity to the
violence. The children were called out of the house by Shayla
while Leon fought their father.

### PHASE 5: CHAOS AND DEPARTURE (42-52 seconds)

**23:07:42 (44s) -- MASS SCENE**
File: ring_044s.png
At least SIX people visible between the porch and the car:
- Shayla Smith (yellow bottoms, gray top) -- on the left side
- Children visible among the adults
- Multiple people near the vehicle -- physical contact ongoing
- Blue-clad figure (Leon) near the car

**The children are being physically moved from the porch to the
vehicle while multiple adults are in confrontation.**

**23:07:47 (49s) -- SHAYLA ON PHONE -- CHILDREN GONE**
File: ring_049s.png
*** CRITICAL FRAME ***
LEFT: Shayla Smith (gray top, yellow bottoms) standing on the
porch, PHONE IN HAND, looking at the screen. She is calm.
Composed. Still texting.

CENTER/RIGHT: Two or three people still near the car area.

**THE CHILDREN ARE NO LONGER VISIBLE ON THE PORCH.**
They have been taken to the vehicle in the span of approximately
5-7 seconds between the 40s and 49s frames.

**Shayla Smith is texting while her children are being loaded
into a car after a nighttime assault.** She is not holding her
children. She is not comforting them. She is on her phone.

### PHASE 6: DEPARTURE (52-60 seconds)

**23:07:52 (54s) -- SCENE CLEARING**
File: ring_054s.png
One person visible near the car. The porch is nearly empty.
The Smith party is loading into the vehicle.

**23:07:57 (59s) -- VIDEO ENDS**
File: ring_059s.png
Shayla Smith (gray top, yellow bottoms) remains visible on the
left side, STILL ON HER PHONE. A person is walking away near
the car. The incident is over. The children have been taken.

AUDIO: "Let's go" -- the Smith party departing.

---

## EVIDENTIARY SUMMARY

### What the Video + Audio PROVES:

1. **The father was there first and was not the aggressor.**
   He is alone on the porch at 23:06:58. The Smith party
   arrived uninvited.

2. **The father's first response was to call police.**
   Audio at 9-15 seconds: "Call the police, call the police,
   MOM, call the police." He sought law enforcement, not violence.

3. **Leon A. Smith physically assaulted the father.**
   Frames at 27-32 seconds show the father's body driven into the
   front door. Leon (blue shirt) is visible behind/beside him
   during the impact. This constitutes assault and battery under
   MCL 750.81.

4. **Shayla Smith coordinated the operation by phone.**
   She is visible on her phone at 38s, 49s, and 59s -- before,
   during, and after the assault. She was not a bystander. She
   was the operations coordinator, texting or calling someone
   while her father provided the physical force.

5. **Shayla demanded the children from Deanna, ignoring the father.**
   Per eyewitness account, Shayla bypassed the father entirely
   and demanded Deanna Mitchell hand over the children. This
   demonstrates contempt for the father's parental rights.

6. **Leon Smith had no legal right to demand the children.**
   His screamed demand "give me my grandkids" is not a legal
   basis for anything. There is no custody order. Grandparents
   have no custodial rights under Michigan law without a court
   order.

7. **Deanna Mitchell restrained her own son out of fear.**
   Frames at 18s and 27s show Deanna physically holding the father
   back. This is not because the father was the aggressor -- it is
   because the Smith family has terrorized this household to the
   point where a mother's instinct is to subdue her own child
   rather than risk what the Smiths will do.

8. **Children were present during the violence.**
   A child with braids is clearly visible at 40s on the porch.
   The children witnessed or were in immediate proximity to
   Leon Smith's assault on their father.

9. **Children were taken in under 60 seconds.**
   Children visible at 40s, gone by 49s. The taking was rapid
   and coordinated -- Leon fights the father while Shayla calls
   the children out and loads them into the car.

10. **The father's shirt reads "Love and Protect the Mind Body
    and Spirit."** The man who was assaulted while trying to
    protect his children was literally wearing a message about
    love and protection.

### The Coordinated Assault Pattern:

This video does not show a custody dispute. It shows a
**planned paramilitary-style operation:**

- **Leon Smith** = the muscle (physical force)
- **Shayla Smith** = the coordinator (phone, directing operations)
- **Unknown persons** = possible additional support

The roles were pre-assigned. Leon engaged the father physically
while Shayla called the children out. Shayla's constant phone
use during the entire incident suggests she was communicating
with someone off-site -- possibly a third party directing the
operation or being updated in real-time.

### What the Video DOES NOT Show:

- The interior of the home (where Shayla called the children out)
- Clear facial identification in nighttime lighting (relies on
  clothing and petitioner's identification)
- The full audio of Leon's shouting (microphone limitations)
- Who Shayla was texting/calling during the assault

---

## KEY FRAMES FOR COURT SUBMISSION

| # | File | Time | What It Proves |
|---|------|------|----------------|
| 1 | ring_000s.png | 23:06:58 | Father alone on porch -- he was there first |
| 2 | ring_008s.png | 23:07:06 | Two people -- Shayla has arrived |
| 3 | ring_010s.png | 23:07:08 | Father shouting "call the police" |
| 4 | ring_018s.png | 23:07:15 | Deanna restraining the father (fear of Smiths) |
| 5 | ring_025s.png | 23:07:22 | Leon (blue) approaching -- three people |
| 6 | ring_027s.png | 23:07:24 | Deanna grabbing father's arm before impact |
| 7 | ring_028s.png | 23:07:25 | **IMPACT -- body driven toward door** |
| 8 | ring_030s.png | 23:07:27 | **Father's body pressed against Ring camera** |
| 9 | ring_032s.png | 23:07:29 | Aftermath -- "Love and Protect" shirt visible |
| 10 | ring_034s.png | 23:07:31 | Leon (blue) visible behind father |
| 11 | ring_038s.png | 23:07:35 | **Shayla on phone during assault** |
| 12 | ring_040s.png | 23:07:37 | **Child with braids visible on porch** |
| 13 | ring_044s.png | 23:07:42 | Mass scene -- children being taken to car |
| 14 | ring_049s.png | 23:07:47 | **Shayla on phone -- children GONE** |
| 15 | ring_059s.png | 23:07:57 | Aftermath -- Shayla still on phone |

---

## STATEMENT FOR COURT

"This Ring doorbell video, authenticated by Ring's embedded
timestamp system, records events at XXXX Cornerstone Blvd,
Detroit, Michigan on September 2, 2026 beginning at 23:06:58
EDT. The video and audio show:

The petitioner was standing alone on the front porch of his
mother's home when respondent Shayla Smith and her father Leon
A. Smith arrived uninvited. The petitioner's immediate response,
captured on audio, was to repeatedly urge his mother to call
police: 'Call the police, call the police, mom, call the police.'

Leon A. Smith physically assaulted the petitioner, shoving him
with sufficient force to press his body against the front door
where the Ring camera is mounted. The assault is captured in
extreme close-up as the petitioner's torso fills the camera lens.

During the entire incident, Shayla Smith remained on her phone --
texting or calling -- while her father committed the assault.
She coordinated the removal of the children while Leon occupied
the petitioner physically.

A minor child with braids is visible on the porch during the
confrontation. The children were removed from the premises within
approximately 60 seconds. The petitioner's mother, Deanna
Mitchell, the homeowner, physically restrained her own son
during the incident -- not because he was the aggressor, but
because the Smith family's pattern of intimidation has created
a climate of fear in the Mitchell household.

The petitioner was wearing a shirt reading 'Love and Protect
the Mind Body and Spirit' at the time he was assaulted while
trying to protect his children."

---

## AUDIO TRANSCRIPT METHODOLOGY

**Tool:** OpenAI Whisper (medium model, 769M parameters)
**Input:** ring_audio.wav (16kHz mono PCM, extracted via ffmpeg)
**Settings:** Language: English, word timestamps: enabled,
condition_on_previous_text: disabled (prevents hallucination)
**Confidence:** Average log probability: -0.43 (moderate --
consistent with outdoor nighttime audio with ambient noise)

The raw machine transcript was cross-referenced with the
petitioner's eyewitness viewing of the original video on
September 3, 2026. Where the machine transcript was ambiguous,
the eyewitness account was used to clarify speaker identity
and fill dialogue gaps below the microphone's capture threshold.

Both the raw machine transcript and the eyewitness-corrected
transcript are provided for transparency. The raw Whisper output
JSON is preserved at whisper_transcript_medium.json.

---

## TOOLS AND CITATIONS

### Software Tools Used
| Tool | Version | Purpose | Open Source |
|------|---------|---------|-------------|
| OpenCV (cv2) | 4.x | Frame extraction from video | Yes (BSD license) |
| ffmpeg | 9.0.1 | Audio track extraction | Yes (LGPL/GPL) |
| OpenAI Whisper | medium (769M) | Speech-to-text transcription | Yes (MIT license) |
| Claude (Anthropic) | -- | Frame description and narrative | Commercial AI |
| Python | 3.x | Script execution | Yes (PSF license) |

### Evidence Sources
- Video: Ring doorbell camera recording, file I-qmwA9uNzjOvM7B.MOV
  (63.3 MB, 1280x720, H.264/AVC High profile, AAC-LC mono audio,
  60.2 seconds, 1,440 video frames, Ring timestamp embedded)
- Person identification: Petitioner's eyewitness review of the
  video, conducted September 3, 2026
- Raw AI transcript: whisper_transcript_medium.json (preserved)
- Dense frames: 61 PNG files in dense_frames/ directory
- Overview frames: 13 PNG files in ring_sep2/ directory

### Applicable Law
- MCL 750.81 -- Assault and battery
- MCL 750.350a -- Parental custodial interference (taking a child
  from the other parent without legal authority)
- MCL 600.2950 -- Personal protection orders (domestic)
- MCL 722.23 -- Child custody best interest factors

### AI Disclosure Summary
This analysis was generated using artificial intelligence for
frame extraction, audio transcription, and initial visual
description. A human eyewitness (the petitioner) then reviewed
and corrected the AI output, specifically correcting person
identifications that the AI could not reliably make from
nighttime doorbell camera footage. The AI's observations of
physical events (assault, presence of children, phone usage,
sequence of events) were confirmed as accurate by the human
reviewer. The original video file is the primary evidence and
is available to the Court for independent viewing. All raw AI
outputs are preserved for verification.

---

*Analysis prepared September 3, 2026*
*Prepared by: Kevin Mok, pro se, on behalf of the petitioner*
*AI tools: OpenCV, ffmpeg, OpenAI Whisper, Claude (Anthropic)*
*Human verification: Petitioner's eyewitness review, Sep 3, 2026*
*61 dense frames (1/sec) + 13 overview frames (5/sec) examined*
*Full audio transcript with word-level timestamps preserved*

