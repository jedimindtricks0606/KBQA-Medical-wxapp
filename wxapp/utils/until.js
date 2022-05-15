let emojiChar = "☺-😋-😌-😍-😏-😜-😝-😞-😔-😪-😭-😁-😂-😃-😅-😆-👿-😒-😓-😔-😏-😖-😘-😚-😒-😡-😢-😣-😤-😢-😨-😳-😵-😷-😸-😻-😼-😽-😾-😿-🙊-🙋-🙏-✈-🚇-🚃-🚌-🍄-🍅-🍆-🍇-🍈-🍉-🍑-🍒-🍓-🐔-🐶-🐷-👦-👧-👱-👩-👰-👨-👲-👳-💃-💄-💅-💆-💇-🌹-💑-💓-💘-🚲";
//0x1f---
let emoji = [
    "60a", "60b", "60c", "60d", "60f",
    "61b", "61d", "61e", "61f",
    "62a", "62c", "62e",
    "602", "603", "605", "606", "608",
    "612", "613", "614", "615", "616", "618", "619", "620", "621", "623", "624", "625", "627", "629", "633", "635", "637",
    "63a", "63b", "63c", "63d", "63e", "63f",
    "64a", "64b", "64f", "681",
    "68a", "68b", "68c",
    "344", "345", "346", "347", "348", "349", "351", "352", "353",
    "414", "415", "416",
    "466", "467", "468", "469", "470", "471", "472", "473",
    "483", "484", "485", "486", "487", "490", "491", "493", "498", "6b4"
];

function changeEmoji(chatLists) {
    let emojiChars = emojiChar.split('-');
    chatLists.map(v => {
        let content = v["content"];
        if(content.includes('[0x1f')){
            let contents = content.split('[0x1f');
            for(let i = 0; i < contents.length; i++) {
                if(contents[i]){
                    let code = contents[i];
                    code = code.split(']')[0];
                    let index = emoji.findIndex(v => {return v === code});
                    if(index !== -1) {
                        content = content.replace(/\[0x1f[a-zA-Z0-9]{3}\]/, emojiChars[index])
                    }
                
                }
            }
        
        }
        v["content"] = content;
        return v
    })
    return chatLists
}


exports.changeEmoji = changeEmoji