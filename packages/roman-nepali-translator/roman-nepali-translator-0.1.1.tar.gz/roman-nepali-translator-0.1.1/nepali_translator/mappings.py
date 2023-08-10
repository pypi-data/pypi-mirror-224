import os
from typing import Dict

Mappings = Dict[str, str]

numbers = {
    '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
    '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'
}

basic_vowels = {
    'a': 'अ', 'aa': 'आ', 'ee': 'ई ', 'i': 'इ', 'u': 'उ',
    'oo': 'ऊ', 'Ri': 'ॠ ', 'Ree': 'ॠ', 'e': 'ए', 'ai': 'ऐ',
    'o': 'ओ',
}

consonant_kaars = {
    'aa': 'ा', 'e': 'े', 'ee': 'ी', 'i': 'ि', 'u': 'ु',
    'oo': 'ू', 'o': 'ो', 'au': 'ौ', 'ai': 'ै'
}

akaars = {
    'ka': 'क', 'kha': 'ख', 'ga': 'ग', 'gha': 'घ', 'Nga': 'ङ',
    'NGa': 'ङ्ग', 'cha': 'च', 'chha': 'छ', 'ja': 'ज', 'jha': 'झ',
    'yNa': 'ञ', 'Ta': 'ट', 'Tha': 'ठ', 'Da': 'ड', 'Dha': 'ढ',
    'Na': 'ण', 'ta': 'त', 'tha': 'थ', 'da': 'द', 'dha': 'ध',
    'na': 'न', 'nga': 'ङ', 'pa': 'प', 'pha': 'फ', 'fa': 'फ',
    'ba': 'ब', 'bha': 'भ', 'va': 'भ', 'ma': 'म', 'ya': 'य',
    'ra': 'र', 'la': 'ल', 'wa': 'व', 'sa': 'स', 'sha': 'श',
    'Sha': 'ष', 'ha': 'ह', 'ksha': 'क्ष', 'tra': 'त्र',
    'gya': 'ज्ञ', 'gYa': 'ग्य',
}

halanta = '्'
amkaar = 'ं'
aNNkaar = 'ँ'
Ri = 'ृ'


def get_mappings() -> Mappings:
    all_mappings = {
        **basic_vowels,
        **akaars,
    }

    halantas = {k[:-1]: v + halanta for k, v in akaars.items()}
    all_mappings.update(halantas)

    for rom, sym in consonant_kaars.items():
        kaar_maps = {k + rom: akaars[k + 'a'] + sym for k in halantas}
        all_mappings.update(kaar_maps)

    all_mappings['.'] = '।'
    all_mappings.update(numbers)
    return dict(sorted(all_mappings.items(), key=lambda x: len(x[0]), reverse=True))


def get_word_maps() -> Mappings:
    maps = {}
    filepath = os.path.join(
        os.path.dirname(__file__),
        'words_maps.txt'
    )
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue
            w, uni = line.split()
            maps[w] = uni
    return maps


if __name__ == '__main__':
    all_maps = get_mappings()
    print(all_maps)
