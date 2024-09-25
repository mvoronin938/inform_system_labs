import java.util.Random;

public class Numbers {
    static Random rnd = new Random();
    static double[] vals = new double[] {1.0, 2.0, 3.0};

    public static void sample1(){
        boolean flag = rnd.nextBoolean();
        Number n = flag ? new Integer(1) : new Double(2.0);
        System.out.println(String.format("Number is %f", n));
    }

    public static void sample2(){
        while(true)
        {
            try
            {
                boolean flag1 = rnd.nextBoolean();
                boolean flag2 = rnd.nextBoolean();
                Integer n = flag1 ? 1 : flag2 ? 2 : null;
                System.out.println(String.format("Number is %d", n));
            }
            catch (Exception ex)
            {
                System.out.println(String.format("Exception occurred: %s", ex.getMessage()));
                return;
            }
        }
    }

    public static double getVal(int idx) {
        try
        {
            return (idx < 0 || idx >= vals.length) ? null : vals[idx];
        }
        catch (Exception ex)
        {
            System.out.println(String.format("Exception occurred: %s", ex.getMessage()));
            return 0;
        }
    }
}
