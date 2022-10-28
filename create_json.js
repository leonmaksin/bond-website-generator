const fs = require('fs');
const cheerio = require('cheerio');

dict = {}

fs.readFile('sample.txt', 'utf8', (err, data) => {
    const $ = cheerio.load(data);
    $(".team").each(function () {
        const desc = $(this).find(".team-desc")
        const name = desc.find(".team-title").find("h4").html()
        const role = desc.find(".team-title").find("span").html()
        const linkedin = desc.find("a").attr("href")
        const image = $(this).find(".team-image").find("img").attr("src").replace('images/','')

        dict[name] = {
            "linkedin": linkedin,
            "role": role,
            "image": image
        }
    })
    const dict_stringified = JSON.stringify(dict, null, 4);
    fs.writeFile('people.json', dict_stringified, (err) => console.log(err));
});
