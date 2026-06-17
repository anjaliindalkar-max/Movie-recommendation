import tkinter as tk
from tkinter import ttk, messagebox

movies = {
    "Inception": {"genre": "Sci-Fi", "year": 2010, "rating": 8.8},
    "Interstellar": {"genre": "Sci-Fi", "year": 2014, "rating": 8.7},
    "The Martian": {"genre": "Sci-Fi", "year": 2015, "rating": 8.0},
    "Arrival": {"genre": "Sci-Fi", "year": 2016, "rating": 7.9},
    "Dune": {"genre": "Sci-Fi", "year": 2021, "rating": 8.0},

    "Harry Potter": {"genre": "Fantasy", "year": 2001, "rating": 7.6},
    "Fantastic Beasts": {"genre": "Fantasy", "year": 2016, "rating": 6.5},
    "Narnia": {"genre": "Fantasy", "year": 2005, "rating": 6.9},
    "The Hobbit": {"genre": "Fantasy", "year": 2012, "rating": 7.8},
    "Lord of the Rings": {"genre": "Fantasy", "year": 2001, "rating": 8.9},

    "Titanic": {"genre": "Romance", "year": 1997, "rating": 7.9},
    "The Notebook": {"genre": "Romance", "year": 2004, "rating": 7.8},
    "La La Land": {"genre": "Romance", "year": 2016, "rating": 8.0},
    "Me Before You": {"genre": "Romance", "year": 2016, "rating": 7.4},
    "A Walk to Remember": {"genre": "Romance", "year": 2002, "rating": 7.3},

    "The Dark Knight": {"genre": "Action", "year": 2008, "rating": 9.0},
    "Joker": {"genre": "Action", "year": 2019, "rating": 8.4},
    "The Batman": {"genre": "Action", "year": 2022, "rating": 7.8},
    "Logan": {"genre": "Action", "year": 2017, "rating": 8.1},
    "Iron Man": {"genre": "Action", "year": 2008, "rating": 7.9},
}


def recommend_movie():
    selected = movie_var.get()

    if selected not in movies:
        messagebox.showerror(
            "Error",
            "Please select a movie."
        )
        return

    genre = movies[selected]["genre"]

    recommendations = []

    for movie, details in movies.items():
        if movie != selected and details["genre"] == genre:
            recommendations.append(
                (movie, details["rating"])
            )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        f"🎬 Selected Movie : {selected}\n\n"
    )

    result_box.insert(
        tk.END,
        f"🎭 Genre : {genre}\n"
    )

    result_box.insert(
        tk.END,
        f"⭐ Rating : {movies[selected]['rating']}\n"
    )

    result_box.insert(
        tk.END,
        f"📅 Year : {movies[selected]['year']}\n\n"
    )

    result_box.insert(
        tk.END,
        "🔥 Recommended Movies\n\n"
    )

    for i, (movie, rating) in enumerate(recommendations[:5], start=1):
        result_box.insert(
            tk.END,
            f"{i}. {movie}\n"
            f"   Rating : {rating}\n"
            f"   Reason : Similar Genre\n\n"
        )


# ---------------------------
# GUI
# ---------------------------

root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("850x650")
root.configure(bg="#0F172A")

title = tk.Label(
    root,
    text="🎥 MOVIE RECOMMENDATION SYSTEM",
    font=("Segoe UI", 24, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Find movies based on genre similarity",
    font=("Segoe UI", 11),
    bg="#0F172A",
    fg="white"
)
subtitle.pack()

movie_var = tk.StringVar()

combo = ttk.Combobox(
    root,
    textvariable=movie_var,
    values=sorted(movies.keys()),
    width=40,
    font=("Segoe UI", 12)
)
combo.pack(pady=20)

recommend_btn = tk.Button(
    root,
    text="Get Recommendations",
    font=("Segoe UI", 13, "bold"),
    bg="#22C55E",
    fg="white",
    padx=15,
    pady=8,
    command=recommend_movie
)
recommend_btn.pack()

result_box = tk.Text(
    root,
    width=75,
    height=18,
    font=("Consolas", 11),
    bg="#1E293B",
    fg="white"
)
result_box.pack(pady=25)

footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    font=("Segoe UI", 10),
    bg="#0F172A",
    fg="#94A3B8"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
