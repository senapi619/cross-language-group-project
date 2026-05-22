public class Book {

    private String title;
    private String author;
    private String genre;
    private int publicationYear;

    // Constructor
    public Book(String title, String author, String genre, int publicationYear) {
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.publicationYear = publicationYear;
    }

    // Getters
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getGenre() {
        return genre;
    }

    public int getPublicationYear() {
        return publicationYear;
    }

    // Display format
    @Override
    public String toString() {
        return title + " | " + author + " | " + genre + " | " + publicationYear;
    }
}