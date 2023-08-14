from goofis_ardihikaru.enums.language import Language


async def reformat_name(name: str, about: str, lang: str) -> str:
    # do nothing if this logic below got triggered
    if len(about) < 0 or len(name) < 0:
        return name
    if lang != Language.INDONESIA.value:
        return name

    # starts converting value
    if "merupakan" in about:
        about_arr = about.split("merupakan")
        name = about_arr[0]

    if "adalah" in about:
        about_arr = about.split("adalah")
        name = about_arr[0]

    return name.strip()
