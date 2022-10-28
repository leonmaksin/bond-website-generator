import json

json_file = open('people.json')
data = json.load(json_file)

header = open('header.html','r').read()
footer = open('footer.html','r').read()

count = 0
tabs = "                        "
open_line = tabs+"<div class=\"row\" style=\"margin-top: 60px;\">"
close_line = tabs+"</div>"

print(header)
print(open_line)
for name in data:
    body = f"""
                            <div class="col-lg-3 col-md-6 bottommargin">
                                <div class="team">
                                    <div class="team-image">
                                        <img src="images/{data[name]["image"]}" alt="{name}">
                                            </div>
                                    <div class="team-desc">
                                        <div class="team-title"><h4>{name}</h4><span>{data[name]["role"]}</span></div><br>
                                        <a href="{data[name]["linkedin"]}" class="social-icon si-colored si-linkedin" title="LinkedIn">
                                            <i class="icon-linkedin"></i>
                                            <i class="icon-linkedin"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
    """
    if count != 0 and count % 4 == 0:
        print(close_line+'\n\n'+open_line)
    print(body)
    count += 1
print(close_line)
print(footer)