# Cricket Applications
Umpiring and Scoring

# Use Langchain for RAG
Input sources to be used for the laws:
1. Laws of Cricket 2022 - latest edition
2. Interpretation of the laws - Tom Smith old 2019 edition
3. Changes to the laws from 2019 to 2022 - to aid interpretation of changed laws
4. Interpretations of specific scenarios compiled from MCC articles

Input sources for playing conditions:
1. ICC playing conditions for different game formats and gender-specific conditions
2. Any other playing conditions for local leagues

The framework is to set up three vector databases:
1. For the law document alone (the 2022 version)
2. For interpretation of the laws (Tom Smith's and other sources)
3. For the playing condtions alone

Agentic RAG to be performed based on the query to source results from the laws and the playing conditions, collating the results. Possibly a single vector database holding all of them may be sufficient and would be the first one to test.

Implements the basic RAG approach only. More refinement and chat features to be added...
The basic implementation can be found in Lang_RAG.ipynb notebook.
