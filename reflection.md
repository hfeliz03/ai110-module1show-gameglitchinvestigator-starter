# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looks fine now. This screen is just GameGlitch Investigator. Developer, debug info, submit guest, new game. We can click show or not show hint, so everything looks good from the beginning. Once we start clicking buttons, it's when we start realizing that some things are off. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1- I only Get Hinted to go lower, never higher even when It should hint me to go higher. (On normal difficulty, at least)
2- On hard mode the hint is backwards
3- The score simply looks like a mess I can't predict what happens, it just adds -5 majority of the time.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It showed me that the hard mode was not utilizing its intended range, but the normal mode's range
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
NA
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tried it on the browser and then performed unittesting
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.  
  I ran a manual test where I intentionally guessed numbers higher and lower than the secret number to verify if the hints were accurate. This test showed that the hint logic was flawed, especially in hard mode, where the hints were reversed.

- Did AI help you design or understand any tests? How?  
  Yes, AI suggested creating a test to verify the range logic for hard mode. It helped me understand that the issue was due to the hard mode using the normal mode's range, which I confirmed by running the test.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
