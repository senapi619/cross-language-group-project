import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# ================= BOOK CLASS =================
class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
    
    def __str__(self):
        return f"{self.title} | {self.author} | {self.genre} | {self.publication_year}"


# ================= BOOK MANAGER CLASS =================
class BookManager:
    def __init__(self):
        self.books = [] 
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, title):
        for i, book in enumerate(self.books):
            if str(book.title).lower() == str(title).lower():
                self.books.pop(i)
                return True
        return False
    
    def search_by_title(self, title):
        results = []
        for book in self.books:
            if str(title).lower() in str(book.title).lower():
                results.append(book)
        return results
    
    def search_by_author(self, author):
        results = []
        for book in self.books:
            if str(author).lower() in str(book.author).lower():
                results.append(book)
        return results
    
    def search_by_genre(self, genre):
        results = []
        for book in self.books:
            if str(genre).lower() in str(book.genre).lower():
                results.append(book)
        return results
    
    def get_all_books(self):
        return self.books
    
    def report_by_genre(self):
        genres = []
        for book in self.books:
            if book.genre not in genres:
                genres.append(book.genre)
        
        report = ""
        for genre in genres:
            report += f"=== {genre} ===\n"
            for book in self.books:
                if book.genre.lower() == genre.lower():
                    report += str(book) + "\n"
            report += "\n"
        return report
    
    def report_by_author(self):
        authors = []
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)
        
        report = ""
        for author in authors:
            report += f"=== {author} ===\n"
            for book in self.books:
                if book.author.lower() == author.lower():
                    report += str(book) + "\n"
            report += "\n"
        return report


