\# Claude AI Guidance File



This file documents how Claude was used during the development of this project,

and the constraints/standards applied to AI-generated code.



\## How AI Was Used



Claude (claude.ai) assisted with the following during this project:



\- \*\*Debugging\*\*: Diagnosing environment variable issues (`REACT\_APP\_BACKEND\_URL` returning `undefined`)

\- \*\*Error analysis\*\*: Reading browser console errors and Flask server logs to identify 400 validation failures
                                                                                                                                                                                             

\## Constraints Applied to AI Output



All AI-generated code and suggestions were held to the following standards:



1\. \*\*No blind copy-paste\*\* — every suggestion was read and understood before use

2\. \*\*No AI-generated secrets or credentials\*\* — environment config was set manually

3\. \*\*Validation logic was not weakened\*\* — AI was not allowed to suggest bypassing ISBN or field validation

4\. \*\*Existing architecture was preserved\*\* — AI suggestions followed the existing separation of concerns (routes, models, validators)



\## What Was NOT AI-Generated



\- Core application logic (`server.py`, `database.py`, `validators.py`)

\- Database schema and model relationships

\- API route design and HTTP method choices

\- Business rules (ISBN validation, borrow/return state management)



\## Prompting Approach



Prompts were kept specific and diagnostic rather than open-ended. For example:

\- Bad: "Fix my app"

\- Good: "The backend returns 400 when I POST to /api/books — here is the validator code, what rule is failing?"



This kept AI assistance targeted and ensured the developer retained full understanding of the system.

