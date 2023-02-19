from google.cloud import language_v1
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file("ScrapeNews\clash-of-clans-179107-cdbdd23e5bc8.json")

# Instantiates a client
client = language_v1.LanguageServiceClient(credentials=creds)



#function to assign categories to subcategories
def categorize_text(text):
    category = "Others"    #the final variable that will return as result

    category_map = {
        '/Adult': 'Others',
        '/Arts & Entertainment': 'Entertainment',
        '/Autos & Vehicles': 'Others',
        '/Beauty & Fitness': 'Lifestyle',
        '/Books & Literature': 'Others',
        '/Business & Industrial': 'Business',
        '/Computers & Electronics': 'Science/Tech',
        '/Finance': 'Business',
        '/Food & Drink': 'Lifestyle',
        '/Games': 'Entertainment',
        '/Health': 'Health',
        '/Hobbies & Leisure': 'Lifestyle',
        '/Home & Garden': 'Lifestyle',
        '/Internet & Telecom': 'Science/Tech',
        '/Jobs & Education': 'Business',
        '/Law & Government': 'Politics',
        '/Online Communities': 'Others',
        '/People & Society': 'Others',
        '/Pets & Animals': 'Others',
        '/Real Estate': 'Business',
        '/Science': 'Science/Tech',
        '/Sensitive Subjects': 'World',
        '/Shopping': 'Business',
        '/Sports': 'Sports',
        '/Travel & Transportation': 'Lifestyle',
        '/News/Other'  : 'Others',
        '/News/Business' : 'Business',
        '/News/Gossip & Tabloid News' : 'Entertainment',
        '/News/Health News' : 'Health',
        '/News/Local News' : 'World',
        '/News/Politics' : 'Politics',
        '/News/Sports News' : 'Sports',
        '/News/Technology News' : 'Science/Tech',
        '/News/Weather' : 'Weather',
        '/News/World News' : 'World'
    }
    for name in category_map:
        
        if text.lower().startswith(name.lower()):
            category = category_map[name]
        
            return category
    return category





#a function to call the google model to assign sub categories
def classify_content(text):
    # Encode the text as document
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Analyze the category of the text
    response = client.classify_text(document=document)

    # Find the category with the highest confidence
    max_confidence = 0.0
    max_category_name = ""

    # print(response.categories)

    for category in response.categories:
        if category.confidence > max_confidence:
            max_confidence = category.confidence
            max_category_name = category.name


    final_cat = categorize_text(max_category_name)
    # Return the category with the highest confidence
    return [final_cat, max_category_name]



# The text to analyze
# def get_category(text):
#     #text = 'The United States Senate has voted to acquit former President Donald Trump in his second impeachment trial. The final vote was 57-43, short of the two-thirds majority needed to convict Trump.'

#     # Analyzing the text
#     document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
#     response = client.classify_text(request={'document': document},)

    
    
#     #print(response)



#     # Filtering the news categories
#     news_categories = [c for c in response.categories if 'News' in c.name]
#     if len(news_categories) > 0:
#         category_label = news_categories[0].name
#     else:
#         category_label = 'Other'

#     return category_label

# #print(get_category()) # prints "News/Politics"
