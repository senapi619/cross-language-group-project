import java.util.ArrayList;

public class BookManager {

    private ArrayList<Book> books;

    // Constructor
    public BookManager() {

        books = new ArrayList<>();
    }

    // ================= ADD BOOK =================

    public void addBook(Book book) {

        books.add(book);
    }

    // ================= REMOVE BOOK =================

    public boolean removeBook(String title) {

        for (int i = 0; i < books.size(); i++) {

            if (books.get(i).getTitle().equalsIgnoreCase(title)) {

                books.remove(i);
                return true;
            }
        }

        return false;
    }

    // ================= SEARCH BY TITLE =================

    public ArrayList<Book> searchByTitle(String title) {

        ArrayList<Book> results = new ArrayList<>();

        for (Book book : books) {

            if (book.getTitle().toLowerCase().contains(title.toLowerCase())) {

                results.add(book);
            }
        }

        return results;
    }

    // ================= SEARCH BY AUTHOR =================

    public ArrayList<Book> searchByAuthor(String author) {

        ArrayList<Book> results = new ArrayList<>();

        for (Book book : books) {

            if (book.getAuthor().toLowerCase().contains(author.toLowerCase())) {

                results.add(book);
            }
        }

        return results;
    }

    // ================= SEARCH BY GENRE =================

    public ArrayList<Book> searchByGenre(String genre) {

        ArrayList<Book> results = new ArrayList<>();

        for (Book book : books) {

            if (book.getGenre().toLowerCase().contains(genre.toLowerCase())) {

                results.add(book);
            }
        }

        return results;
    }

    // ================= GET ALL BOOKS =================

    public ArrayList<Book> getAllBooks() {

        return books;
    }

    // ================= REPORT BY GENRE =================

    public String reportByGenre() {

        StringBuilder report = new StringBuilder();

        ArrayList<String> genres = new ArrayList<>();

        for (Book book : books) {

            if (!genres.contains(book.getGenre())) {

                genres.add(book.getGenre());
            }
        }

        for (String genre : genres) {

            report.append("=== ").append(genre).append(" ===\n");

            for (Book book : books) {

                if (book.getGenre().equalsIgnoreCase(genre)) {

                    report.append(book).append("\n");
                }
            }

            report.append("\n");
        }

        return report.toString();
    }

    // ================= REPORT BY AUTHOR =================

    public String reportByAuthor() {

        StringBuilder report = new StringBuilder();

        ArrayList<String> authors = new ArrayList<>();

        for (Book book : books) {

            if (!authors.contains(book.getAuthor())) {

                authors.add(book.getAuthor());
            }
        }

        for (String author : authors) {

            report.append("=== ").append(author).append(" ===\n");

            for (Book book : books) {

                if (book.getAuthor().equalsIgnoreCase(author)) {

                    report.append(book).append("\n");
                }
            }

            report.append("\n");
        }

        return report.toString();
    }
}