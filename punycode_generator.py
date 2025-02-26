import itertools
import idna

def generate_homoglyphs(domain):
    homoglyphs = {
        'a': ['à', 'á', 'â', 'ã', 'ä', 'å', 'ā', 'ă', 'ǎ', 'ȧ', 'ạ', 'ả', 'ȁ', 'ȃ'],
        'c': ['ç', 'ć', 'ĉ', 'ċ', 'č'],
        'e': ['è', 'é', 'ê', 'ë', 'ē', 'ĕ', 'ė', 'ę', 'ě'],
        'i': ['ì', 'í', 'î', 'ï', 'ī', 'ĭ', 'į', 'ı'],
        'o': ['ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'ō', 'ŏ', 'ő'],
        'u': ['ù', 'ú', 'û', 'ü', 'ū', 'ŭ', 'ů', 'ű', 'ų'],
        'l': ['ł'],
        'n': ['ñ', 'ń', 'ņ', 'ň', 'ŉ'],
        's': ['ś', 'ŝ', 'ş', 'š'],
        't': ['ţ', 'ť', 'ŧ'],
        'y': ['ý', 'ÿ'],
        'z': ['ź', 'ż', 'ž'],
        'g': ['ģ'],
    }
    
    domain_parts = domain.split('.')
    main_domain = domain_parts[0]
    tld = '.'.join(domain_parts[1:]) if len(domain_parts) > 1 else ''
    
    # Generate combinations with homoglyph substitutions
    indices = [i for i, letter in enumerate(main_domain) if letter in homoglyphs]
    
    lookalikes = []
    for i in indices:
        for glyph in homoglyphs[main_domain[i]]:
            new_domain = main_domain[:i] + glyph + main_domain[i+1:]
            lookalikes.append(new_domain + ('.' + tld if tld else ''))
    
    return lookalikes

def convert_to_punycode(domains):
    punycode_domains = {}
    for domain in domains:
        try:
            punycode_domains[domain] = idna.encode(domain).decode('utf-8')
        except idna.IDNAError:
            pass  # Ignore domains that cannot be encoded
    return punycode_domains

def main():
    domain = input("Enter a domain (e.g., google.com): ").strip()
    lookalike_domains = generate_homoglyphs(domain)
    punycode_domains = convert_to_punycode(lookalike_domains)
    
    print("\nLook-alike domains and their Punycode equivalents:")
    for original, punycode in punycode_domains.items():
        print(f"{original} => {punycode}")

if __name__ == "__main__":
    main()
