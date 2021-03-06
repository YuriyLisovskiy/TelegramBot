letter_map_en_ua = {
	'q': 'й',
	'w': 'ц',
	'e': 'у',
	'r': 'к',
	't': 'е',
	'y': 'н',
	'u': 'г',
	'i': 'ш',
	'o': 'щ',
	'p': 'з',
	'[': 'х',
	']': 'ї',
	'a': 'ф',
	's': 'і',
	'd': 'в',
	'f': 'а',
	'g': 'п',
	'h': 'р',
	'j': 'о',
	'k': 'л',
	'l': 'д',
	';': 'ж',
	'\'': 'є',
	'z': 'я',
	'x': 'ч',
	'c': 'с',
	'v': 'м',
	'b': 'и',
	'n': 'т',
	'm': 'ь',
	',': 'б',
	'.': 'ю',
	'/': '.',
	'Q': 'Й',
	'W': 'Ц',
	'E': 'У',
	'R': 'К',
	'T': 'Е',
	'Y': 'Н',
	'U': 'Г',
	'I': 'Ш',
	'O': 'Щ',
	'P': 'З',
	'{': 'Х',
	'}': 'Ї',
	'A': 'Ф',
	'S': 'І',
	'D': 'В',
	'F': 'А',
	'G': 'П',
	'H': 'Р',
	'J': 'О',
	'K': 'Л',
	'L': 'Д',
	':': 'Ж',
	'"': 'Є',
	'Z': 'Я',
	'X': 'Ч',
	'C': 'С',
	'V': 'М',
	'B': 'И',
	'N': 'Т',
	'M': 'Ь',
	'<': 'Б',
	'>': 'Ю',
	'?': ',',
	'&': '?'
}


def convert_text(text):
	return ''.join([letter_map_en_ua[x] if x in letter_map_en_ua else x for x in text])