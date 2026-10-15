import requests
import json
from jinja2 import Template

# rs = requests.get("https://hcmue.edu.vn")
# print(rs, rs.status_code)
# print(rs.text)

# Thử vào trang https://dummyjson.com khám phá
pro_text = requests.get("https://dummyjson.com/products", verify=False)
if pro_text.status_code != 200:
    print("Loi")
else:
    json_data = pro_text.json()
    template_output ="""
<html>
<body>
<h1>{{product.title}}</h1>
<h3>{{product.price}}</h3>
<img src="{{product.image}}" />
</body>
</html>
"""
    tenplate=Template(template_output)
    if "products" in json_data:
        for product in json_data["products"]:
            prodata = { "title": product["title"],
                "price": product["price"], "image": product["images"][0]
            }
            html_content = tenplate.render(product=prodata)
            with open(f"report-{product['id']}.html", 'w', encoding='UTF-8') as file:
                file.write(html_content)