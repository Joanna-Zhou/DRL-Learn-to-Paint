from graphqlclient import GraphQLClient
import json
from pandas import DataFrame

client = GraphQLClient("https://api.yelp.com/v3/graphql")
client.inject_token(
    "Bearer TLPTOgPbMD_UndfePrI51V6Ilig_HNXqVD0LONlj7FW08uYNOMKFQqMJCsyDtguAZYgL6i0lLfETMjGOWlM9lluaMGD-mnof80FrCJ8sEqpcMiBXoIOYnD0crhiQXXYx"
)

query = open("business_meta.graphql", "r").read()

offset = 0
total = 1
business_data = []
while offset < total:
    print(str(offset), "batch")
    result = client.execute(query % offset)
    payload = json.loads(result)
    retry = 0
    if not payload["data"]["search"]:
        break
    search = payload["data"]["search"]
    total = search["total"]
    businesses = search["business"]
    for business in businesses:
        info = {
            "business_id": business["id"],
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
    offset += 50
DataFrame(business_data).to_csv("business_meta_5000.csv")

