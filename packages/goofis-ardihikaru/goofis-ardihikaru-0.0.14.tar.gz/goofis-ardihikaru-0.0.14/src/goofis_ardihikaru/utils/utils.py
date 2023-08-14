from goofis_ardihikaru.enums.language import Language


async def reformat_name(name: str, about: str, lang: str) -> str:
    # do nothing if this logic below got triggered
    if len(about) < 0 or len(name) < 0:
        return name
    if lang != Language.INDONESIA:
        return name

    # starts converting value
    if "merupakan" in name:
        name_arr = name.split("merupakan")
        name = name_arr[0]

    if "adalah" in name:
        name_arr = name.split("adalah")
        name = name_arr[0]

    return name
