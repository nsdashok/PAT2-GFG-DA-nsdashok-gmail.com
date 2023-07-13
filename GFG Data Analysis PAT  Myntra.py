#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.head()


# In[2]:


df.head(15)


# In[3]:


df.shape


# In[4]:


df.isnull()


# In[21]:


df.describe()


# In[24]:


df.tail()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 1. How many unique products are there in the dataset? (5 marks)
# You need to find product ID of each product from product_link and then find the number of unique product ids
# 
# Finding Unique Products as per their Product ID
# Removing Products with Duplicate Product ID

# In[5]:


df['product_id'] = df['product_link'].str.split('/').str[-1]
unique_products = df['product_id'].nunique()
print("Number of unique products:  ", unique_products)


# The second question, which is about removing products with duplicate product IDs, becomes relevant when we have multiple instances of the same product ID in our dataset. This step ensures that i only have one instance of each product in my analysis, eliminating any duplicates.
# 
# Since i have determined that there is only one unique product in my dataset, i can skip the step of removing duplicates.

# ### 2. What is the average rating of the products? (2 mark)
# Try it without the product that are having rating 0
# 
# Try it without the product that are having 0 people given any rating

# In[6]:


# Filter out products with rating 0
filtered_data = df[df['rating'] != 0]
average_rating = filtered_data['rating'].mean()
print("Average rating:- (excluding products with rating 0):", average_rating)


# In[7]:


# Filter out products with 0 people given any rating
filtered_data = df[df['rating_count'] != 0]
average_rating = filtered_data['rating'].mean()
print("Average rating:- (excluding products with 0 people rating count):", average_rating)


# ### 3. What is the average discount percentage of the products?

# In[25]:


# Calculate the average discount percentage
average_discount_percent = df['discount_percent'].mean()
print("Average discount percentage of the products:", average_discount_percent)


# ### 4. What are the top 5 most expensive products?

# In[26]:


# Sort the data by discounted price in descending order becouse i need top 
sorted_data = df.sort_values(by=['discounted_price'], ascending=False)
top_5_expensive_products = sorted_data.head(5)
print("Top 5 most expensive products:")
print('------------------------------------------------------------------------')
print(top_5_expensive_products[['product_name', 'brand_name', 'discounted_price']])


# ### 5. What are the top 10 brands by the number of products in the dataset?

# In[28]:


# Group the data by brand_name and count the number of products
brand_counts = df['brand_name'].value_counts()
top_10_brands = brand_counts.head(10)
print("Top 10 brands by number of products:")
print(" -Brand-            -No. of Product-")
print(top_10_brands)


# ### 6. List top 5 brands with maxiumum average rating of products?
# Neglect the products which are not reviewed by any person

# In[29]:


# Filter out products with 0 rating count, i have excluding products that have not been reviewed by anyone 
filtered_data = df[df['rating_count'] != 0]
brand_avg_rating = filtered_data.groupby('brand_name')['rating'].mean()
sorted_avg_ratings = brand_avg_rating.sort_values(ascending=False)
top_5_brands = sorted_avg_ratings.head(5)
print("Top 5 brands with the highest average rating:")
print(top_5_brands)


# ### 7. Plot a histogram of the distribution of ratings of following brand.
# H&M
# 
# max
# 
# Puma
# 
# MANGO
# 
# Neglect the products which are not reviewed by any person

# In[30]:


# Filter out products with 0 rating count
filtered_data = df[df['rating_count'] != 0]
brands_of_interest = ['H&M', 'Max', 'Puma', 'MANGO']
brand_data = filtered_data[filtered_data['brand_name'].isin(brands_of_interest)]

# Create a histogram of the ratings distribution for each brand
for brand in brands_of_interest:
    brand_ratings = brand_data[brand_data['brand_name'] == brand]['rating']
    plt.hist(brand_ratings, bins=10, alpha=0.5, label=brand)

# Adding labels and a legend to the plot for beautifying the graph
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Ratings for H&M, max, Puma, MANGO Brands')
plt.legend()
plt.show()


# ### 8. What is the distribution of discounts by brand for specific brands mentioned below?
# H&M
# 
# max
# 
# Puma
# 
# MANGO
# 
# Neglect the products which are not reviewed by any person. Neglect the products which are not on any discount.

# In[ ]:





# In[31]:


# Filter out products with 0 rating count and products with no discount
filtered_data = df[(df['rating_count'] != 0) & (df['discount_percent'] != 0)]
brands_of_interest = ['H&M', 'Max', 'Puma', 'MANGO']
brand_data = filtered_data[filtered_data['brand_name'].isin(brands_of_interest)]
brand_avg_discount = brand_data.groupby('brand_name')['discount_percent'].mean()
brand_avg_discount.plot(kind='bar', figsize=(8, 6))
plt.xlabel('Brand')
plt.ylabel('Average Discount Percentage')
plt.title('Distribution of Discounts by Brand')
plt.xticks(rotation=45)
plt.show()


# ### 9. Is there any trend or pattern you can find between discount percent and rating of the product? 

