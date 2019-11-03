from graphqlclient import GraphQLClient
import json
from pandas import DataFrame, read_csv, concat

client = GraphQLClient("https://api.yelp.com/v3/graphql")
client.inject_token(
    "Bearer TLPTOgPbMD_UndfePrI51V6Ilig_HNXqVD0LONlj7FW08uYNOMKFQqMJCsyDtguAZYgL6i0lLfETMjGOWlM9lluaMGD-mnof80FrCJ8sEqpcMiBXoIOYnD0crhiQXXYx"
)

query = open("one_business.graphql", "r").read()

business_names = read_csv(
    "business_name_popularity.csv", names=["business", "popularity"]
)
already_fetched = read_csv("business_category_info.csv")
already_fetched_names = set(already_fetched["business_name"])
business_data = []
err_count = 0
for n in business_names["business"]:
    if n in already_fetched_names:
        print("skipping", n)
        continue
    print(n)
    try:
        result = client.execute(query % n)
        payload = json.loads(result)
        business = payload["data"]["search"]["business"][0]
        info = {
            "price": business["price"],
            "business_name": business["name"],
            "immediate_categories": ", ".join(
                {c["title"] for c in business["categories"]}
            ),
            "parent_categories": set(),
        }
        for c in business["categories"]:
            for p in c["parent_categories"]:
                info["parent_categories"].add(p["title"])
        info["parent_categories"] = ",".join(info["parent_categories"])
        business_data.append(info)
        # clean error count on a success
        err_count = 0
    except Exception as e:
        print(e)
        err_count += 1
    if err_count > 3:
        break
concat([already_fetched, DataFrame(business_data)]).to_csv("business_category_info.csv",index=False)
