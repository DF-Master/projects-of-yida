import pydeck

# Connenct cards.cdb
con = pydeck.loadDatabase('AI/AI_in_chem/YGO-AI/cdbopen/cards_cn.cdb')


# Find Card ID
def find(name):
    card_name = pydeck.getCardsFromName(name)
    print('Card ID is: ', card_name)


#
def Search_all(CardID):
    # Get Text with ID
    get_text = pydeck.getText(CardID, 'name')
    print('Card Text is:', get_text)

    get_text = pydeck.getText(CardID, 'desc')
    print('Card Function is:', get_text)

    get_text = pydeck.getText(CardID, 'str1')
    print('Card Tag1 is:', get_text)

    get_text = pydeck.getText(CardID, 'str2')
    print('Card Tag2 is:', get_text)

    # Get Data with ID

    get_text = pydeck.getData(CardID, 'race')
    print('Card Race is:', get_text)

    get_text = pydeck.getData(CardID, 'level')
    print('Card level is:', get_text)

    get_text = pydeck.getData(CardID, 'atk')
    print('Card Atk is:', get_text)

    get_text = pydeck.getData(CardID, 'def')
    print('Card Def is:', get_text)

    get_text = pydeck.getData(CardID, 'type')
    print('Card Type is:', get_text)

    get_text = pydeck.getData(CardID, 'ot')
    print('Card Ot is:', get_text)

    get_text = pydeck.getData(CardID, 'alias')
    print('Card Alias is:', get_text)

    get_text = pydeck.getData(CardID, 'setcode')
    print('Card Setcode is:', get_text)

    get_text = pydeck.getData(CardID, 'attribute')
    print('Card Attribute is:', get_text)

    get_text = pydeck.getData(CardID, 'category')
    print('Card Category is:', get_text)


if __name__ == '__main__':
    find('天霆号 阿宙斯')
    Search_all('79868386')
