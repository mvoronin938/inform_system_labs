import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.IntStream;


public class Dates {
    private static DateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
    private static final int concurrencyLevel = 10;

    public static void getDates() {
        List<CompletableFuture<Void>> futures =
                IntStream.range(0, concurrencyLevel)
                        .mapToObj(i -> CompletableFuture.runAsync(Dates::getDateInternal))
                        .toList();

        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();
    }

    private static void getDateInternal() {
        try {
            System.out.println(format.format(format.parse("2024-09-18 19:19:23.000")));
        } catch (Exception ex) {
            System.out.println(String.format("Error: %s", ex.getMessage()));
        }
    }
}
