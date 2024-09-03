# only 300 requests per month so be careful while using it (used 7 times till now)
import requests

url = "https://comprehend-it.p.rapidapi.com/predictions/ml-zero-nli-model"

payload = {
	"labels": ["Music & Podcasts", "Gaming & Online Content", "Comedy & Fun", "Education & Information", "Lifestyle", "Movies & Drama", "Shorts", "Sports", "Film & Animation", "Autos & Vehicles"],
	"text": "Thank you to everyone who joined us to celebrate #PokemonWorlds at #NintendoNYC!"
}
headers = {
	"x-rapidapi-key": "13d5549068mshfacb66786474454p1531abjsn8945b82a3b40",
	"x-rapidapi-host": "comprehend-it.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

outputs = data['outputs']

most_relevant_category = max(outputs, key=outputs.get)
print(most_relevant_category)