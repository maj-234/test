import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Long start = System.currentTimeMillis();
        userObject object = new userObject("asd");
        object.getMethod();
        fileWrite_ver_0 fw = new fileWrite_ver_0();
        //fw.fileWrite(fw.fileRead(), "new content");
        System.out.println(fw.fileRead());
        //awtSample.run();
        recForDp dp = new recForDp();
        dp.initDp();
        System.out.println(dp.rec(0, dp.W));
        dp.print();
        var p = new NextPermutation();
        int[] a = new int[]{3, 2, 1};
        while(p.nextPermutation(a)) {
            p.print(a);
        }
        System.out.println(p.count);
        Long end = System.currentTimeMillis();
        Long duration = end - start;
        System.out.println("Execution time is " + duration +"ms");
    }
}