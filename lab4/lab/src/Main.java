public class Main {
    public static void main(String[] args) {
        drawLine('#', 40);
        System.out.println();
        Numbers.sample1();
        drawLine('-', 40);

        Numbers.sample2();
        drawLine('-', 40);

        Numbers.getVal(-1);
        System.out.println();
        drawLine('#', 40);
        System.out.println();

        Dates.getDates();
        System.out.println();
        drawLine('#', 40);
        System.out.println();

        Decimals.sample1();
        drawLine('-', 40);

        Decimals.sample2();
        System.out.println();
        drawLine('#', 40);
        System.out.println();

        Print.sample1();
    }

    private static void drawLine(char ch, int length) {
        for (int i = 0; i < length; i++) {
            System.out.print(ch);
        }
        System.out.println();
    }
}