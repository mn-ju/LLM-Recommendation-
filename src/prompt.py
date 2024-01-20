condense_question_prompt_template = """Given the following chat history and a follow up question, rephrase the follow up input question to be a standalone question.
Or end the conversation if it seems like it's done.

Chat History:\"""
{chat_history}
\"""

Follow Up Input: \"""
{question}
\"""

Standalone question:"""



qa_prompt_template = """ 
You have access to a vectorbase containing information about various retail products. The vectorbase includes the following variables for each product:

- Name 
- SKU 
- MPN 
- Price 
- In-Stock Status 
- Currency
- Brand 
- Description
- Images Urls
- Gender 

{context}

Based on the information in the vectorbase, I need your assistance in recommending products that match specific criteria. Please follow these steps carefully:


Step 1: Shortlist Products
- Find products that match the question's description.
- Shortlist at least 10 products with unique SKUs.

Step 2: Score and Rank
- Evaluate products based on how well they fit the criteria.
- Rank the products based on their scores.

Step 3: Select the Top 5 Products
- Choose the top 5 products with the highest scores.

Format for a helpful answer:
```
List of Recommended Products:

1. Product Name 1
* Price: [Price 1]
* Brand: [brand 1]
* In-Stock Status: [In-Stock Status 1]
* Currency: [Currency 1]
* Description: [Description 1]
* Gender: [gender 1]
* Image Url: [images 1]
* Reason for Recommendation: [Reasons should be in bullet points]
So on

Please recommend at least 5 products with their only one images url present in the given context.
Ensure that you recommend products based only on the data available in the context
It's important not to generate additional products on your own.

If the question is unrelated to product recommendations, please answer it based on the provided context

Standalone questions (for further clarification):
[List down at least 3-5 standalone questions]
```
helpful answer:
"""



# """Given the following chat history and a follow up question, rephrase the follow up input question to be a standalone question.
# Or end the conversation if it seems like it's done.

# Chat History:\"""
# {chat_history}
# \"""

# Follow Up Input: \"""
# {question}
# \"""

# Standalone question:"""



# qa_prompt_template = """ 
# You have access to a vectorbase containing information about various retail products. The vectorbase includes the following variables for each product:

# - Name 
# - SKU 
# - MPN 
# - Price 
# - In-Stock Status 
# - Currency
# - Brand 
# - Description
# - Images Urls
# - Gender 

# {context}

# Based on the information in the vectorbase, I need your assistance in recommending products that match specific criteria. Please follow these steps carefully:

# Step 1: Shortlist Products
# - Search the vectorbase for products that closely match the description provided in the input question
# - Shortlist at least 10 products, ensuring that each product has a unique SKU (Stock Keeping Unit) that you can find in the CSV context
# - Gather comprehensive details about the shortlisted products, including their name, SKU, MPN (Manufacturer Part Number), price, in-stock status, currency, brand, description, images, and gender

# Step 2: Score Each Product
# - Assign a score to each shortlisted product based on how well it aligns with the criteria mentioned in the input question
# - Take into account the context of the question and how closely each product matches the question's criteria and intent
# - Give higher scores to products that are the best fit for the question's intent

# Step 3: Rank the Products
# - Rank all shortlisted products based on the scores determined in Step 2
# - Ensure that the product with the highest score receives the top rank, followed by others in descending order

# Step 4: Select the Top 5 Products
# - Choose the top 5 products with the highest scores and ranks from Step 3
# - These are the products you should recommend to the shopper as they best match their criteria

# Format for a helpful answer:

# List of Recommended Products:

# 1. Product Name 1
# * Price: [Price 1]
# * Brand: [brand 1]
# * In-Stock Status: [In-Stock Status 1]
# * Currency: [Currency 1]
# * Description: [Description 1]
# * Gender: [gender 1]
# * Image Url: [images 1]
# * Reason for Recommendation: [Reasons should be in bullet points]

# 2. Product Name 2
# * Price: [Price 2]
# * Brand: [brand 2]
# * In-Stock Status: [In-Stock Status 2]
# * Currency: [Currency 2]
# * Description: [Description 2]
# * Gender: [gender 2]
# * Image Url: [images 2]
# * Reason for Recommendation: [Reasons should be in bullet points]
# So on

# You must recommend strictly at least 5 products with their images url present in the given context.
# Please note that you have to share data availabe in context only.

# Standalone questions (for further clarification):
# [List down at least 3-5 standalone questions]

# helpful answer:
# """

