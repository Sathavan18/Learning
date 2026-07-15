public class DrawBox {

  static String drawBox(int width, int height) {
    String top = "+" + ("-".repeat(width)) + "+";
    String middle_row = "|" + (" ".repeat(width)) + "|\n";
    String middle = middle_row.repeat(height);
    String bottom = top;
    return top + "\n" + middle + bottom;
  }

  static void assertThat(String name, String actual, String expected) {
    System.out.println(name + ": " + (expected.trim().equals(actual.trim()) ? "PASS" : "FAIL: \n" + actual));
  }

  public static void main(String[] args) {
    System.out.println("==== NEW TEST RUN ====");

    assertThat("should draw a 2x2 box", drawBox(2, 2),
    """
    +--+
    |  |
    |  |
    +--+""");

    assertThat("should draw a 6x3 box", drawBox(6, 3),
    """
    +------+
    |      |
    |      |
    |      |
    +------+""");
  }
}