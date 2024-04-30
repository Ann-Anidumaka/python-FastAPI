from main import FastAPI
app = FastAPI
poets = {
    "A": ["Ana Huang", "Arthur Rimbaud"],
    "B": ["Bertolt Brecht", "Bashō"],
    "C": ["Chimamanda Adichie", "Chinua Achebe"],
    "D": ["Danille steel", "Dylan Thomas"],
    "E": ["Emily Dickinson", "Edgar Allan Poe"],
    "F": ["Federico García Lorca", "Fernando Pessoa"],
    "G": ["Gabriela Mistral", "Geoffrey Chaucer"],
    "H": ["Homer", "Henri Cole"],
    "I": ["Ibn Arabi", "Imtiaz Dharker"],
    "J": ["John Keats", "Jalal ad-Din Muhammad Rumi"],
    "K": ["Kahlil Gibran", "Kathleen Jamie"],
    "L": ["Langston Hughes", "Louise Glück"],
    "M": ["Maya Angelou", "Matsuo Bashō"],
    "N": ["Nizar Qabbani", "Naguib Mahfouz"],
    "O": ["Oscar Wilde", "Octavio Paz"],
    "P": ["Pablo Neruda", "Paul Celan"],
    "Q": ["Qabbani", "Qian Qi"],
    "R": ["Rainer Maria Rilke", "Robert Frost"],
    "S": ["Sappho", "Sylvia Plath"],
    "T": ["T. S. Eliot", "Taha Muhammad Ali"],
    "U": ["Ursula K. Le Guin", "Unknown"],
    "V": ["Victor Hugo", "Virgil"],
    "W": ["Walt Whitman", "William Shakespeare"],
    "X": ["Xiao Hong", "Xu Zhimo"],
    "Y": ["Yehuda Amichai", "Yosa Buson"],
    "Z": ["Zbigniew Herbert", "Zora Neale Hurston"],
}


@app.get("/poets/{English_letter}")
async def read_poet(English_letter: str) :
    matched_poet = poets.get(English_letter.upper(), [])
    return{"poet_name": matched_poet}
