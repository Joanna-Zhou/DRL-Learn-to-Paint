from dataset_parse import *

training_data_index = [
    "user_id",
    "business_id",
    "review_id",
    "review_stars",
    "review_useful",
    "review_funny",
    "review_cool",
    "review_text",
    "review_date",
    "business_name",
    "business_address",
    "business_city",
    "business_state",
    "business_postal_code",
    "business_latitude",
    "business_longitude",
    "business_stars",
    "business_review_count",
    "business_is_open",
    "business_categories",
    "user_name",
    "user_review_count",
    "user_yelping_since",
    "user_useful",
    "user_funny",
    "user_cool",
    "user_fans",
    "user_average_stars",
    "user_compliment_hot",
    "user_compliment_more",
    "user_compliment_profile",
    "user_compliment_cute",
    "user_compliment_list",
    "user_compliment_note",
    "user_compliment_plain",
    "user_compliment_cool",
    "user_compliment_funny",
    "user_compliment_writer",
    "user_compliment_photos"
]

# Creating training data dictionary:
training_data_dictionary = {}
for i in range(len(training_data_index)):
    training_data_dictionary[training_data_index[i]] = i

# Visualizing the first row of data:
for key, value in training_data_dictionary.items():
    if key == "review_text":
        continue
    print(key, "=", training_data[0][value])
