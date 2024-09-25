import java.math.BigDecimal;

public class Decimals {
    public static void sample1() {
        System.out.println(new BigDecimal(1.1));
    }

    public static void sample2() {
        BigDecimal d1 = new BigDecimal("1.1");
        BigDecimal d2 = new BigDecimal("1.10");
        System.out.println(d1.equals(d2));
    }
}
