shtetet = {
    "Kosova": {
        "kryeqyteti": "Prishtina",
        "popullsia": 1800000    
    },
    "Shqiperia": {
        "kryeqyteti": "Tirana",
        "popullsia": 3000000
    },
    "Maqedonia e Veriut": {
        "kryeqyteti": "Shkupi",
        "popullsia": 2000000
    }
}
print(shtetet["Kosova"]["kryeqyteti"])
    
produktet = {
    "tv":300,
    "mouse":5,
    "laptop":1000,
    "keyboard":50
}
print(sorted(produktet.values()))
print(f"produkti me cmimin me te vogel eshte", min(produktet.values()))