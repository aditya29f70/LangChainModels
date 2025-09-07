from langchain_core.prompts import PromptTemplate


p_template= """
please summarize the reasearch Paper titled "{paper_input}" with the following
specifications:
Explanation Style: {style_input}
Explanation length: {lenght_input}
1. Mathematical Details:
  - Include relevent mathematical equation if present in the paper.
  - Explain the mathematical concepts using simple, intuitive code snippets
2. Analogies:
  - Use relatable analogies to simplify complex ideas,
if certain information is not available in the paper, respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""



template= PromptTemplate(
  template= p_template,
  input_variables=['paper_input', 'style_input', 'lenght_input'],
  validate_template=True
)

# now try to save this template
# by using template.save('file_name')
template.save('template.json')
# for saving you have to run this file once

