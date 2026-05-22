import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class MainGUI extends JFrame {

    private BookManager manager;

    private JTextField titleField;
    private JTextField authorField;
    private JTextField genreField;
    private JTextField yearField;

    private JTextArea outputArea;

    public MainGUI() {

        manager = new BookManager();

        // ================= SAMPLE BOOKS =================

        manager.addBook(new Book("Harry Potter", "J.K. Rowling", "Fantasy", 1997));
        manager.addBook(new Book("1984", "George Orwell", "Dystopian", 1949));
        manager.addBook(new Book("Dune", "Frank Herbert", "Science Fiction", 1965));

        // ================= FRAME SETTINGS =================

        setTitle("Book Cataloging System");
        setSize(900, 650);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // ================= FONTS =================

        Font labelFont = new Font("Arial", Font.BOLD, 14);
        Font buttonFont = new Font("Arial", Font.BOLD, 13);
        Font outputFont = new Font("Monospaced", Font.PLAIN, 14);
        Font headingFont = new Font("Arial", Font.BOLD, 26);

        // ================= MAIN PANEL =================

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.setBackground(new Color(240, 240, 240));

        mainPanel.setBorder(
                BorderFactory.createEmptyBorder(10, 10, 10, 10)
        );

        // ================= HEADING =================

        JLabel heading = new JLabel(
                "Book Cataloging System",
                JLabel.CENTER
        );

        heading.setFont(headingFont);

        heading.setBorder(
                BorderFactory.createEmptyBorder(10, 10, 20, 10)
        );

        // ================= INPUT PANEL =================

        JPanel inputPanel = new JPanel(new GridLayout(4, 2, 10, 10));

        inputPanel.setBackground(new Color(240, 240, 240));

        inputPanel.setBorder(
                BorderFactory.createTitledBorder("Book Details")
        );

        JLabel titleLabel = new JLabel("Title:");
        titleLabel.setFont(labelFont);

        JLabel authorLabel = new JLabel("Author:");
        authorLabel.setFont(labelFont);

        JLabel genreLabel = new JLabel("Genre:");
        genreLabel.setFont(labelFont);

        JLabel yearLabel = new JLabel("Publication Year:");
        yearLabel.setFont(labelFont);

        titleField = new JTextField();
        authorField = new JTextField();
        genreField = new JTextField();
        yearField = new JTextField();

        inputPanel.add(titleLabel);
        inputPanel.add(titleField);

        inputPanel.add(authorLabel);
        inputPanel.add(authorField);

        inputPanel.add(genreLabel);
        inputPanel.add(genreField);

        inputPanel.add(yearLabel);
        inputPanel.add(yearField);

        // ================= BUTTON PANEL =================

        JPanel buttonPanel = new JPanel(new GridLayout(3, 3, 10, 10));

        buttonPanel.setBackground(new Color(240, 240, 240));

        JButton addButton = new JButton("Add Book");
        JButton removeButton = new JButton("Remove Book");

        JButton searchTitleButton = new JButton("Search Title");
        JButton searchAuthorButton = new JButton("Search Author");
        JButton searchGenreButton = new JButton("Search Genre");

        JButton displayAllButton = new JButton("Display All");

        JButton reportGenreButton = new JButton("Report Genre");
        JButton reportAuthorButton = new JButton("Report Author");

        // ================= BUTTON FONTS =================

        addButton.setFont(buttonFont);
        removeButton.setFont(buttonFont);

        searchTitleButton.setFont(buttonFont);
        searchAuthorButton.setFont(buttonFont);
        searchGenreButton.setFont(buttonFont);

        displayAllButton.setFont(buttonFont);

        reportGenreButton.setFont(buttonFont);
        reportAuthorButton.setFont(buttonFont);

        // ================= BUTTON COLORS =================

        addButton.setBackground(new Color(76, 175, 80));
        addButton.setForeground(Color.WHITE);

        removeButton.setBackground(new Color(244, 67, 54));
        removeButton.setForeground(Color.WHITE);

        displayAllButton.setBackground(new Color(33, 150, 243));
        displayAllButton.setForeground(Color.WHITE);

        // ================= ADD BUTTONS =================

        buttonPanel.add(addButton);
        buttonPanel.add(removeButton);
        buttonPanel.add(displayAllButton);

        buttonPanel.add(searchTitleButton);
        buttonPanel.add(searchAuthorButton);
        buttonPanel.add(searchGenreButton);

        buttonPanel.add(reportGenreButton);
        buttonPanel.add(reportAuthorButton);

        // ================= TOP PANEL =================

        JPanel topPanel = new JPanel();
        topPanel.setLayout(new BorderLayout());

        topPanel.setBackground(new Color(240, 240, 240));

        topPanel.add(inputPanel, BorderLayout.NORTH);
        topPanel.add(buttonPanel, BorderLayout.SOUTH);

        // ================= OUTPUT AREA =================

        outputArea = new JTextArea();

        outputArea.setEditable(false);

        outputArea.setFont(outputFont);

        outputArea.setLineWrap(true);
        outputArea.setWrapStyleWord(true);

        JScrollPane scrollPane = new JScrollPane(outputArea);

        scrollPane.setBorder(
                BorderFactory.createTitledBorder("Book Catalog")
        );

        // ================= ADD COMPONENTS =================

        mainPanel.add(heading, BorderLayout.NORTH);
        mainPanel.add(topPanel, BorderLayout.CENTER);
        mainPanel.add(scrollPane, BorderLayout.SOUTH);

        add(mainPanel);

        // ================= BUTTON ACTIONS =================

        addButton.addActionListener(e -> addBook());

        removeButton.addActionListener(e -> removeBook());

        searchTitleButton.addActionListener(e -> {
            displayBooks(manager.searchByTitle(titleField.getText()));
        });

        searchAuthorButton.addActionListener(e -> {
            displayBooks(manager.searchByAuthor(authorField.getText()));
        });

        searchGenreButton.addActionListener(e -> {
            displayBooks(manager.searchByGenre(genreField.getText()));
        });

        displayAllButton.addActionListener(e -> {
            displayBooks(manager.getAllBooks());
        });

        reportGenreButton.addActionListener(e -> {
            outputArea.setText(manager.reportByGenre());
        });

        reportAuthorButton.addActionListener(e -> {
            outputArea.setText(manager.reportByAuthor());
        });

        setVisible(true);
    }

    // ================= ADD BOOK =================

    private void addBook() {

        try {

            String title = titleField.getText().trim();
            String author = authorField.getText().trim();
            String genre = genreField.getText().trim();

            if (title.isEmpty() ||
                    author.isEmpty() ||
                    genre.isEmpty()) {

                outputArea.setText("Please fill all fields.");
                return;
            }

            int year = Integer.parseInt(yearField.getText());

            Book book = new Book(title, author, genre, year);

            manager.addBook(book);

            JOptionPane.showMessageDialog(
                    this,
                    "Book Added Successfully!"
            );

            clearFields();

        } catch (Exception e) {

            outputArea.setText("Please enter valid data.");
        }
    }

    // ================= REMOVE BOOK =================

    private void removeBook() {

        String title = titleField.getText();

        boolean removed = manager.removeBook(title);

        if (removed) {

            JOptionPane.showMessageDialog(
                    this,
                    "Book Removed Successfully!"
            );

        } else {

            outputArea.setText("Book Not Found!");
        }
    }

    // ================= DISPLAY BOOKS =================

    private void displayBooks(ArrayList<Book> books) {

        outputArea.setText("");

        if (books.isEmpty()) {

            outputArea.setText("No books found.");
            return;
        }

        for (Book book : books) {

            outputArea.append(book.toString() + "\n\n");
        }
    }

    // ================= CLEAR FIELDS =================

    private void clearFields() {

        titleField.setText("");
        authorField.setText("");
        genreField.setText("");
        yearField.setText("");
    }
}