# ================= MAIN GUI CLASS =================
class BookCatalogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Cataloging System")
        self.root.geometry("900x650")
        self.root.configure(bg="#f0f0f0")
        
        # Create BookManager instance
        self.manager = BookManager()
        
        # ================= SAMPLE BOOKS (stored but NOT displayed initially) =================
        self.manager.add_book(Book("Harry Potter", "J.K. Rowling", "Fantasy", 1997))
        self.manager.add_book(Book("1984", "George Orwell", "Dystopian", 1949))
        self.manager.add_book(Book("Dune", "Frank Herbert", "Science Fiction", 1965))
        
        # Create GUI
        self.create_widgets()
        
        # Start with EMPTY grid (no books shown)
        # self.displayed_books will track what's currently shown
        self.displayed_books = []  # List to track books currently in grid
    
    def create_widgets(self):
        # ================= HEADING =================
        heading = tk.Label(self.root, text="Book Cataloging System", 
                           font=("Arial", 26, "bold"), 
                           bg="#f0f0f0", fg="#333333")
        heading.pack(pady=(10, 20))
        
        # ================= INPUT FRAME =================
        input_frame = tk.LabelFrame(self.root, text="Book Details", 
                                    bg="#f0f0f0", font=("Arial", 12, "bold"))
        input_frame.pack(pady=5, padx=10, fill="x")
        
        # Title row
        tk.Label(input_frame, text="Title:", bg="#f0f0f0", 
                 font=("Arial", 11, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.title_entry = tk.Entry(input_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Author row
        tk.Label(input_frame, text="Author:", bg="#f0f0f0", 
                 font=("Arial", 11, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.author_entry = tk.Entry(input_frame, width=30)
        self.author_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Genre row
        tk.Label(input_frame, text="Genre:", bg="#f0f0f0", 
                 font=("Arial", 11, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.genre_entry = tk.Entry(input_frame, width=30)
        self.genre_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Year row
        tk.Label(input_frame, text="Publication Year:", bg="#f0f0f0", 
                 font=("Arial", 11, "bold")).grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.year_entry = tk.Entry(input_frame, width=30)
        self.year_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # ================= BUTTON FRAME =================
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        # Row 1
        add_btn = tk.Button(button_frame, text="Add Book", bg="#4CAF50", fg="white",
                           font=("Arial", 11, "bold"), width=14, command=self.add_book)
        add_btn.grid(row=0, column=0, padx=5, pady=5)
        
        remove_btn = tk.Button(button_frame, text="Remove Book", bg="#F44336", fg="white",
                              font=("Arial", 11, "bold"), width=14, command=self.remove_book)
        remove_btn.grid(row=0, column=1, padx=5, pady=5)
        
        display_btn = tk.Button(button_frame, text="Display All", bg="#2196F3", fg="white",
                               font=("Arial", 11, "bold"), width=14, command=self.display_all)
        display_btn.grid(row=0, column=2, padx=5, pady=5)
        
        # Row 2
        search_title_btn = tk.Button(button_frame, text="Search Title", bg="#FF9800", fg="white",
                                     font=("Arial", 11, "bold"), width=14, command=self.search_title)
        search_title_btn.grid(row=1, column=0, padx=5, pady=5)
        
        search_author_btn = tk.Button(button_frame, text="Search Author", bg="#FF9800", fg="white",
                                      font=("Arial", 11, "bold"), width=14, command=self.search_author)
        search_author_btn.grid(row=1, column=1, padx=5, pady=5)
        
        search_genre_btn = tk.Button(button_frame, text="Search Genre", bg="#FF9800", fg="white",
                                     font=("Arial", 11, "bold"), width=14, command=self.search_genre)
        search_genre_btn.grid(row=1, column=2, padx=5, pady=5)
        
        # Row 3
        report_genre_btn = tk.Button(button_frame, text="Report Genre", bg="#9C27B0", fg="white",
                                     font=("Arial", 11, "bold"), width=14, command=self.report_genre)
        report_genre_btn.grid(row=2, column=0, padx=5, pady=5)
        
        report_author_btn = tk.Button(button_frame, text="Report Author", bg="#9C27B0", fg="white",
                                      font=("Arial", 11, "bold"), width=14, command=self.report_author)
        report_author_btn.grid(row=2, column=1, padx=5, pady=5)
        
        # ================= OUTPUT AREA (Table) =================
        output_frame = tk.LabelFrame(self.root, text="Book Catalog", 
                                     bg="#f0f0f0", font=("Arial", 12, "bold"))
        output_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Create Treeview (table)
        columns = ("Title", "Author", "Genre", "Year")
        self.tree = ttk.Treeview(output_frame, columns=columns, show="headings", height=10)
        
        # Define headings
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Year", text="Year")
        
        # Define column widths
        self.tree.column("Title", width=200)
        self.tree.column("Author", width=180)
        self.tree.column("Genre", width=120)
        self.tree.column("Year", width=80)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        self.tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)
    
    # ================= DISPLAY BOOKS IN GRID =================
    def display_books(self, books):
        # Clear current table
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add books to table
        for book in books:
            self.tree.insert("", "end", values=(
                book.title,
                book.author,
                book.genre,
                book.publication_year
            ))
        
        # Store what's currently displayed
        self.displayed_books = books.copy()
    
    # ================= ADD BOOK =================
    def add_book(self):
        try:
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()
            genre = self.genre_entry.get().strip()
            year_text = self.year_entry.get().strip()
            
            # Validation
            if not title or not author or not genre or not year_text:
                messagebox.showwarning("Warning", "Please fill all fields.")
                return
            
            year = int(year_text)
            book = Book(title, author, genre, year)
            self.manager.add_book(book)
            
            # Add to currently displayed books (accumulate)
            self.displayed_books.append(book)
            
            # Refresh grid with accumulated books
            self.display_books(self.displayed_books)
            
            # Clear input fields
            self.clear_fields()
            
            messagebox.showinfo("Success", f"Book '{title}' Added Successfully!")
            
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid year (numbers only).")
    
    # ================= REMOVE BOOK =================
    def remove_book(self):
        # Get selected item from table
        selected = self.tree.selection()
        
        if selected:
            # Get the title of selected book
            values = self.tree.item(selected[0])["values"]
            title = values[0]
            
            # Remove from manager
            removed = self.manager.remove_book(title)
            
            if removed:
                # Remove from displayed books list
                for i, book in enumerate(self.displayed_books):
                    if book.title.lower() == title.lower():
                        self.displayed_books.pop(i)
                        break
                
                # Refresh grid with updated displayed books
                self.display_books(self.displayed_books)
                self.clear_fields()
                messagebox.showinfo("Success", f"Book '{title}' Removed Successfully!")
            else:
                messagebox.showwarning("Warning", "Book Not Found!")
        else:
            # If nothing selected, try by title field
            title = self.title_entry.get().strip()
            if title:
                removed = self.manager.remove_book(title)
                if removed:
                    # Remove from displayed books list
                    for i, book in enumerate(self.displayed_books):
                        if book.title.lower() == title.lower():
                            self.displayed_books.pop(i)
                            break
                    
                    # Refresh grid with updated displayed books
                    self.display_books(self.displayed_books)
                    self.clear_fields()
                    messagebox.showinfo("Success", f"Book '{title}' Removed Successfully!")
                else:
                    messagebox.showwarning("Warning", f"Book '{title}' Not Found!")
            else:
                messagebox.showwarning("Warning", "Select a book from the list or enter a title to remove.")
    
    # ================= SEARCH METHODS =================
    def search_title(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Enter a title to search.")
            return
        results = self.manager.search_by_title(title)
        if results:
            self.display_books(results)
        else:
            messagebox.showinfo("Info", f"No books found with title containing '{title}'")
    
    def search_author(self):
        author = self.author_entry.get().strip()
        if not author:
            messagebox.showwarning("Warning", "Enter an author to search.")
            return
        results = self.manager.search_by_author(author)
        if results:
            self.display_books(results)
        else:
            messagebox.showinfo("Info", f"No books found by author '{author}'")
    
    def search_genre(self):
        genre = self.genre_entry.get().strip()
        if not genre:
            messagebox.showwarning("Warning", "Enter a genre to search.")
            return
        results = self.manager.search_by_genre(genre)
        if results:
            self.display_books(results)
        else:
            messagebox.showinfo("Info", f"No books found in genre '{genre}'")
    
    def display_all(self):
        # Show ALL books from manager (including hardcoded samples)
        all_books = self.manager.get_all_books()
        if all_books:
            self.display_books(all_books)
            # Update displayed_books to all books
            self.displayed_books = all_books.copy()
        else:
            self.display_books([])
            messagebox.showinfo("Info", "No books in catalog.")
    
    def report_genre(self):
        report = self.manager.report_by_genre()
        report_window = tk.Toplevel(self.root)
        report_window.title("Report by Genre")
        report_window.geometry("500x400")
        
        text_area = scrolledtext.ScrolledText(report_window, font=("Courier", 11))
        text_area.pack(fill="both", expand=True, padx=10, pady=10)
        text_area.insert(tk.END, report if report else "No books in catalog.")
        text_area.configure(state="disabled")
    
    def report_author(self):
        report = self.manager.report_by_author()
        report_window = tk.Toplevel(self.root)
        report_window.title("Report by Author")
        report_window.geometry("500x400")
        
        text_area = scrolledtext.ScrolledText(report_window, font=("Courier", 11))
        text_area.pack(fill="both", expand=True, padx=10, pady=10)
        text_area.insert(tk.END, report if report else "No books in catalog.")
        text_area.configure(state="disabled")
    
    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)


# ================= MAIN ENTRY POINT =================
if __name__ == "__main__":
    root = tk.Tk()
    app = BookCatalogApp(root)
    root.mainloop()