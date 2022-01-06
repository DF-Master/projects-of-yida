from google_images_download import google_images_download
import pydeck

# Connenct cards.cdb
con = pydeck.loadDatabase(
    'C:/Users/jiang/Documents/GitHub/projects-of-yida/AI/AI_in_chem/YGO-AI/cdbopen/cards_en.cdb'
)


#
def Search_all(CardID):
    # Get Text with ID
    get_text = pydeck.getText(CardID, 'name')
    print('Card Text is:', get_text)
    card_name = get_text

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

    return card_name


def Crawl_image(card_name):
    response = google_images_download.googleimagesdownload()

    arguments = {
        "keywords": card_name,
        "limit": 99,
        "print_urls": True,
        "output_directory": "H:/chrome-download/google_images_download"
    }  #creating list of arguments

    absolute_image_paths = response.download(
        arguments)  #passing the arguments to the function
    print(absolute_image_paths
          )  #printing absolute paths of the downloaded images


with open(
        'C:/Users/jiang/Documents/GitHub/projects-of-yida/AI/AI_in_chem/YGO-AI/OCR/deck/all_cards.txt'
) as f:
    all_name = []
    for card_id in f:
        if card_id in all_name:
            continue
        else:
            all_name.append(card_id)
            card_name = str(Search_all(card_id))
            try:
                Crawl_image(card_name)
            except:
                Crawl_image("".join(card_name.split(":")))