# In[32]:


# Filter out products with 0 rating count and products with no discount
filtered_data = df[(df['rating_count'] != 0) & (df['discount_percent'] != 0)]
plt.scatter(filtered_data['discount_percent'], filtered_data['rating'])
plt.xlabel('Discount Percentage')
plt.ylabel('Rating')
plt.title('Discount Percentage vs. Rating')
plt.show()


# #### higher ratings associated with higher discount percentages

# ### 10. What are the top 10 most popular tags in the dataset?

# In[33]:


# Split the product tags into individual tags
tags = df['product_tag'].str.split(',')
flat_tags = [tag.strip() for sublist in tags for tag in sublist]
tag_counts = pd.Series(flat_tags).value_counts()
top_10_tags = tag_counts.head(10)
print("Top 10 most popular tags:")
print(top_10_tags)


# ### 11. Are there any relations between the rating and number of people who rated the products?
# Neglect the products that are not reviewed by any person
# 
# Neglect the products that are having zero rating

# In[34]:


# Filter out products with zero rating count and products with a rating of zero
filtered_data = df[(df['rating_count'] != 0) & (df['rating'] != 0)]
plt.scatter(filtered_data['rating_count'], filtered_data['rating'])
plt.xlabel('Number of People Who Rated')
plt.ylabel('Rating')
plt.title('Rating vs. Number of People Who Rated')
plt.show()


# ### 12. What are the top 10 Most Expensive brands?
# 
# Use marked price as the reference to find the most expensive brand

# In[35]:


# Group the data by brand_name and calculate the maximum marked price
brand_max_price = df.groupby('brand_name')['marked_price'].max()
sorted_max_prices = brand_max_price.sort_values(ascending=False)
top_10_expensive_brands = sorted_max_prices.head(10)
print("Top 10 Most Expensive Brands based on Marked Price:")
print("*******************************")
print(top_10_expensive_brands)


# ### 13. What are the top 10 Most Expensive Product Category?
# Use marked price as the reference to find the most expensive brand

# In[36]:


# Group the data by product_tag and calculate the maximum marked price
category_max_price = df.groupby('product_tag')['marked_price'].max()
sorted_max_prices = category_max_price.sort_values(ascending=False)
top_10_expensive_categories = sorted_max_prices.head(10)
print("Top 10 Most Expensive Product Categories based on Marked Price:")
print("..................................")
print(top_10_expensive_categories)


# ### 14. Analyse the Violen Plot of watches of following brands mentioned below ? (5 marks)
# Take Marked Price for Reference
# 
# Take product_tag as watches
# 
# Take brand_tag as tommy-hilfiger, daniel-wellington, armani-exchange, emporio-armani, earnshaw, tissot
# 
# Make sure to write your inference based on the violen plot of following watch brands price
# 

# In[19]:


# Filter the data for watches of the specified brands
brands_of_interest = ['tommy-hilfiger', 'daniel-wellington', 'armani-exchange', 'emporio-armani', 'earnshaw', 'tissot']
filtered_data = df[(df['product_tag'] == 'watches') & (df['brand_tag'].isin(brands_of_interest))]

# Create the Violin Plot
plt.figure(figsize=(12, 6))
sns.violinplot(x=filtered_data['brand_tag'], y=filtered_data['marked_price'])
plt.xlabel('Brand')
plt.ylabel('Marked Price')
plt.title('Violin Plot of Watches by Brand')
plt.xticks(rotation=45)
plt.show()


# ###  15. List top 5 brands which are having most wide range or products
# Use marked price as the reference

# In[20]:


# Group the data by brand_name and calculate the range of marked prices
brand_price_range = df.groupby('brand_name')['marked_price'].agg(lambda x: x.max() - x.min())
sorted_price_ranges = brand_price_range.sort_values(ascending=False)
top_5_wide_range_brands = sorted_price_ranges.head(5)
print("Top 5 Brands with the Widest Range of Products based on Marked Price:")
print(top_5_wide_range_brands)


# ###  Important points for advice to the product company's for their business growth
# 
# * Strengthen Top Brands: Allocate more resources and marketing efforts towards the top-performing brands to further enhance their presence in the market and capitalize on their success.
# 
# * Improve Product Ratings: Focus on improving the quality, design, and customer satisfaction of products with lower ratings. Positive ratings and reviews are crucial for attracting new customers and building trust in the brand.
# 
# * Optimize Pricing Strategy: Analyze competitor pricing and ensure your products are competitively priced. Consider offering promotional discounts or bundle offers to attract price-conscious customers and gain a competitive edge.
# 
# * Enhance Customer Experience: Invest in improving the overall customer experience, including website usability, product descriptions, and customer support. A seamless and positive shopping experience can lead to increased customer loyalty and repeat purchases.
# 
# * Leverage Social Media: Utilize social media platforms to engage with customers, build brand awareness, and showcase new products. Encourage user-generated content and leverage influencer marketing to reach a larger audience and increase brand visibility.
#  
# 

# In[ ]:




