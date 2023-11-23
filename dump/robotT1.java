import java.awt.*;
import java.awt.event.KeyEvent;
import java.io.IOException;

public class robotT1 {
    Robot r = new Robot();
    Runtime rt = Runtime.getRuntime();
    String application = "explorer.exe";

    public robotT1() throws AWTException {
    }

    public void type() throws InterruptedException, IOException {
        rt.exec(application);
        Thread.sleep(100);
        r.keyPress(KeyEvent.VK_A);
        Thread.sleep(100);
        r.keyPress(KeyEvent.VK_B);
        Thread.sleep(100);
        r.keyPress(KeyEvent.VK_C);

    }

}
