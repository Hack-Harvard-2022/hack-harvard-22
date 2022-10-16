# hack-harvard-2022

Speech to text language learning app.

## Inspiration
While there are plenty of language-learning apps out there that provide resources to help language-learners learn/practice reading and writing, speaking a new language is a difficult yet incredibly applicable aspect of learning a new language that can often be overlooked by learning resources. Additionally, when considering speaking a new language, we realized there can often a big gap between native and non-native speakers of a language because their use of correct grammar/pronunciation, so we were inspired to create a resource to help bridge this gap.

## What it does
Our program allows users to record their conversations either with others or directly into the program and outputs both the user's speech and a version of their speech that corrects grammar/word choice, allowing them to learn where their grammar went wrong, if at all.

## How we built it
First, we built a voice recorder using Google voice recognition APIs. Then, we created a speech-to-text converter and then created a series of grammar checks that filtered the input text and modifies it into a grammatically correct version of itself. Then, we constructed a GUI that outputs both of these texts and compares them one on top of the other.

## Challenges we ran into
It was difficult to get a combination of grammar checks that were actually effective in correcting grammar. There were also a lot of challenges along the way with combining the different components of the program, installing different packages, and creating the GUI. 

## Accomplishments that we're proud of
We're proud of creating something from scratch with relatively little coding experience, especially in Python. Also, neither of us knew how to create a GUI, so we learned the entire process of creating an interface in the span of a day.

## What we learned
We learned a lot about how to navigate packages in Python, grammar check models, and how to create a GUI. Also, as my (Sabrina) first hackathon, I learned the process of creating a project from start to finish, including brainstorming ideas and layers upon layers of failure and modification.

## What's next for SpeechLearn
Our program has a long way to go, as we want to implement it for all languages, and implement a pronunciation-checker. We also can modify the GUI for a more aesthetic interactive experience, and the final vision would be to create a phone app after combining all of these moving parts.

