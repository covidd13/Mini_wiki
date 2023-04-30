def emoticon_converter(message):
    words=message.split(" ")
    emojis={
        ":)" : "😂",
        "):" : "😢"
    }
    output=" "
    for word in words:
        outcome+=emojis.get(word,word) + " "
    return output
message=input(">")
print(emoticon_converter(message))

